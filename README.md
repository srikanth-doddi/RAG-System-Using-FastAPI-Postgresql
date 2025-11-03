# Simple RAG — POC with FastAPI + Postgres (Neon)

```
███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗    ██████╗  █████╗  ██████╗ 
██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝    ██╔══██╗██╔══██╗██╔════╝ 
███████╗██║██╔████╔██║██████╔╝██║     █████╗      ██████╔╝███████║██║  ███╗
╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝      ██╔══██╗██╔══██║██║   ██║
███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗    ██   ██╝██║  ██║╚██████╔╝
╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝    ╚═   ═╝ ╚═╝  ╚═╝ ╚═════╝ 

A tiny, funky README for the Proof-of-Concept using **FastAPI** + **Postgres (Neon)**.
```

---

## ✨ What this is

A compact guide to get the POC running locally (or in a small cloud/dev environment). It includes:

* Python **3.8** (recommended for compatibility)
* A Postgres database (Neon was used for the POC)
* Environment variable configuration via a `.env` file
* Running the app with `uvicorn`

> This README is playful — but the instructions are serious. Keep secrets secret. 🔐

---

## 🧰 Prerequisites

1. **Python 3.8** installed. (You can use `pyenv`, system installer, or your OS package manager.)
2. **pip** available and working.
3. Optional but recommended: **PyCharm** (or any IDE) — set interpreter to Python 3.8.
4. A Postgres instance (Neon or any other Postgres) for the DB.

---

## 🐍 Python / PyCharm setup (quick)

* In PyCharm: `File > Settings > Project: <your-project> > Python Interpreter`
* Click the gear icon → `Add...` → choose a local interpreter and select Python **3.8**.
* Create a virtual environment (recommended) and select it as the project interpreter.

---

## 📦 Install dependencies

Create a virtual environment and install requirements:

```bash
python3.8 -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate     # Windows (PowerShell or cmd)

pip install --upgrade pip
pip install -r requirements.txt
```

> If you don't have a `requirements.txt` yet, create one with the libs you need (e.g. `fastapi`, `uvicorn`, `asyncpg`, `sqlalchemy`, etc.).

---

## 🔁 .env configuration (example)

**Important:** Do **not** commit your real secrets to Git. Use placeholders in the repo and keep real values in your local `.env` or in your CI/CD secret manager.

Create a file named `.env` at the project root with the following template (replace placeholders):

```env
# Postgres database (replace with your own values)
POSTGRES_USERNAME=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=your-db-host.example.com
POSTGRES_PORT=5432
DATABASE_NAME=your_db_name

# OpenAI (replace with your own API key)
OPENAI_API_KEY=sk-REPLACE_WITH_YOUR_KEY
```

**If you accidentally paste real credentials into a public place, rotate them immediately.**

---

## 🗄️ Using Neon (optional)

For the POC I used **Neon** (serverless Postgres hosting). If you want the same:

1. Sign up at [https://console.neon.tech](https://console.neon.tech)
2. Create a project and note the connection string / host credentials
3. Put those values into your local `.env` (again — **never** commit them)

---

## ▶️ Run the app (development)

Typical command to run a FastAPI app using `uvicorn`:

```bash
# run from project root
uvicorn main:app --reload
```

Notes:

* Ensure your `main` module exposes an `app` FastAPI instance: `app = FastAPI()`.
* The `--reload` flag is for development only.

---

## ⚠️ Security & housekeeping

* **Rotate** any credentials you accidentally shared or pasted publicly.
* Add `.env` to `.gitignore`.
* Use environment-specific secrets (do not reuse dev keys in prod).

---

## 🐞 Troubleshooting

* `psycopg2` / `asyncpg` install errors: ensure you have build tools and Python dev headers (`build-essential`, `libpq-dev`, etc.) on Linux, or use wheels on Windows.
* Connection errors: double-check `POSTGRES_HOST`, `POSTGRES_PORT`, `DATABASE_NAME`, and user credentials.
* If `uvicorn main:app` fails, verify the file name `main.py` and that it defines `app = FastAPI()`.

---
![Swagger](Img/swagger.png)

This whole POC has been built on MAC OS

*Made with ✨ and a dash of funk.*
