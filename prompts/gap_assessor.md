# 🔍 Gap Assessor — Stage 2 Prompt #2

## Objective: Technical Friction Analysis

Analyze strategic gaps & opportunities from company profile:

- **Explicit Gaps:** Challenges, risks, needs stated in wiki
- **Implicit Gaps:** Technology debt areas mentioned
- **Market Pressures:** Competitive or regulatory headwinds noted
- **Investment Opportunities:** Tech stack completeness assessment

**Synthesis Goal:** Identify clear entry vectors for solutions engineering.

---

## Input Source:
```
<company_profile_wiki>
[Wiki page content here]
</company_profile_wiki>
```

## Analysis Framework:

### 1. Technology Gaps
- What capabilities are missing from their stack?
- Which integrations are manually maintained?
- Where do they show "legacy" or "on-prem" indicators?

### 2. Market Friction Points
- Are there compliance/regulatory constraints mentioned?
- Do they indicate scalability limitations?
- What customer complaints or challenges surface?

### 3. Investment Opportunities  
- Technology modernization vectors
- Automation acceleration points
- Data governance gaps
- AI/ML capability readiness

---

## Output Format:
```json
{
  "explicit_gaps": ["gap1", "gap2"],
  "implicit_gaps": ["inferred_gap1", "inferred_gap2"],
  "market_friction": ["friction1", "friction2"],
  "investment_vectors": [
    {
      "area": "string",
      "priority": "high|medium|low",
      "rationale": "string"
    }
  ]
}
```

---

## Solutions Engineering Map:
For each gap, map to potential solutions:
- **Orchestration Layer:** How do we automate this friction?
- **Data Layer:** What data governance gaps exist?  
- **Infrastructure Layer:** Where can we modernize?
- **AI/ML Layer:** What intelligent automation fits here?

---