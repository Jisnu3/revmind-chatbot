# RevMind AI - NovaBite Sales Chatbot

A full-stack conversational sales analytics application built for the RevMind AI Full-Stack Engineer Assignment.

The application allows sales managers to:

* View business KPIs
* Analyze revenue trends
* Ask natural language business questions
* Receive AI-generated answers powered by Google Gemini.

---

## Technology Stack

### Backend

* FastAPI
* SQLite
* Pandas
* Google Gemini API

### Frontend

* React (Vite)
* Axios
* Recharts

### Database

* SQLite

---

## Features

### Dashboard

* Total Net Revenue KPI
* Gross Profit Margin KPI
* Top Region KPI
* Monthly Revenue Trend Chart

### Sales Analytics Chatbot

Supports business questions such as:

* Which region had the highest net revenue in Q1 2024?
* What is the gross profit margin for the Snacks category?
* Which sales rep closed the most units in 2025?
* Compare E-Commerce vs Modern Trade net revenue.
* What was the best performing product in the West region?

---

## Project Structure

```text
revmind-chatbot/
│
├── backend/
│   ├── app/
│   ├── seed.py
│   ├── novabite.db
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── data/
│   └── novabite_sales_data.csv
│
├── README.md
├── .env.example
└── .gitignore
```

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/Jisnu3/revmind-chatbot.git
cd revmind-chatbot
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

### Seed Database

```bash
python seed.py
```

Expected Output:

```text
Loaded 1000 rows into SQLite
```

### Run Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Open a second terminal:

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## API Endpoints

### GET /api/products

Returns product-level revenue and units sold.

### GET /api/summary

Returns:

* Total Net Revenue
* Total Units
* Gross Profit Margin
* Top Region
* Top Channel
* Top Product

### GET /api/trends

Returns monthly revenue trend data.

### POST /api/chat

Request:

```json
{
  "question": "Which region had the highest net revenue in Q1 2024?"
}
```

Response:

```json
{
  "answer": "West region had the highest net revenue..."
}
```

---

## LLM Used

### Google Gemini 2.5 Flash

Why Gemini?

* Free API tier available
* Fast response times
* Suitable for business analytics questions
* Easy FastAPI integration

---

## Prompt Design

The chatbot does not send the full dataset to Gemini.

Workflow:

1. User asks a question.
2. Intent detection identifies the query type.
3. Relevant SQL query is executed.
4. SQLite returns the required business data.
5. Context is generated.
6. Gemini creates a natural-language answer.

Example:

Question:

Which region had the highest net revenue in Q1 2024?

Context:

West = 294046.66

Prompt:

"You are a business analytics assistant. Answer using only supplied data."

This approach minimizes hallucinations and improves accuracy.

---

## Future Improvements

* Authentication and user accounts
* Additional analytics queries
* Streaming chatbot responses
* Unit testing
* Docker deployment
* Retrieval-Augmented Generation (RAG)
* Query caching
* Interactive visualizations

---

## Tradeoffs

* SQLite used instead of PostgreSQL for simplicity.
* Rule-based intent detection implemented before LLM processing.
* Focused on required assignment questions first.
* Limited analytics coverage beyond assignment requirements.

---

## Author

Jisnu Hazra

Submitted for the RevMind AI Full-Stack Engineer Assignment.
