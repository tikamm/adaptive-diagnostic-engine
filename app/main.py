from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
import uuid

app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["adaptive_test"]

questions_collection = db["questions"]
sessions_collection = db["user_sessions"]


@app.get("/")
def home():
    return {"message": "Adaptive Diagnostic Engine Running"}


# Start a new test session
@app.get("/start-session")
def start_session():

    session_id = str(uuid.uuid4())

    session = {
        "session_id": session_id,
        "ability_score": 0.5,
        "questions_answered": [],
        "current_question": None
    }

    sessions_collection.insert_one(session)

    return {
        "message": "Session started",
        "session_id": session_id,
        "starting_ability": 0.5
    }


# Get next adaptive question
@app.get("/next-question")
def get_next_question(session_id: str):

    session = sessions_collection.find_one({"session_id": session_id})

    if not session:
        return {"error": "Session not found"}

    ability = session["ability_score"]

    # find question closest to ability
    question = questions_collection.find_one(
        {"difficulty": {"$gte": ability}},
        sort=[("difficulty", 1)]
    )

    if not question:
        question = questions_collection.find_one(
            sort=[("difficulty", -1)]
        )

    # save question id in session
    sessions_collection.update_one(
        {"session_id": session_id},
        {"$set": {"current_question": question["_id"]}}
    )

    # convert ObjectId to string for API response
    question["_id"] = str(question["_id"])

    return question


# Submit answer and update ability
@app.post("/submit-answer")
def submit_answer(session_id: str, answer: str):

    session = sessions_collection.find_one({"session_id": session_id})

    if not session:
        return {"error": "Session not found"}

    question_id = session["current_question"]

    if not question_id:
        return {"error": "No active question"}

    question = questions_collection.find_one(
        {"_id": ObjectId(str(question_id))}
    )

    if not question:
        return {"error": "Question not found"}

    correct = answer == question["correct_answer"]

    ability = session["ability_score"]

    # adaptive update
    if correct:
        ability += 0.1
    else:
        ability -= 0.1

    ability = max(0.1, min(1.0, ability))

    sessions_collection.update_one(
        {"session_id": session_id},
        {"$set": {"ability_score": ability}}
    )

    return {
        "correct": correct,
        "new_ability_score": ability
    }
@app.get("/study-plan")
def generate_study_plan(session_id: str):

    session = sessions_collection.find_one({"session_id": session_id})

    if not session:
        return {"error": "Session not found"}

    ability = session["ability_score"]

    if ability < 0.4:
        plan = [
            "Review basic arithmetic and algebra concepts.",
            "Practice solving simple equations daily.",
            "Focus on understanding problem statements carefully."
        ]
    elif ability < 0.7:
        plan = [
            "Practice medium-level GRE algebra questions.",
            "Improve speed and accuracy with timed exercises.",
            "Review mistakes and focus on weak topics."
        ]
    else:
        plan = [
            "Attempt advanced GRE quantitative problems.",
            "Practice mixed topic problem sets.",
            "Focus on improving speed under timed conditions."
        ]

    return {
        "ability_score": ability,
        "study_plan": plan
    }