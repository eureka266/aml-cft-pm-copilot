# Workflow: Address Screening

## Last Reviewed
- Date: YYYY-MM-DD
- Owner: [Name]
- Status: Draft / Reviewed / Approved

## Goal
Describe the goal of address screening.

## Primary Actor
- compliance analyst
- risk analyst
- operations reviewer
- investigator
- other

## Trigger
When does this workflow start?

Examples:
- onboarding a wallet
- reviewing a counterparty
- reviewing inbound/outbound exposure
- investigating suspicious activity

## Preconditions
- user has access
- address is available
- relevant chain is supported
- other prerequisites

## Input
- wallet address
- chain / network
- optional labels / notes
- optional linked case / entity

## Main Steps
1. User submits an address for screening
2. System retrieves risk-related information
3. System presents risk result and supporting evidence
4. User interprets result
5. User may escalate into monitoring, case handling, or deeper investigation

## System Response
Describe what the system returns:
- risk level
- labels / categories
- evidence summary
- linked entities or behavior indicators
- other relevant output

## Key Decision Points
- Is the risk acceptable?
- Does this require manual review?
- Does this require continuous monitoring?
- Does this require escalation to case management?

## Exceptions / Edge Cases
- unsupported chain
- incomplete data
- ambiguous ownership
- conflicting signals
- unavailable evidence
- missing enrichment

## Output
- screening result
- analyst decision
- linked case or note
- monitoring decision
- follow-up recommendation

## Success Criteria
- result is returned quickly
- evidence is understandable
- analyst can make or escalate a decision
- output is traceable and reusable

## Related Modules
- risk result page
- monitoring
- case management
- reporting
- analytics

## Data Objects
- address
- screening result
- risk label
- entity
- case note
- alert (if applicable)

## Demo Notes
For demo purposes, emphasize:
- clarity of result
- explainability
- speed to evidence
- escalation path

## PRD Notes
For PRD generation, pay attention to:
- input validation
- result schema
- edge cases
- collaboration workflow
- auditability
- performance expectations

## Guardrails
- do not claim guaranteed legal determination
- do not claim automatic blocking unless confirmed
- do not imply perfect attribution