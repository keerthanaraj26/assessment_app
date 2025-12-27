***Features***

🔐 JWT-based authentication
🔑 Secure password hashing (bcrypt)
⚡ Async MongoDB integration (Motor)
📘 Auto-generated Swagger documentation
🧩 Modular and scalable folder structure
🚫 No schema enforcement (flexible documents)


***Project Structure***

backend/
│
├── main.py                  # FastAPI app entry point
├── database.py              # MongoDB connection
│
├── routes/
│   └── auth_routes.py       # Authentication APIs
│
├── services/
│   └── auth_service.py      # Business logic
│
├── utils/
│   ├── jwt.py               # JWT handling
│   └── security.py          # Password hashing
│
└── requirements.txt


***Prerequisites***

Python 3.10 or above
MongoDB Community Server
MongoDB Compass (optional)

Check Python in terminal: 
        python --version


***Installation & Setup***

1️⃣ Clone the Repository
    git clone "https://github.com/keerthanaraj26/assessment_app.git"

2️⃣ Create Virtual Environment
    python -m venv venv

Activate:

# Windows
    venv\Scripts\activate

3️⃣ Install Dependencies
    python -m pip install fastapi uvicorn motor passlib[bcrypt] python-jose

▶️ Running the Server
    python -m uvicorn main:app --reload


***Server URL***

http://127.0.0.1:8000


***Swagger UI***

http://127.0.0.1:8000/docs


***MongoDB Configuration***

Host - localhost
Port - 27017
Database - assessment
Collection - user

***API***

POST 
    /api/auth/login

Request

{
  "email": "admin@test.com",
  "password": "Test@123"
}