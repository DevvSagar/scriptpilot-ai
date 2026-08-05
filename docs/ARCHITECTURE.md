# 🏗 Architecture

## High-Level Flow

```text
                User
                  │
                  ▼
         React Frontend
                  │
                  ▼
          FastAPI Backend
                  │
      ┌───────────┼───────────┐
      │           │           │
      ▼           ▼           ▼
 PostgreSQL    Gemini AI    File Storage
                  │
                  ▼
          AI Generated Response
```

---

## Backend Responsibilities

- Handle authentication
- Manage uploaded scripts
- Connect with Gemini
- Store chat history
- Provide REST APIs

---

## Frontend Responsibilities

- Upload screenplay
- Chat interface
- Script dashboard

---

## AI Responsibilities

- Summarize scripts
- Answer questions
- Extract entities
- Support future agent workflows