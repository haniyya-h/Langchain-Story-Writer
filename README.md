# Langchain-Story-Writer

Generate short stories from a simple prompt using *LangChain* with pluggable LLM backends (OpenAI / Google Gemini). One command in, a structured story out — optionally with outline, character notes, and “continue the story” support.

> Repo contains: story-writer.py, requirements.txt, and an MIT license. ([GitHub][1])

---

## ✨ Features

* *Single-file CLI*: run story-writer.py and get a story.
* *Prompt → Outline → Story* pipeline (outline optional).
* *Provider-agnostic*: works with OpenAI or Google Gemini (set via env).
* *Determinism control*: tweak temperature/seed (if supported by provider).
* *Easy to extend*: swap the model or add tools in one place.

---

## 📦 Requirements

* *Python*: 3.10 or newer recommended
* *Dependencies*: listed in requirements.txt (install with pip)

> License is MIT. ([GitHub][1])

---

## 🔐 Environment Variables

Create a .env in the project root:

bash
# Choose a provider by setting the matching API key.
# You can set one or both; the script will pick the one you configure.

# OpenAI (e.g., GPT-4o-mini or gpt-4.1-mini)
OPENAI_API_KEY=sk-...

# Google Gemini (e.g., gemini-2.5-flash)
GEMINI_API_KEY=...

# Optional model overrides (defaults are reasonable if omitted)
MODEL_NAME=gpt-4o-mini         # or gemini-2.5-flash
TEMPERATURE=0.7                # 0.0–1.0
MAX_TOKENS=1200                # provider dependent


> Tip: If you prefer not to use dotenv, export these in your shell profile.

---

## 🚀 Quickstart

bash
# 1) Clone
git clone https://github.com/haniyya-h/Langchain-Story-Writer
cd Langchain-Story-Writer

# 2) (Recommended) Create & activate a virtual env
python -m venv .venv
# Windows
. .venv/Scripts/activate
# macOS/Linux
source .venv/bin/activate

# 3) Install deps
pip install -r requirements.txt

# 4) Add your keys in .env (see above)

# 5) Run (interactive prompt)
python story-writer.py


---

## 🧑‍💻 Usage

### A) Interactive mode (works even if no CLI args are defined)

Just run the script. You’ll be asked for a brief *prompt* (e.g., “A lost robot finds home in a desert city”) and optional settings. The program then:

1. (Optional) Generates a *story outline*
2. Expands it into a *full story*
3. Prints the result to console and (optionally) saves to a file

### B) CLI flags (if present in the script)

If your story-writer.py exposes argparse flags, typical usage looks like:

bash
python story-writer.py \
  --prompt "A young detective in Karachi solves a metro mystery" \
  --genre "mystery" \
  --words 800 \
  --outline \
  --temperature 0.6 \
  --output out/metro-mystery.md


> If you’re unsure which flags exist, run:
>
> bash
> python story-writer.py --help
> 
> 
>or open the file and check the argparse section at the bottom.

---

## 🧠 How it works (high-level)

1. *Model setup*: The script looks for OPENAI_API_KEY or GEMINI_API_KEY, and picks a default MODEL_NAME accordingly.
2. *Prompting chain*:

   * (Optional) *Outline Chain* – turns your idea into a structured outline (acts like a scaffold).
   * *Story Chain* – expands the idea/outline into a complete short story, honoring genre/tone/length hints.
3. *Post-processing*: Trims overlong output, optionally writes to file.

This separation keeps the story coherent, avoids repetition, and gives you a clean place to insert future tools (e.g., style checkers or “continue the story” calls).

---

## 🗂️ Project structure


Langchain-Story-Writer/
├─ story-writer.py        # main script: model init + outline + story
├─ requirements.txt       # Python deps
└─ LICENSE                # MIT


---

## 🔧 Configuration & Tips

* *Switch provider*: set MODEL_NAME and the matching API key in .env.
* *More/less creativity*: raise/lower TEMPERATURE.
* *Length control*: increase MAX_TOKENS (subject to model limits).
* *Reproducibility*: if the script supports a --seed, set it for repeatable output.
* *Non-English*: prompt in your target language; models handle Urdu, etc., well.

---

## 📚 Examples

bash
# Classic fantasy
python story-writer.py --prompt "An apprentice mage loses her spellbook before exams" --genre fantasy --words 900

# Sci-fi micro-story (concise)
python story-writer.py --prompt "An AI lighthouse guards a stormy digital sea" --words 300 --temperature 0.4

# Noir style
python story-writer.py --prompt "Monsoon night in Karachi; a PI follows a trail of receipts" --genre noir --temperature 0.65


---

## 🧩 Extending

* Add a *Style Chain* that rewrites the draft to a specific author’s vibe (ethically, without imitating living authors too closely).
* Insert a *Content Filter* step (e.g., PG-rating clamp).
* Add a *Continue / Next Chapter* function that feeds the last paragraph back into the chain.

---

## 🧪 Development

* Code style: keep functions small and chain logic explicit (outline → story).
* Testing: store a couple of fixed prompts and compare outputs for gross regressions.
* CI: you can wire a “lint & smoke” GitHub Action later.

---

## ❓ Troubleshooting

* *KeyError: API key*: Set .env properly; restart your shell after exporting.
* *401/403*: Check your model name is available to your key; some tiers restrict models.
* *Weird formatting*: Pipe output to a file and open in a Markdown editor.
* *Very short stories*: increase MAX_TOKENS and/or words flag.

---

## 📝 License

MIT — see LICENSE. ([GitHub][1])

---
