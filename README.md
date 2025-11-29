# GenAI Content Studio

GenAI Content Studio is a modular, production-ready FastAPI application that generates **blogs**, **social posts**, and **images** from a single topic prompt.

It demonstrates modern GenAI concepts such as **prompt chaining**, **template-driven generation**, **multi-model orchestration**, and the **OpenAI 1.x Python API**.

---

## 🚀 Features

- Blog and social content generation
- Image generation using gpt-image-1
- Prompt templates (Jinja2)
- Prompt chaining
- Modular architecture (services + pipelines)
- Local output storage
- Docker ready

---

## 🛠️ Setup

### Clone repo
`git clone https://github.com/<your-username>/genai-content-studio.git`

### Install dependencies
`pip install -r requirements.txt`

### Set environment key
`export OPENAI_API_KEY="sk-..."`

---

## ▶️ Run Server

```
uvicorn app.main:app --reload --port 8000
```

Swagger Docs: http://localhost:8000/docs

---

## 🧪 Testing

### Curl
```
curl -X POST http://localhost:8000/api/generate -H "Content-Type: application/json" -d '{"title":"AI in Construction","tone":"friendly","format":"blog","include_images":true}'
```

Outputs saved in:
```
outputs/text/
outputs/images/
```

---

## 📚 Concepts Covered

- Prompt chaining  
- Template-driven prompting  
- Multi-model orchestration  
- Async image generation  
- Clean AI service architecture  
- OpenAI Python SDK v1.x  
- FastAPI best practices  

---

## 🐳 Docker

Build:
`docker build -t genai-studio .`

Run:
```
docker run -p 8000:8000 -e OPENAI_API_KEY=$OPENAI_API_KEY genai-studio
```

---

## 🗂️ Project Structure

See repository structure in main documentation.

---

## 🧩 .gitignore

```
__pycache__/
*.pyc
env/
venv/
.venv/
.DS_Store
.env
outputs/
```

