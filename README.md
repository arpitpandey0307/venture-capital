# Venture Alpha - AI Intelligence Layer

Venture Alpha is an autonomous AI-driven venture capital scouting agent. It is designed to automatically discover, analyze, and evaluate trending software engineering projects and open-source repositories to provide actionable investment insights. 

The system leverages large language models (Google Gemini), advanced web research (Exa), and multi-source data aggregation to perform comprehensive due diligence, generate investment memos, and even simulate founder interviews.

## 🌟 Key Features

- **Automated Data Pipeline:** Aggregates trending signals from GitHub, Product Hunt, Google Trends, and NewsAPI into MongoDB Atlas.
- **Technology Analysis:** Utilizes Gemini AI to analyze raw repository data and abstract key technical components and architectural decisions.
- **Trend Validation:** Evaluates projects against emerging industry trends to provide data-backed trend validation scores.
- **Founder Interview Simulation:** Actively simulates a rigorous VC due-diligence interview with virtual founders to assess technical depth and problem-solving capability.
- **Automated Investment Memos:** Generates complete investment memos calculating a final conviction score, risk breakdowns, and a go-to-market analysis.
- **Comparative Matchups:** Pits two trending open-source projects head-to-head to determine the stronger investment opportunity.

## 🏗️ System Architecture

The project is logically structured into three main layers:

* **`data_collection/` & `data_preprocessing/` (The Data Engine)**  
  Python scripts that periodically fetch, normalize, and save product trends, trending repositories, and news sentiments into a MongoDB database.

* **`LLM/` (The AI Intelligence Backend)**  
  A modern Python FastAPI service orchestrating AI agents and tools. Exposes REST API endpoints (`/full_analysis`, `/generate_memo`, `/demo_projects`, `/compare_projects`) to serve the frontend asynchronously.

* **`frontend/` (The User Interface)**  
  A blazing-fast React frontend built with Vite and Tailwind CSS. It provides a sleek VC dashboard to view scouted projects, interact with real-time data, and trigger comprehensive due diligence reports.

## 🚀 Getting Started

### 1. Start the LLM Intelligence Server
Ensure you have the necessary API keys (`GEMINI_API_KEY`, `MONGO_URI`, `EXA_API_KEY`) populated in the `.env` file within the `LLM` directory.

```bash
cd LLM
# Activate your virtual environment, then run:
pip install -r requirements.txt
python -m uvicorn app:app --reload --port 8000
# The server will run at http://localhost:8000
```

### 2. Start the Frontend Application
```bash
cd frontend/venture-alpha-frontend
npm install
npm run dev
# The frontend will run at http://localhost:5173
```

### 3. (Optional) Run the Data Pipeline
To manually ingest new data into MongoDB from GitHub and Product Hunt:
```bash
cd data_collection/data_collection
python main.py
```

## 🛠️ Built With

- **Backend:** Python, FastAPI, Pydantic
- **AI Integration:** Google Gemini, Exa API
- **Frontend:** React, Vite, Tailwind CSS
- **Database:** MongoDB Atlas
