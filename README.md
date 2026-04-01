# 📝 To‑Do List Application (CLI + GUI + PRO)

A beginner‑friendly Python To‑Do List project with **three versions**:

- **💻 CLI** (Command Line Interface)
- **🖥 Basic GUI** (Tkinter)
- **🚀 PRO GUI** (Tkinter + Status + Category)

All versions share the **same `tasks.txt` file** for persistence.

---

## 📌 Project Description

This project helps you manage daily tasks efficiently. You can:

- Add tasks
- View tasks
- Delete tasks
- (PRO) Mark tasks as Done + categorize tasks

---

## ⚙️ Features

- ✅ Add / View / Delete tasks
- ✅ Persistent storage using `tasks.txt`
- ✅ GUI interaction (buttons, listbox)
- ✅ Status tracking (**Pending / Done**) *(PRO + shared format)*
- ✅ Categories (**Work / Study / Personal**) *(PRO + shared format)*
- ✅ Color‑coded tasks *(PRO)*
- ✅ **Auto‑migration** from old plain‑text task files

---

## 🛠 Technologies Used

- **Python 3**
- **Tkinter** (GUI)
- **File Handling** (read/write)
- **Lists & Dictionaries**
- *(No external dependencies for the app itself)*

---

## 📂 Project Structure

```text
python-todo-cli/
├── todo.py            # CLI app
├── todo_gui.py        # Basic Tkinter GUI
├── todo_pro_gui.py    # PRO Tkinter GUI (status + categories)
├── task_storage.py    # Shared load/save + migration logic
├── tasks.txt          # Shared data file (auto-created/updated)
└── README.md
```

---

## ▶️ How to Run

### 🔹 CLI Version
```bash
python todo.py
```

### 🔹 Basic GUI Version
```bash
python todo_gui.py
```

### 🔹 PRO GUI Version
```bash
python todo_pro_gui.py
```

---

## 💾 Unified Storage Format (`tasks.txt`)

All three versions use a single storage format:

```text
title|status|category
```

### Example `tasks.txt`
```text
Study Python|Pending|Study
Buy Milk|Done|Personal
Call doctor|Pending|Work
```

The shared file logic is implemented in **`task_storage.py`**:

- `load_tasks(path="tasks.txt")` — reads tasks and returns a list of dicts
- `save_tasks(tasks, path="tasks.txt")` — writes tasks in the unified format

A task dictionary looks like:
```python
{"title": "Task", "status": "Pending", "category": "Work"}
```

---

## 🔄 Auto‑Migration (Backward Compatibility)

If your `tasks.txt` was created by an older version of the app (plain text, one task per line), it will be automatically migrated **on load**.

Legacy line:
```text
Buy milk
```

Migrated representation:
```text
Buy milk|Pending|Work
```

✅ The file is fully normalized into the new format **the next time any version saves tasks**.

---

## 💻 Example Output (CLI)

### Add a task
```text
Enter new task: Study Python
Task added successfully!
```

### View tasks
```text
Your Tasks:
1. Study Python [Pending] (Work)
```

---

## 🖥 GUI Overview

### 🔹 Basic GUI
- Input field for task title
- Buttons for add/delete
- List display format:
  - `[status] title (category)`

### 🔹 PRO GUI
- Category dropdown
- Mark task as Done
- Color coding based on status:
  - Pending → Red
  - Done → Green

---

## 🧠 How It Works (High Level)

- All apps load tasks with `task_storage.load_tasks()`
- After any change, they write back with `task_storage.save_tasks()`
- This keeps **CLI / GUI / PRO** fully compatible with one shared `tasks.txt`

---

## ⚠️ Common Mistakes

- Forgetting to save after updating tasks *(handled automatically in current code)*
- Entering an empty task title
- Selecting nothing before deleting in GUI
- Using an incorrect file format in `tasks.txt`

---

## ⚡ Complexity (Big‑O)

| Operation    | Time Complexity |
|-------------|------------------|
| Add Task    | O(1)             |
| View Tasks  | O(n)             |
| Delete Task | O(n)             |

---

## 🚀 Future Improvements (Optional Ideas)

- Search tasks
- Filter by category/status
- Due dates & reminders
- Dark mode UI
- Store tasks in SQLite instead of a text file

---

## 👨‍💻 Author

Saloni Tiwari  
Python & Data Science Student
