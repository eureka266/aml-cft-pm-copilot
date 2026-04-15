# Workflow: Transaction Screening

## Last Reviewed
- Date: YYYY-MM-DD
- Owner: [Name]
- Status: Draft / Reviewed / Approved

## Goal
Describe the goal of transaction screening.

## Primary Actor
- compliance analyst
- risk analyst
- payment operations reviewer
- investigator

## Trigger
Examples:
- reviewing a suspicious transfer
- checking inbound funds
- checking outbound transfer risk
- responding to alert or investigation

## Preconditions
- transaction hash is available
- network is known
- access permission is available

## Input
- transaction hash
- chain / network
- optional linked case
- optional analyst note

## Main Steps
1. User inputs a transaction hash
2. System analyzes the transaction context
3. System surfaces risk indicators and evidence
4. User reviews counterparties, flows, and risk context
5. User decides whether to approve, escalate, monitor, or investigate further

## System Response
May include:
- transaction-level risk result
- counterparties
- fund flow context
- entity associations
- suspicious indicators
- evidence summary

## Key Decision Points
- Is the transaction low-risk, medium-risk, or high-risk?
- Is additional investigation required?
- Should the related address/entity be monitored?
- Should a case be opened?

## Exceptions / Edge Cases
- unsupported chain
- internal transfers with unclear context
- missing enrichment
- multi-hop complexity
- partial visibility

## Output
- screening result
- analyst decision
- escalation path
- new monitoring or case creation
- evidence summary

## Success Criteria
- transaction context is understandable
- evidence is sufficient for analyst review
- escalation path is clear
- related entities and patterns are discoverable

## Related Modules
- flow tracing
- monitoring
- case management
- reporting
- analytics
- MetaSleuth linkage if applicable

## Data Objects
- transaction
- address
- counterparty
- flow graph
- case
- evidence note

## Demo Notes
Emphasize:
- evidence-backed risk context
- flow visibility
- decision support
- investigation handoff

## PRD Notes
Pay attention to:
- transaction result structure
- trace depth expectations
- counterparties and linked entities
- analyst note workflow
- exportable evidence
- performance and usability

## Guardrails
- do not claim full certainty in attribution
- do not claim legal conclusions
- do not imply complete chain visibility in all cases