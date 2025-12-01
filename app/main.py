from pathlib import Path
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load replaced chars from: app/replaced_chars.txt
REPLACEMENTS = {}
REPLACED_PATH = Path(__file__).resolve().parent / "replaced_chars.txt"

# Read replacement rules (format: a=4)
if REPLACED_PATH.exists():
    content = REPLACED_PATH.read_text(encoding="utf-8")
    lines = content.splitlines()
    for line in lines:
        if "=" in line:  # avoid empty lines
            key, value = line.strip().split("=")
            REPLACEMENTS[key] = value

def replace_chars(text, replacements):
    result = text
    # Replace each char based on mapping
    for char, repl in replacements.items():
        result = result.replace(char, repl)
        result = result.replace(char.upper(), repl)  # Optional: uppercase support
    return result

@app.post("/replace")
def replace_endpoint():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    replaced = replace_chars(text, REPLACEMENTS)
    return jsonify({"result": replaced})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
