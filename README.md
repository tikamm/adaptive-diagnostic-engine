# AI-Driven Adaptive Diagnostic Engine

## Overview

This project implements a **1-Dimensional Adaptive Testing System** using FastAPI and MongoDB.
The system dynamically adjusts question difficulty based on the student’s performance.

The goal is to estimate the student's ability level efficiently.

---

## Tech Stack

* Python
* FastAPI
* MongoDB
* PyMongo

---

## Features

* Adaptive question selection
* Ability score tracking
* MongoDB question storage
* Personalized study plan generation

---

## API Endpoints

### Start Session

GET /start-session

Creates a new student test session.

---

### Get Next Question

GET /next-question?session_id=...

Returns the next question based on ability score.

---

### Submit Answer

POST /submit-answer?session_id=...&answer=...

Evaluates the answer and updates the ability score.

---

### Generate Study Plan

GET /study-plan?session_id=...

Returns a personalized study plan based on performance.

---

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the server:

uvicorn app.main:app --reload

Open API documentation:

http://127.0.0.1:8000/docs
