# Natural Language Shell

[![asciicast](https://asciinema.org/a/R4KWar0124OVL4L61JkXALIYD.svg)](https://asciinema.org/a/R4KWar0124OVL4L61JkXALIYD)

Nutzt die OpenAI Autocompletion AI, um natürliche Sprache in Shell-Befehle umzuwandeln.

### Setup

```bash
# create virtual env
python3 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# create .env and set OPENAI token
cp sample.env .env
```

### Usage

```bash
python nls.py
```