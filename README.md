📝 To-Do List Application (CLI + GUI + PRO)

A Python-based To-Do List project implemented in three versions:

- 💻 CLI (Command Line Interface)
- 🖥 GUI (Tkinter Basic)
- 🚀 GUI PRO (Advanced with Status & Categories)

---

📌 Project Description

This project helps users manage daily tasks efficiently.
It allows adding, viewing, deleting, and organizing tasks.

Three versions are included:

- CLI → Simple terminal-based system
- GUI → Interactive interface using Tkinter
- PRO → Advanced version with status tracking, categories, and color coding

All data is stored in a file ("tasks.txt") for persistence using a unified format.

---

⚙️ Features

- Add new tasks
- View all tasks
- Delete tasks
- Persistent storage using file
- GUI interaction (buttons, listbox)
- Status tracking (Pending / Done)
- Category management (Work, Study, Personal)
- Color-coded task display (PRO version)
- Auto-migration of legacy plain-text task files

---

🛠 Technologies Used

- Python 3
- Tkinter (GUI Development)
- File Handling (read/write)
- Lists & Dictionaries

---

📂 Project Structure

todo-list-project/
│
├── todo.py
├── todo_gui.py
├── todo_pro_gui.py
├── task_storage.py
├── tasks.txt
└── README.md

---

▶️ How to Run

🔹 CLI Version

python todo.py

🔹 GUI Version

python todo_gui.py

🔹 PRO Version

python todo_pro_gui.py

---

💾 Unified Storage Format

All three versions share a single `tasks.txt` file using the format:

    title|status|category

Example:

    Study Python|Pending|Study
    Buy Milk|Done|Personal
    Call doctor|Pending|Work

The shared logic lives in `task_storage.py` which provides:
- `load_tasks(path)` — reads tasks and returns a list of dicts.
- `save_tasks(tasks, path)` — writes tasks in the unified format.

🔄 Auto-Migration

If `tasks.txt` was created by an older version of the app (plain text, one task per line),
the app will automatically migrate each legacy line on load:

    Buy milk  →  Buy milk|Pending|Work

The next time any version saves tasks, the file is written in the new unified format.

---

💻 Example

CLI Example

1. Add Task
Enter task: Study Python
Task added successfully!

2. View Tasks
1. Study Python [Pending] (Work)

PRO File Example ("tasks.txt")

Study Python|Pending|Study
Buy Milk|Done|Personal

---

🖥 GUI Overview

🔹 Basic GUI

- Input field for task entry
- Buttons for operations
- Listbox shows: [status] title (category)

🔹 PRO GUI

- Category dropdown
- Status indicator (Pending / Done)
- Color-coded tasks (Red/Green)
- Interactive task management

---

🎯 Learning Purpose

This project helps in learning:

- Python fundamentals
- File handling (persistent storage)
- CLI vs GUI development
- Tkinter basics
- Event-driven programming
- Data structuring using dictionaries
- Modular code design

---

🧠 Approach / Logic

🔹 CLI Version

- Tasks loaded at start via task_storage.load_tasks()
- Written back via task_storage.save_tasks() after each change

🔹 GUI Version

- Same logic + Tkinter interface
- Listbox used for displaying tasks
- Buttons trigger actions

🔹 PRO Version

- Tasks stored as dictionary:

{"title": "Task", "status": "Pending", "category": "Work"}

- File stores structured data using "|"
- Color coding based on status

---

⚠️ Common Mistakes

- ❌ Forgetting to save file after update
- ❌ Not handling empty input
- ❌ Index error while deleting
- ❌ Wrong file format (especially in PRO version)
- ❌ Not stripping newline characters

---

⚡ Complexity

Operation| Time Complexity
Add Task| O(1)
View Tasks| O(n)
Search Task| O(n)
Delete Task| O(n)

---

🚀 Future Improvements

- Add task search functionality
- Filter tasks by category
- Add due date & reminders
- Dark mode UI
- Save data using database (SQLite)
- Mobile app version

---

👨‍💻 Author

Saloni Tiwari
Python & Data Science Student

---

📊 Project Level

🟢 CLI → Beginner
🟡 GUI → Beginner+
🔵 PRO → Intermediate

---

⭐ This project is ideal for beginners progressing towards real-world applications.
