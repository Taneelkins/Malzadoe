# Master-Index.md
This file is the **table of contents and operating manual** for Malzadoe’s Luau Tutor system.  
It defines the authoritative file list, load order, roles, and update workflow.  
Together with `Malzadoe-Spec.md`, this is the source of truth.  
If new files are added, update this index immediately.

> Repo layout: all files live in the repo root (`C:\Users\Tanee\Malzadoe\`) for maximum compatibility.

---

## 0) Session Bootstrap (client → server)
- **Github.md** → Stores the canonical repo URL.  
- **Startup.md** → Defines the startup order.  
> Client side must read `Github.md` first, then `Startup.md`.

---

## 1) Core Directives
- **Malzadoe-Spec.md** → Unified rulebook (persona, teaching rules, safety).  
- **Master-Index.md** → This file (map + procedures).  
- **Teaching-Protocol.md** → Lesson mechanics, answer templates, Socratic flow.  
- **Preferences.md** → Communication and behavior preferences.  

---

## 2) Memory System
- **Memory.md** → Active working memory (short-term).  
- **Memory-Archive.md** → Archive of past notes (long-term).  
- **Variable-Mapping.md** → Maps Master Taru’s project variable names to tutor examples.  

---

## 3) Logging & Governance
- **FixLog.csv** → Troubleshooting ledger. Each row: `YYYY-MM-DD, Action, Result, Next Step`. Always consult before suggesting fixes.  
- **Corrections.md** → Correction policy and archive of past corrections.  

---

## 4) Curriculum & Skills
- **Curriculum-Tracker.md** → Lessons completed, current focus, upcoming steps.  
- **Modules-and-Skills.md** → Skills introduced, modules covered, pending skills.  

---

## 5) Update & Automation (server)
- **.github/workflows/apply-updates.yml** → GitHub Actions workflow. Accepts JSON update payload and commits changes.  
- **scripts/apply_updates.py** → Python script that applies updates from JSON.  

---

## 6) Load Order (session start)
1. `Github.md` → get repo URL.  
2. `Startup.md` → confirm startup order.  
3. `Malzadoe-Spec.md` → apply global rules.  
4. `Master-Index.md` → verify full file map.  
5. `Preferences.md` + `Teaching-Protocol.md` → load specifics.  
6. Memory files (`Variable-Mapping.md`, `Memory.md`, `Memory-Archive.md`).  
7. Governance files (`FixLog.csv`, `Corrections.md`).  
8. Curriculum (`Curriculum-Tracker.md`, `Modules-and-Skills.md`).  

---

## 7) Conflict Resolution
- Priority: **Malzadoe-Spec.md > Teaching-Protocol.md > Preferences.md > others**.  
- Latest explicit instruction from Master Taru always overrides.  

---

## 8) JSON Update Schema
The workflow accepts JSON with the following shape:

```json
{
  "version": 1,
  "ops": [
    {"file":"Preferences.md","op":"replace","content":"<full text>"},
    {"file":"Memory.md","op":"append","section":"Active Notes","content":"2025-08-20 — Practiced conditionals."},
    {"file":"FixLog.csv","op":"csv-append","row":["2025-08-20","Test action","Result","Next step"]}
  ]
}
