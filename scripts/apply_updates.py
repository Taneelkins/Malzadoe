# C:\Users\Tanee\my-bot-files\scripts\apply_updates.py
import json, sys, os, csv

def ensure_parent(path):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)

def op_replace(path, content):
    ensure_parent(path)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(content if content.endswith("\n") else content + "\n")

def op_append(path, content, section=None):
    ensure_parent(path)
    base = ""
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            base = f.read()
    if not section:
        joined = base + ("" if base.endswith("\n") else "\n") + content + "\n"
        with open(path, "w", encoding="utf-8") as f:
            f.write(joined)
        return
    # append under a markdown heading containing `section` (case-insensitive)
    lines = base.splitlines(True)
    start = None
    for i, line in enumerate(lines):
        if line.lstrip().startswith("#") and section.lower() in line.lower():
            start = i; break
    if start is None:
        joined = base + ("" if base.endswith("\n") else "\n") + f"\n## {section}\n{content}\n"
        with open(path, "w", encoding="utf-8") as f:
            f.write(joined)
        return
    end = len(lines)
    for j in range(start+1, len(lines)):
        if lines[j].lstrip().startswith("#"):
            end = j; break
    section_text = "".join(lines[:end])
    if not section_text.endswith("\n"):
        section_text += "\n"
    section_text += content + "\n"
    remainder = "".join(lines[end:])
    with open(path, "w", encoding="utf-8") as f:
        f.write(section_text + remainder)

def op_csv_append(path, row):
    ensure_parent(path)
    with open(path, "a", encoding="utf-8", newline="") as f:
        csv.writer(f).writerow(row)

def main():
    if len(sys.argv) < 2:
        print("usage: apply_updates.py updates.json"); sys.exit(2)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = json.load(f)
    ops = data.get("ops", [])
    for op in ops:
        file = op["file"]; kind = op["op"]
        if kind == "replace":
            op_replace(file, op.get("content", ""))
        elif kind == "append":
            op_append(file, op.get("content",""), op.get("section"))
        elif kind == "csv-append":
            op_csv_append(file, op.get("row", []))
        else:
            raise SystemExit(f"Unknown op: {kind}")
    print(f"Applied {len(ops)} ops.")

if __name__ == "__main__":
    main()
