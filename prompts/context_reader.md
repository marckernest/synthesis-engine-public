# 📋 Context Reader — Stage 2 Prompt #1

## Objective: Strategic Challenge ID (Who/What/How)

Read company profile and extract foundational intelligence:

- **Entity:** Company name & core identity
- **Mission:** Value proposition & strategic focus
- **Tech Stack:** Infrastructure capabilities mentioned
- **Market Presence:** Industry positioning & customer base

**Synthesis Goal:** Build knowledge base for partnership discussions.

---

## Input Source:
```
<company_profile_wiki>
[Wiki page content here]
</company_profile_wiki>
```

## Extraction Framework:
1. Identify primary business verticals served
2. Map technology differentiators mentioned
3. Note market positioning claims (e.g., "market leader", "emerging challenger")
4. Extract explicit/implicit value propositions

---

## Output Format:
```json
{
  "entity": "string",
  "core_mission": "string", 
  "tech_stack": ["keyword1", "keyword2"],
  "market_presence": "string",
  "synthesis_note": "string"
}
```

---

## Strategic Alignment Check:
- Does this company align with enterprise automation patterns?
- Are their tech differentiators complementary or competitive?
- What knowledge base value do they represent for our solutions track?

---