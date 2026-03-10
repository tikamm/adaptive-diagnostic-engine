from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["adaptive_test"]
questions_collection = db["questions"]

questions = [
    {
        "question": "What is 5 + 7?",
        "options": ["10", "11", "12", "13"],
        "correct_answer": "12",
        "difficulty": 0.1,
        "topic": "Arithmetic",
        "tags": ["addition", "basic"]
    },
    {
        "question": "Solve: 2x + 3 = 7",
        "options": ["1", "2", "3", "4"],
        "correct_answer": "2",
        "difficulty": 0.3,
        "topic": "Algebra",
        "tags": ["equations"]
    },
    {
        "question": "What is the square root of 144?",
        "options": ["10", "11", "12", "13"],
        "correct_answer": "12",
        "difficulty": 0.2,
        "topic": "Arithmetic",
        "tags": ["square-root"]
    },
    {
        "question": "If x = 3, what is x^2?",
        "options": ["6", "9", "12", "3"],
        "correct_answer": "9",
        "difficulty": 0.2,
        "topic": "Algebra",
        "tags": ["powers"]
    },
    {
        "question": "What is 15% of 200?",
        "options": ["20", "25", "30", "35"],
        "correct_answer": "30",
        "difficulty": 0.4,
        "topic": "Percentage",
        "tags": ["percent"]
    },
    {
        "question": "Solve: 3x = 18",
        "options": ["3", "6", "9", "12"],
        "correct_answer": "6",
        "difficulty": 0.3,
        "topic": "Algebra",
        "tags": ["equation"]
    },
    {
        "question": "What is 9 * 8?",
        "options": ["72", "64", "81", "69"],
        "correct_answer": "72",
        "difficulty": 0.1,
        "topic": "Arithmetic",
        "tags": ["multiplication"]
    },
    {
        "question": "What is the cube of 3?",
        "options": ["9", "27", "18", "6"],
        "correct_answer": "27",
        "difficulty": 0.4,
        "topic": "Algebra",
        "tags": ["cube"]
    },
    {
        "question": "Solve: x/4 = 5",
        "options": ["10", "15", "20", "25"],
        "correct_answer": "20",
        "difficulty": 0.5,
        "topic": "Algebra",
        "tags": ["division"]
    },
    {
        "question": "What is 100 / 5?",
        "options": ["10", "15", "20", "25"],
        "correct_answer": "20",
        "difficulty": 0.2,
        "topic": "Arithmetic",
        "tags": ["division"]
    }
]

questions_collection.insert_many(questions)

print("Questions inserted successfully!")