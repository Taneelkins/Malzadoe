# Malzadoe – Luau Tutor System

Malzadoe is a structured memory and automation system designed to teach and assist Master Taru with Luau programming.  
This repository contains all persistent rules, preferences, memory, and automation scripts that keep Malzadoe consistent across sessions.

---

## 📂 Repo Structure

- **Malzadoe-Spec.md** → The master rulebook (persona, honorifics, teaching rules, safety).
- **Master-Index.md** → The map of all files, their roles, and load order.
- **Preferences.md** → Communication and style preferences.
- **Teaching-Protocol.md** → Lesson mechanics, answer templates, Socratic flow.
- **Corrections.md** → Correction policy + archive of past corrections.
- **FixLog.csv** → Troubleshooting ledger (never repeat failed fixes).
- **Memory.md** → Active working memory.
- **Memory-Archive.md** → Long-term memory archive.
- **Curriculum-Tracker.md** → Tracks lessons completed, current focus, next steps.
- **Modules-and-Skills.md** → Skills/modules taught and pending.
- **Variable-Mapping.md** → Maps project-specific variable names.
- **Github.md** → Stores the canonical repo URL.
- **Startup.md** → Session bootstrap instructions.
- **.github/workflows/apply-updates.yml** → GitHub Actions workflow for applying updates.
- **scripts/apply_updates.py** → Python script that applies updates from JSON.

---

## ⚙️ Workflow Overview

1. **Start of session**  
   - ChatGPT reads `Github.md` → then `Startup.md`.  
   - Loads `Malzadoe-Spec.md`, `Master-Index.md`, and all category files.  
   - Greets Master Taru once fully loaded.

2. **During session**  
   - Malzadoe follows rules from the Spec + Index.  
   - Logs new notes, fixes, and corrections into the proper files.

3. **End of session**  
   - Malzadoe generates a JSON payload of updates.  
   - Master Taru runs the **Apply Tutor Updates** workflow on GitHub and pastes the JSON.  
   - Workflow commits the changes to this repo.

4. **Next session**  
   - Malzadoe reloads everything fresh from this repo.

---

## 🔑 JSON Update Operations

The GitHub Action accepts JSON payloads with `ops` (operations).  
Each operation has a `file`, an `op`, and either `content` or `row`.

### Supported Ops
- **replace** → overwrite entire file  
  ```json
  {"file":"Preferences.md","op":"replace","content":"<full file content>"}
  ```

- **append** → add text at the end or under a section heading  
  ```json
  {"file":"Memory.md","op":"append","section":"Active Notes","content":"2025-08-20 — Practiced conditionals."}
  ```

- **csv-append** → add a row to a CSV log  
  ```json
  {"file":"FixLog.csv","op":"csv-append","row":["2025-08-20","Restart LSP","Failed","Tried Nightly build"]}
  ```

---

## 📝 Example Save JSON

Append a memory note and log a FixLog row:
```json
{"ops":[
  {"file":"Memory.md","op":"append","section":"Active Notes","content":"2025-08-20 — Learned conditionals."},
  {"file":"FixLog.csv","op":"csv-append","row":["2025-08-20","Test save","✅ Worked","None"]}
]}
```

Replace Preferences.md entirely:
```json
{"ops":[
  {"file":"Preferences.md","op":"replace","content":"# Preferences.md\n- Keep answers minimal\n- Use honorifics naturally"}
]}
```

---

## 🖥️ Manual Git Commands (optional)

If you want to bypass the Action and push manually:

```powershell
cd "C:\Users\Tanee\Malzadoe"
git add .
git commit -m "manual update"
git push
```

Check repo status:
```powershell
git status
```

Pull latest changes:
```powershell
git pull --rebase origin main
```

---

## ✅ Routine Checklist

- **Start** → Malzadoe auto-loads from this repo.  
- **During** → Malzadoe tracks notes, fixes, preferences.  
- **End** → Generate JSON → run **Apply Tutor Updates** → paste JSON.  
- **Next Session** → Repo reloads automatically, always fresh.  

---

_End of README._

---

## 🆕 Adding Rules and Notes During Chat

To make Malzadoe automatically generate JSON updates, use simple tags while you chat.  
At the end of a session, ask **“SAVE JSON”** and Malzadoe will produce the correct payload.

### Tags

- `+mem:` note → goes to **Memory.md** (under “Active Notes”)
- `+fix:` action | result | next → new row in **FixLog.csv**
- `+pref:` rule → bullet in **Preferences.md**
- `+corr:` corrected text/code → entry in **Corrections.md**
- `+map:` Key => Value → added to **Variable-Mapping.md**
- `+lesson:` item → logged in **Curriculum-Tracker.md**

### Example usage

```
+mem: Add debounce to input handler.
+fix: Restart LSP | Worked | None
+pref: Keep examples under 20 lines.
+map: PlayerService => Players
+lesson: Covered tables vs dictionaries.
```

At the end of the chat, say **SAVE JSON**.  
Malzadoe will generate a JSON like:

```json
{"ops":[
  {"file":"Memory.md","op":"append","section":"Active Notes","content":"- Add debounce to input handler."},
  {"file":"FixLog.csv","op":"csv-append","row":["2025-08-20","Restart LSP","Worked","None"]},
  {"file":"Preferences.md","op":"append","section":"Active Preferences","content":"- Keep examples under 20 lines."},
  {"file":"Variable-Mapping.md","op":"append","section":"Active Mappings","content":"PlayerService → Players"},
  {"file":"Curriculum-Tracker.md","op":"append","section":"Completed Lessons","content":"- Covered tables vs dictionaries."}
]}
```
