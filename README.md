
```markdown
# 🎬 Video Task Processing API with FastAPI

A lightweight, modular, and scalable REST API built with **FastAPI**, **SQLAlchemy**, and **SQLite**. This service allows users to upload videos and perform asynchronous tasks like **audio extraction**, **thumbnail generation**, and **video compression**.

---

## 📦 Features

- ✅ Upload video files via API  
- ⚙️ Background task processing  
- ⏱ Task queue using FastAPI BackgroundTasks  
- 📄 SQLite-based task tracking  
- 🧩 Modular architecture with SQLAlchemy ORM  
- 🔄 Auto DB migration (on first run)  
- 🔍 View all tasks or specific task by ID  

---

## 🚀 Tech Stack

- **FastAPI** for API framework  
- **SQLAlchemy** for ORM  
- **SQLite** for persistent storage  
- **Pydantic** for data validation  
- **BackgroundTasks** for async task handling  

---

## 📂 Project Structure

```plaintext
project/
├── main.py           # FastAPI app with routes and logic
├── database.py       # SQLAlchemy engine and session
├── models.py         # SQLAlchemy ORM models
├── schemas.py        # Pydantic schemas for request/response
├── tasks.py          # Background task processor
├── upload/           # Directory for uploaded videos
├── data.db           # SQLite database (auto-created)
└── requirements.txt  # Python dependencies
```

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/arpit910/Assignment-Web-Cue-
cd video-task-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI server

```bash
uvicorn main:app --reload
```

Server will be running at:  
📡 `http://127.0.0.1:8000`

---

## 🔍 API Endpoints

### `POST /tasks/`  
**Description:** Upload a video and create a task  
**Consumes:** `multipart/form-data`  

**Form Data:**
- `file`: UploadFile (video)
- `task_type`: `extract_audio`, `thumbnail`, or `compress`

**Response:** Task object

---

### `GET /tasks`  
**Description:** Retrieve all tasks  

---

### `GET /tasks/{id}`  
**Description:** Get a specific task by ID  

---

## 🧪 Example Task Flow

1. Upload a file with `task_type="extract_audio"`  
2. API stores the file in `/upload`  
3. A background task starts processing  
4. Task status transitions: `pending → processing → completed`  
5. Result is returned as filename suffix (e.g., `_audio.mp3`)  

---

## 📌 Notes

- All files are stored in the `upload/` directory.  
- This project is for prototyping/demo only. For production use:
  - Replace SQLite with PostgreSQL
  - Add authentication
  - Use task queues like Celery + Redis for heavy jobs

---

## 📄 License

MIT License
```

---

Now, this is a ready-to-use `README.md` for your project. Let me know if you need further changes!
