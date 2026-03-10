# AI-Driven Adaptive Diagnostic Engine

## Overview

This project implements a **1-Dimensional Adaptive Testing Prototype** using **FastAPI and MongoDB**.
The system dynamically adjusts question difficulty based on a student's previous answers to estimate their ability level efficiently.

This prototype demonstrates the core idea behind **adaptive exams like GRE and GMAT**, where question difficulty adapts to the student’s performance.

---

## Tech Stack

* Python
* FastAPI
* MongoDB
* PyMongo

---

## System Architecture

Student → FastAPI Backend → Adaptive Algorithm → MongoDB → Study Plan Generator

1. A student session starts with an **initial ability score of 0.5**.
2. The system selects a question whose difficulty is closest to the ability score.
3. After answering:

   * Correct → ability increases
   * Incorrect → ability decreases
4. The next question adapts based on the updated ability.
5. After answering questions, the system generates a **personalized study plan**.

---

## Database Design

### questions collection

Stores all GRE-style questions.

Fields:

* question
* options
* correct_answer
* difficulty (0.1 – 1.0)
* topic
* tags

### user_sessions collection

Tracks each student's session.

Fields:

* session_id
* ability_score
* current_question
* questions_answered

---

## API Endpoints

### Start Session

```
GET /start-session
```

Creates a new test session.

Response example:

```
{
 "session_id": "abc123",
 "starting_ability": 0.5
}
```

---

### Get Next Question

```
GET /next-question?session_id=<id>
```

Returns the next adaptive question.

---

### Submit Answer

```
POST /submit-answer?session_id=<id>&answer=<answer>
```

Updates the student's ability score.

Example response:

```
{
 "correct": true,
 "new_ability_score": 0.6
}
```

---

### Generate Study Plan

```
GET /study-plan?session_id=<id>
```

Returns a personalized study plan based on the student’s ability.

Example:

```
{
 "ability_score": 0.6,
 "study_plan": [
   "Review algebra fundamentals",
   "Practice GRE equation problems",
   "Attempt medium difficulty quantitative questions"
 ]
}
```

---

## Adaptive Algorithm

The prototype uses a simplified adaptive model:

Initial ability = **0.5**

If answer is correct:

```
ability = ability + 0.1
```

If answer is incorrect:

```
ability = ability - 0.1
```

Ability is always kept between **0.1 and 1.0**.

Questions are selected based on difficulty closest to the ability score.

---

## Running the Project

Install dependencies:

```
pip install -r requirements.txt
```

Start the server:

```
uvicorn app.main:app --reload
```

Open API document
