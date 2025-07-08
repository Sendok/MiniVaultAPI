# 🧠 MiniVault API

A lightweight local REST API that simulates a core feature of ModelVault: receiving a prompt and returning a generated response — with optional streaming and local LLM integration.

---

## 🚀 Features

- ✅ REST API `POST /generate`
- 🧠 Local model via Hugging Face (`distilgpt2`)
- ⚙️ Streaming response via `/generate/stream`
- 🗃️ Logging prompt/response to `logs/log.jsonl`
- 🧪 Unit tested via `pytest`
- 🖥️ CLI tool via `Typer`

---

## 🛠️ Setup Instructions

### 1. Clone & Install Dependencies

> ⚠️ Make sure you're using **Python 3.10+** or higher

```bash
git clone https://github.com/Sendok/MiniVaultAPI
cd miniVaultAPI
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Run the API

```bash
uvicorn app.main:app --reload
```

API will be available at: [http://localhost:8000](http://localhost:8000)

---

> First run may download `gpt2` model via HuggingFace.

---
## 📦 API Endpoints

### `POST /generate`

**Request:**
```json
{ "prompt": "Hello there!" }
```

**Response:**
```json
{ "response": "Hello there! I am a stubbed AI response..." }
```

---

### `POST /generate/stream`

**Request:**
```json
{ "prompt": "Once upon a time" }
```

**Response:**
Plain-text response streamed **token by token**. please Using CLI to see streamed **token by token**

curl -N -X POST http://localhost:8000/generate/stream -H "Content-Type: application/json" -d '{"prompt": "Once upon a time"}'

---

## 🧪 Run Tests

```bash
pytest -s -v tests/test_main.py
```

---

## 🖥️ CLI Tool

### Generate once:
```bash
python3 cli.py generate "Tell me a joke about AI"
```

### Stream output:
```bash
python3 cli.py stream "Write a short story"
```

---

## 🧠 Design Decisions & Tradeoffs

- **Model Choice:** Chose `distilgpt2` for lightweight performance and fast local inference. Can be swapped with any Hugging Face-compatible model.
- **Streaming:** Simulated token-by-token streaming using `.split()` to demonstrate structure; true token-level streaming would use incremental decoding loop.
- **Modular Code:** Split into `model_handler`, `logger`, and `schemas` for maintainability and clarity.
- **Logging:** File-based logging in JSONL format for easy parsing and audit trail.
- **No Cloud Dependency:** Entirely local per project requirement.

---

## 💡 Future Improvements

- True real-time token streaming
- Switchable models with lazy loading
- SQLite-based structured logging
- Docker containerization

---

## 📂 Project Structure

```
MiniVaultAPI/
├── app/
│   ├── main.py             # FastAPI app
│   ├── logger.py           # Logging util
│   ├── model_handler.py    # LLM logic
│   └── schemas.py          # Pydantic models
├── cli.py                  # CLI tool
├── logs/log.jsonl          # Prompt-response logs
├── tests/test_main.py       # Unit tests
├── requirements.txt
└── README.md
```

---

## 🙌 Thanks!

Built as part of the ModelVault take-home challenge.  
All responses are generated locally. No cloud APIs are used.
