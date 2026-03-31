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

All data is stored in a file ("tasks.txt") for persistence.

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
├── todo_cli.py
├── todo_gui.py
├── todo_pro_gui.py
├── tasks.txt
└── README.md

---

▶️ How to Run

🔹 CLI Version

python todo_cli.py

🔹 GUI Version

python todo_gui.py

🔹 PRO Version

python todo_pro_gui.py

---

💻 Example

CLI Example

1. Add Task
Enter task: Study Python
Task added successfully!

2. View Tasks
1. Study Python

PRO File Example ("tasks.txt")

Study Python|Pending|Study
Buy Milk|Done|Personal

---

🖥 GUI Overview

🔹 Basic GUI

- Input field for task entry
- Buttons for operations
- Listbox to display tasks

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

---

🧠 Approach / Logic

🔹 CLI Version

- Tasks stored in a list
- Read from file at start
- Write to file after changes

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
