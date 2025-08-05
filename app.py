from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os
from datetime import datetime

# Create Flask application instance
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Sample data storage (in production, use a database)
tasks = [
    {"id": 1, "title": "Learn Flask", "description": "Build a web application with Flask", "completed": False, "created_at": "2025-08-04"},
    {"id": 2, "title": "Create routes", "description": "Set up different URL endpoints", "completed": True, "created_at": "2025-08-03"}
]

# Home route
@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# API route to get all tasks
@app.route('/api/tasks')
def get_tasks():
    return jsonify(tasks)

# Route to add a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    
    if title:
        new_task = {
            "id": len(tasks) + 1,
            "title": title,
            "description": description or "",
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d")
        }
        tasks.append(new_task)
        flash('Task added successfully!', 'success')
    else:
        flash('Task title is required!', 'error')
    
    return redirect(url_for('home'))

# Route to toggle task completion
@app.route('/toggle_task/<int:task_id>')
def toggle_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            flash(f'Task {"completed" if task["completed"] else "reopened"}!', 'success')
            break
    return redirect(url_for('home'))

# Route to delete a task
@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    flash('Task deleted!', 'success')
    return redirect(url_for('home'))

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error_code=404, error_message="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error_code=500, error_message="Internal server error"), 500

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Create static directory if it doesn't exist
    if not os.path.exists('static'):
        os.makedirs('static')
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)