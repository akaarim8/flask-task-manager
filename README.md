# Flask Task Manager

A simple web-based task management application built with Flask.

## Directory Structure

```
flask-task-manager/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template with common elements
│   ├── index.html        # Home page template
│   ├── about.html        # About page template
│   └── error.html        # Error page template
└── static/               # Static files (CSS, JS, images)
    └── style.css         # Main stylesheet
```

## Features

- ✅ Add new tasks with titles and descriptions
- ✅ Mark tasks as completed or reopen them
- ✅ Delete tasks you no longer need
- ✅ View all tasks with their creation dates
- ✅ RESTful API endpoint for task data
- ✅ Responsive design for mobile and desktop
- ✅ Flash messages for user feedback
- ✅ Error handling with custom error pages

## Installation & Setup

1. **Create project directory:**
   ```bash
   mkdir flask-task-manager
   cd flask-task-manager
   ```

2. **Create virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create directory structure:**
   ```bash
   mkdir templates static
   ```

5. **Save the files:**
   - Save `app.py` in the root directory
   - Save HTML templates in the `templates/` folder
   - Save `style.css` in the `static/` folder

## Running the Application

1. **Start the Flask development server:**
   ```bash
   python app.py
   ```

2. **Open your web browser and visit:**
   ```
   http://localhost:5000
   ```

## Available Routes

- `/` - Home page with task management interface
- `/about` - About page with app information
- `/api/tasks` - JSON API endpoint returning all tasks
- `/add_task` - POST endpoint for adding new tasks
- `/toggle_task/<id>` - Toggle task completion status
- `/delete_task/<id>` - Delete a specific task

## API Usage

Get all tasks as JSON:
```bash
curl http://localhost:5000/api/tasks
```

## Customization

### Changing the Secret Key
Edit `app.py` and replace `'your-secret-key-here'` with a secure random string:
```python
app.secret_key = 'your-secure-secret-key'
```

### Adding Database Support
Currently, tasks are stored in memory. For production use, consider integrating with:
- SQLite (simple file-based database)
- PostgreSQL (robust relational database)
- MongoDB (document database)

### Styling
Modify `static/style.css` to customize the appearance of your application.

## Development Notes

- The application runs in debug mode by default
- Tasks are stored in memory and will be lost when the server restarts
- Flash messages provide user feedback for all actions
- The app includes basic error handling for 404 and 500 errors

## Production Deployment

For production deployment:
1. Set `debug=False` in `app.py`
2. Use a production WSGI server like Gunicorn
3. Implement a proper database
4. Add user authentication and authorization
5. Use environment variables for configuration

## License

This project is open source and available under the MIT License.