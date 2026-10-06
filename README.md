# Task List Manager

A simple command-line task manager developed in Python.

## 📋 Features

- Add new tasks
- View task list
- Update task names
- Mark tasks as completed
- Remove completed tasks
- Interactive terminal interface

## 🛠️ Technologies Used

- **Python 3.x** - Primary programming language
- **Python Standard Libraries** - No external dependencies required

## 🏗️ Design Patterns

- **Static Methods** - Implementation of static methods in the `Task` class
- **Modular Structure** - Separation of concerns between `main.py` and `src/task.py`
- **Type Hints** - Explicit typing for improved code readability

## ⚙️ Setup and Configuration

### Prerequisites

- Python 3.8+ installed on the system

### Installation and Execution

1. Clone the repository:

```bash
git clone <repository-url>
cd task-list
```

2. Run the program:

```bash
python main.py
```

## 📝 Usage Example

```
Task Manager Menu

1 - Add Task
2 - View Tasks
3 - Update Task
4 - Complete Task
5 - Delete completed tasks
6 - Exit

Enter the desired option: 1
Enter the task name: Study Python
'Study Python' task added successfully!
```

## 🚧 Next Steps

### Web Interface Implementation with Flask

The project's next objective is to migrate from the command line interface to a modern web application:

#### Planned Technologies

- **Flask** - Web framework for Python
- **HTML/CSS/JavaScript** - Application frontend
- **Bootstrap** - CSS Framework for responsive interface
- **SQLite** - Database for task persistence

#### Planned Web Features

- Intuitive and responsive web interface
- Data persistence in database
- REST API for CRUD operations
- Deploy on hosting platform (Heroku, Vercel, etc.)

#### Future Project Structure

```
task-list-web/
├── app.py # Main Flask application
├── models/
│ └── task_model.py # Task data model
├── routes/
│ └── task_routes.py # REST API routes
├──templates/
│ ├── base.html # Template base
│ └── index.html # Main page
├── static/
│ ├── css/
│ ├── js/
│ └── img/
├── requirements.txt # Project dependencies
└── README.md
```

#### Future Setup Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run Flask application
python app.py

# Access via browser
http://localhost:5000
```
