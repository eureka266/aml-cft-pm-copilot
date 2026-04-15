# Guardrails

## Last Reviewed
- Date: YYYY-MM-DD
- Owner: [Name]
- Status: Draft / Reviewed / Approved

## Purpose
This file defines what Claude Code and other AI workflows must not claim, must escalate, or must phrase carefully.

## Rule Categories
- product capability guardrails
- compliance guardrails
- external messaging guardrails
- pricing / packaging guardrails
- workflow guardrails

---

## 1. Product Capability Guardrails

### Must Not Claim
- The system automatically makes legal determinations
- The system automatically files regulatory reports without human review
- The system automatically blocks transactions unless explicitly confirmed in source files
- The system automatically configures all rules by itself unless explicitly confirmed
- The system supports a feature not documented in authoritative files

### Must Phrase Carefully
- “can help”
- “supports”
- “enables review”
- “assists analysts”
- “provides evidence for”
- “helps accelerate”

### Must Escalate
- requests about unsupported workflows
- requests asking for certainty when the source only supports assistance
- claims involving direct regulatory guarantees

---

## 2. Compliance Guardrails

### Must Not State
- legal conclusions as facts
- guaranteed compliance outcomes
- regulator acceptance without support
- filing completion without human review

### Must Escalate
- jurisdiction-specific legal interpretation
- regulatory advice
- law enforcement outcome guarantees

---

## 3. External Messaging Guardrails

### Allowed Tone
- factual
- evidence-based
- controlled
- not over-promising

### Not Allowed
- “fully automated compliance”
- “guaranteed safe”
- “eliminates AML risk”
- “regulator-approved” unless explicitly supported

---

## 4. Pricing / Packaging Guardrails

### Must Not State
- exact pricing if not confirmed
- packaging commitments not in source files
- commercial promises not validated

---

## 5. Draft Handling Rules

### Candidate Knowledge
New ideas discovered in discussion must go to:
- `11_candidate/facts/`
- `11_candidate/workflows/`
- `11_candidate/copy/`
- `11_candidate/contradictions/`

### Never Do
- silently promote candidate content into authoritative fact files
- treat draft outputs as approved messaging

---

## 6. Contradiction Handling

If two sources conflict:
1. do not choose silently
2. record the contradiction
3. mark the impact area
4. request review

---

## 7. Safe Default Language

Preferred expressions:
- “supports”
- “helps teams”
- “enables analysts to”
- “can be used to”
- “is designed to”

Avoid:
- “guarantees”
- “fully automates”
- “eliminates”
- “proves”
- “ensures compliance”