# PromptVault - Personal Prompt Library

A full-stack personal productivity web application built with Python and Streamlit.
PromptVault helps you save, organize, search, and reuse your best AI prompts - all in one place.

---

## Features

- Add Prompts - Save prompts with title, category, difficulty, tags, and full prompt framework
- View Library - Browse all your saved prompts in a clean, organized list
- Search and Filter - Find any prompt instantly by keyword, category, or difficulty
- Edit Prompts - Update and improve your prompts anytime
- Delete Prompts - Remove prompts you no longer need
- Favorites - Star your most-used prompts for quick access
- Dashboard - See statistics about your prompt collection at a glance
- Analytics - View charts showing prompts by category and difficulty

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11+ | Main programming language |
| Streamlit 1.40 | Web application framework |
| SQLite | Database |
| SQLAlchemy | Database ORM |
| Pandas | Data analysis and charts |

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/PromptVault.git
cd PromptVault
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Load sample prompts
```bash
python seed.py
```

### 5. Run the application
```bash
streamlit run app.py
```

Open your browser at http://localhost:8501

---

## Project Structure

PromptVault/
|-- app.py Main application entry point
|-- seed.py Sample data loader (15 prompts)
|-- requirements.txt Python dependencies
|
|-- database/
| |-- db.py Database connection and setup
| |-- models.py Database table structure
|
|-- views/
| |-- dashboard.py Dashboard page
| |-- add_prompt.py Add Prompt page
| |-- view_prompts.py View and manage prompts
| |-- analytics.py Analytics and charts
|
|-- utils/
| |-- helpers.py CRUD operations
| |-- search.py Search and filter logic
|
|-- assets/ logo file

---

## How to Use

1. Run the app using the steps above
2. Click Add Prompt in the sidebar to save your first prompt
3. Use View Prompts to browse, search, edit, and delete prompts
4. Click the Favorite button to star your best prompts
5. Check the Dashboard and Analytics for stats and charts

---

## Author

Annaladasu Meghana

---

## License

MIT License - free to use and modify
