# 📖 LangChain Story Writer

Turn a simple idea into a complete short story with *LangChain* and your choice of LLM backend (OpenAI or Google Gemini).
One prompt in → an outline, character notes, and a polished story out — with optional “continue the story” support.

---

## ✨ Features

* **Single-file CLI**: run `story-writer.py` and get a story instantly.
* **Prompt → Outline → Story** pipeline (outline optional).
* **Backend agnostic**: works with OpenAI or Google Gemini (set via env).
* **Customizable output**: control temperature, seed, length, and genre.
* **Extensible**: swap models or add new tools in one place.

---

## 📦 Requirements

* **Python**: 3.10+
* **Dependencies**: see `requirements.txt`

Install with:

```bash
pip install -r requirements.txt
```

License: MIT

---

## 🔐 Setup Environment Variables

Create a `.env` file in the project root:

```bash
# Choose a provider (OpenAI or Gemini)

# OpenAI (e.g., gpt-4o-mini or gpt-4.1-mini)
OPENAI_API_KEY=sk-...

# Google Gemini (e.g., gemini-2.5-flash)
GEMINI_API_KEY=...

# Optional overrides
MODEL_NAME=gpt-4o-mini       # or gemini-2.5-flash
TEMPERATURE=0.7              # 0.0–1.0
MAX_TOKENS=1200              # depends on provider
```

> 💡 Tip: You can also export these in your shell instead of using `.env`.

---

## 🚀 Quickstart

```bash
# 1) Clone
git clone https://github.com/haniyya-h/Langchain-Story-Writer
cd Langchain-Story-Writer

# 2) (Optional) Virtual environment
python -m venv .venv
# Windows
. .venv/Scripts/activate
# macOS/Linux
source .venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Add your API key(s) in .env

# 5) Run
python story-writer.py
```

---

## 🧑‍💻 Usage

### Interactive Mode

Run the script without arguments:

```bash
python story-writer.py
```

* Enter a short prompt (e.g., *“A lost robot finds home in a desert city”*)
* Optionally generate an **outline**
* Expand into a **full story**
* View in console or save to a file

---

### CLI Flags (if enabled in script)

```bash
python story-writer.py \
  --prompt "A young detective in Karachi solves a metro mystery" \
  --genre "mystery" \
  --words 800 \
  --outline \
  --temperature 0.6 \
  --output out/metro-mystery.md
```

Check available flags with:

```bash
python story-writer.py --help
```

---

## 🧠 How It Works

1. **Model setup** → selects OpenAI or Gemini based on your API key.
2. **Prompting chain**:

   * *(Optional)* Outline chain → turns your idea into a scaffold.
   * Story chain → expands into a full short story with genre, tone, and length.
3. **Post-processing** → trims extra output and saves (if requested).

---

## 🗂️ Project Structure

```
Langchain-Story-Writer/
├─ story-writer.py      # Main script
├─ requirements.txt     # Dependencies
└─ LICENSE              # MIT license
```

---

## 🔧 Configuration Tips

* **Switch provider**: set `MODEL_NAME` + API key in `.env`.
* **Control creativity**: raise/lower `TEMPERATURE`.
* **Control length**: adjust `MAX_TOKENS` and/or `--words`.
* **Reproducibility**: set a seed (if supported).
* **Multi-language**: works in English, Urdu, and others.

---

## 📚 Examples

```bash
# Fantasy
python story-writer.py --prompt "An apprentice mage loses her spellbook" --genre fantasy --words 900

# Sci-fi short
python story-writer.py --prompt "An AI lighthouse guards a stormy digital sea" --words 300 --temperature 0.4

# Noir style
python story-writer.py --prompt "Monsoon night in Karachi; a PI follows a trail of receipts" --genre noir
```

---

## 🧩 Extending

* Add a **Style Chain** to mimic specific writing tones.
* Insert a **Content Filter** (e.g., PG-safe mode).
* Add a **Continue Story / Next Chapter** loop.

---

## 🧪 Development Notes

* Keep functions small; keep chain logic explicit (outline → story).
* Use test prompts for quick regression checks.
* CI can run linting + smoke tests.

---

## ❓ Troubleshooting

* **`KeyError: API key`** → check `.env` or shell exports.
* **401/403 errors** → model not available for your tier.
* **Weird formatting** → pipe to file and open in Markdown editor.
* **Stories too short** → raise `MAX_TOKENS` or `--words`.


## 📝 License

MIT — see LICENSE.

---
