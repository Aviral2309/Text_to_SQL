# AI Text-to-SQL Assistant

An AI-powered web application that converts natural language questions into SQL queries and executes them on a database.
Built using **Flask, LangChain, Google Gemini, and MySQL**, this tool allows users to interact with databases without writing SQL manually.

---

## Overview

This project demonstrates how **Large Language Models (LLMs)** can be integrated with databases to build an intelligent data assistant.

Users simply ask questions in plain English such as:

* "Show all products"
* "What was the budget of Product 12?"
* "List all customers"

The system automatically:

1. Understands the user query
2. Generates the correct SQL statement
3. Executes the query on the database
4. Displays results in a structured table

---

## Features

* Natural Language → SQL generation using **Google Gemini**
* Database schema awareness using **LangChain SQLDatabase**
* Secure query execution using **MySQL**
* Interactive **dashboard-style frontend**
* Real-time query results in table format
* Example queries for quick testing
* AI-powered data assistant interface

---

## Tech Stack

### Backend

* Python
* Flask
* LangChain
* Google Gemini API
* PyMySQL

### Frontend

* HTML
* CSS
* JavaScript

### Database

* MySQL

---

## Project Structure

```
Text_to_SQL/
│
├── app.py
├── .env
│
├── utils/
│   ├── __init__.py
│   └── sql_chain.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/text-to-sql-ai.git
cd text-to-sql-ai
```

### 2. Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory.

```
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## Run the Application

```
python app.py
```

Open the application in your browser

```
http://127.0.0.1:5000
```

---

## Example Queries

Try asking:

```
Show all products
List all customers
What was the budget of Product 12
Find the name and state of all regions
```

---

## How It Works

1. The user asks a question in natural language.
2. LangChain retrieves the database schema.
3. The Gemini LLM generates a SQL query based on the schema.
4. Flask executes the SQL query on MySQL.
5. Results are returned and displayed on the frontend.

---

## Example Workflow

User Query

```
What was the budget of Product 12?
```

Generated SQL

```
SELECT budget FROM products WHERE name='Product 12';
```

Result

```
Budget: 20000
```

---

## Future Improvements

* SQL query validation
* Automatic data visualization (charts)
* Upload CSV datasets and query them
* Query explanation using LLM
* Support for multiple databases
* Conversational chat interface

---

## Use Cases

* AI Data Analyst tools
* Business Intelligence assistants
* Natural language database interfaces
* Data exploration without SQL knowledge

---

## Author

Aviral Mittal

AI & Data Science Enthusiast


