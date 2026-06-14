# RevMind AI - NovaBite Sales Chatbot

A full-stack conversational sales analytics application built for the RevMind AI Full-Stack Engineer Assignment.

The application allows sales managers to:
- View business KPIs
- Analyze revenue trends
- Ask natural language business questions
- Receive AI-generated answers powered by Gemini

# RevMind AI - NovaBite Sales Chatbot

A full-stack conversational sales analytics application built for the RevMind AI Full-Stack Engineer Assignment.

The application allows sales managers to:
- View business KPIs
- Analyze revenue trends
- Ask natural language business questions
- Receive AI-generated answers powered by Gemini

## Technology Stack

### Backend
- FastAPI
- SQLite
- Pandas
- Google Gemini API

### Frontend
- React (Vite)
- Axios
- Recharts

### Database
- SQLite

## Features

### Dashboard
- Total Net Revenue KPI
- Gross Profit Margin KPI
- Top Region KPI
- Monthly Revenue Trend Chart

### Sales Analytics Chatbot
Supports business questions such as:

- Which region had the highest net revenue in Q1 2024?
- What is the gross profit margin for the Snacks category?
- Which sales rep closed the most units in 2025?
- Compare E-Commerce vs Modern Trade net revenue.
- What was the best performing product in the West region?

## Project Structure

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

# Setup Instructions

## Clone Repository

git clone https://github.com/Jisnu3/revmind-chatbot.git

cd revmind-chatbot

## Backend Setup

Navigate to backend folder:

cd backend

Create virtual environment:

python -m venv venv

Activate environment:

### Windows

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Seed Database

Load CSV data into SQLite:

python seed.py

Expected output:

Loaded 1000 rows into SQLite

## Run Backend

uvicorn app.main:app --reload

## Frontend Setup

Open a second terminal.

Navigate to frontend:

cd frontend

Install packages:

npm install

Run application:

npm run dev

## API Endpoints

### GET /api/products

Returns product-level revenue and units sold.

### GET /api/summary

Returns:

- Total Net Revenue
- Total Units
- Gross Profit Margin
- Top Region
- Top Channel
- Top Product

### GET /api/trends

Returns monthly revenue trend data.

### POST /api/chat

Accepts:

{
  "question": "Which region had the highest net revenue in Q1 2024?"
}

Returns:

{
  "answer": "West region had the highest net revenue..."
}

## LLM Used

Google Gemini 2.5 Flash

### Why Gemini?

- Free API tier available
- Fast response time
- Suitable for business analytics questions
- Easy integration with FastAPI

## LLM Used

Google Gemini 2.5 Flash

### Why Gemini?

- Free API tier available
- Fast response time
- Suitable for business analytics questions
- Easy integration with FastAPI