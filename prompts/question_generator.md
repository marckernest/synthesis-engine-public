# 🤔 Question Generator — Stage 2 Prompt #3

## Objective: Discovery Question Synthesis

Convert gap analysis into interview pipeline catalysts:

- **Strategic Questions:** High-level value alignment checks  
- **Technical Deep-Dive:** Solutions architecture enablement
- **Customer Success Integration:** Account strategy mapping

**Synthesis Goal:** Build direct interview pipeline for executive engagement.

---

## Input Source (Gap Analysis Results):
```
<gap_analysis_output>
[Output from Gap Assessor prompt]
</gap_analysis_output>
```

## Synthesis Framework:

### 1. Executive Questions (CEO/C-Level)
- Value alignment checks for partnership discussions
- Strategic priority mapping to our solutions
- Success metric identification

### 2. Solutions Engineering Questions  
- Technical enablement deep-dives
- Integration complexity assessments
- Modernization opportunity sizing

### 3. Customer Success Questions
- Account strategy considerations
- Migration path identification
- Adoption friction points

---

## Question Synthesis Rules:

**DO:**
- Frame questions as "How can we help with X?"  
- Connect to measurable business outcomes
- Link to specific capabilities mentioned in wiki

**DON'T:**
- Ask basic "tell me about yourself" questions
- Make assumptions not supported by data
- Over-focus on technical implementation without business value

---

## Output Format:
```json
{
  "strategic_questions": [
    {
      "topic": "string", 
      "question": "string",
      "target_audience": "CEO|Head of Eng|CISO",
      "purpose": "align|validate|identify"
    }
  ],
  "technical_questions": [...],
  "interview_pipeline": [
    {
      "stage": "exec_briefing|technical_workshop|sales_enablement",
      "questions": [...]
    }
  ]
}
```

---

## Business Outcome Mapping:

For each question set, map to:
- **Orchestration:** Multi-agent workflows for automation tasks
- **Data Engineering:** Real-time processing requirements  
- **Security Operations:** Threat detection/DR capabilities
- **Cloud Modernization:** Infrastructure optimization opportunities

---