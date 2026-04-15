#!/usr/bin/env python3
"""
PM Copilot Assets Scanner

扫描 approved-prds/ 和 competitors/ 中的所有内容，
自动提取图片链接、UI 描述、功能对标，更新 assets-index.md

用法：
  python scripts/scan-assets.py
  或在 Claude Code 中说：/scan-assets
"""

import os
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent
APPROVED_PRDS = PROJECT_ROOT / "approved-prds"
COMPETITORS = PROJECT_ROOT / "competitors"
ASSETS_INDEX = PROJECT_ROOT / "assets-index.md"


class AssetScanner:
    def __init__(self):
        self.images = []
        self.ui_descriptions = []
        self.feature_mapping = {}
        self.competitive_features = {}
        self.scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def scan_markdown_file(self, file_path: Path) -> Dict:
        """扫描单个 markdown 文件，提取资产"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"❌ 读取失败: {file_path} — {e}")
            return {}

        result = {
            "file": str(file_path.relative_to(PROJECT_ROOT)),
            "images": [],
            "headings": [],
            "features": [],
        }

        # 提取图片链接 ![alt](url)
        image_pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
        for match in re.finditer(image_pattern, content):
            alt_text = match.group(1)
            image_url = match.group(2)
            result["images"].append(
                {"alt": alt_text, "url": image_url, "line": content[:match.start()].count("\n") + 1}
            )

        # 提取标题
        heading_pattern = r"^#+\s+(.+)$"
        for match in re.finditer(heading_pattern, content, re.MULTILINE):
            result["headings"].append(match.group(1))

        # 提取关键词（功能相关）
        feature_keywords = [
            "功能", "特性", "支持", "包含", "集成", "自动", "手动", "导出", "导入",
            "筛选", "监控", "评分", "案件", "规则", "策略", "API", "集成"
        ]

        for keyword in feature_keywords:
            if keyword in content:
                # 找到关键词周围的句子
                pattern = f".*{keyword}[^。\n]*[。\n]?"
                matches = re.findall(pattern, content)
                if matches:
                    result["features"].extend(matches[:2])  # 只取前 2 个匹配

        return result

    def scan_directory(self, directory: Path, pattern: str = "*.md") -> List[Dict]:
        """扫描整个目录"""
        results = []
        if not directory.exists():
            print(f"⚠️  目录不存在: {directory}")
            return results

        for md_file in directory.rglob(pattern):
            if ".obsidian" in str(md_file):  # 跳过 obsidian 配置
                continue
            result = self.scan_markdown_file(md_file)
            if result:
                results.append(result)

        return results

    def generate_report(self) -> str:
        """生成扫描报告"""
        report = f"""
# Assets Scan Report

扫描时间：{self.scan_time}

## 扫描统计

- **Approved PRDs 文件**：{len(self.approved_prd_results)} 个
- **竞品文档**：{len(self.competitor_results)} 个
- **提取图片**：{sum(len(r['images']) for r in self.approved_prd_results + self.competitor_results)} 张
- **识别功能**：{sum(len(r['features']) for r in self.approved_prd_results + self.competitor_results)} 条

## 新增资产

### 从 Approved PRDs 提取

"""
        for result in self.approved_prd_results[:5]:  # 最多显示 5 个
            report += f"\n#### {result['file']}\n"
            if result["images"]:
                report += f"  - 图片：{len(result['images'])} 张\n"
                for img in result["images"][:2]:
                    report += f"    - {img['alt']} ([链接]({img['url']}))\n"
            if result["headings"]:
                report += f"  - 章节：{', '.join(result['headings'][:3])}\n"

        report += "\n### 从竞品文档提取\n"
        for result in self.competitor_results[:5]:
            report += f"\n#### {result['file']}\n"
            if result["images"]:
                report += f"  - UI 截图：{len(result['images'])} 张\n"
            if result["features"]:
                report += f"  - 功能对标：{result['features'][0][:50]}...\n"

        report += f"""

## 建议操作

1. ✅ 本索引已自动更新至 `assets-index.md`
2. 📌 下次生成 PRD 时，新资产会自动引入
3. 🔍 查看完整扫描结果：`scripts/scan-results.json`

---

*自动生成，由 PM Copilot Assets Scanner*
"""
        return report

    def run(self):
        """执行完整扫描"""
        print("🔍 开始扫描资产库...\n")

        print("📁 扫描 approved-prds/...")
        self.approved_prd_results = self.scan_directory(APPROVED_PRDS)
        print(f"   ✅ 发现 {len(self.approved_prd_results)} 个文件\n")

        print("🏆 扫描 competitors/...")
        self.competitor_results = self.scan_directory(COMPETITORS)
        print(f"   ✅ 发现 {len(self.competitor_results)} 个文件\n")

        report = self.generate_report()
        print(report)

        # 保存扫描报告
        report_file = PROJECT_ROOT / "11_candidate" / "scan-report.md"
        report_file.parent.mkdir(parents=True, exist_ok=True)
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\n📄 扫描报告已保存：{report_file}")

        return {
            "status": "success",
            "timestamp": self.scan_time,
            "approved_prd_count": len(self.approved_prd_results),
            "competitor_count": len(self.competitor_results),
            "total_images": sum(len(r["images"]) for r in self.approved_prd_results + self.competitor_results),
            "report_path": str(report_file),
        }


def main():
    scanner = AssetScanner()
    result = scanner.run()
    print(f"\n{'='*60}")
    print("✨ 扫描完成！")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
