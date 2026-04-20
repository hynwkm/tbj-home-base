# Toronto Blue Jays Homebase Challenge

**Live Demo**: https://tbj-home-base.vercel.app/

A web app built for the Toronto Blue Jays developer exercise.

## Overview

This project displays baseball data.

## Features

- Division standings
- MLB news stories
- Team standings
- Player stat pages
- Leaderboards

## Tech Stack

- Python
- Flask
- Jinja
- Tailwind CSS
- uv

## Prerequisites

- Python 3.10+
- Git
- uv

## Getting Started

### 1. Clone the repo and install dependencies

If you have `uv` installed:

```bash
git clone https://github.com/hynwkm/tbj-home-base.git
cd tbj-home-base
uv sync
```

If you don't have `uv`, create a virtual environment and install dependencies with `pip`:

Windows:

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

macOS/Linux:

```bash
python -m venv .venv
.venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the app

With `uv`:

```bash
uv run python main.py
```

Or with `venv`:

```bash
python main.py
```

Then open:
`http://127.0.0.1:5000`

## Notes

Built as part of the Toronto Blue Jays developer exercise.
