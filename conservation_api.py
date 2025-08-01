from flask import Flask, request, jsonify,render_template_string
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per hour"]  # Adjust as needed
)

# In-memory database to store user efforts
efforts_db = []

@app.route('/submit_effort', methods=['POST'])
@limiter.limit("10 per minute")  # Limit to 10 submissions per minute per IP
def submit_effort():
    data = request.json
    user = data.get('user')
    effort_type = data.get('effort_type')
    description = data.get('description')
    
    if not user or not effort_type or not description:
        return jsonify({'error': 'Missing data'}), 400
    
    effort = {
        'user': user,
        'effort_type': effort_type,
        'description': description
    }
    efforts_db.append(effort)
    return jsonify({'message': 'Effort submitted successfully'}), 200

@app.route('/get_efforts', methods=['GET'])
def get_efforts():
    return jsonify(efforts_db), 200

# ...existing code...

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Conservation Efforts API. Use /submit_effort to submit data and /get_efforts to view efforts.", 200

# ...existing code...

# Simple HTML form for submitting efforts
form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Submit Conservation Effort</title>
</head>
<body>
    <h2>Submit Conservation Effort</h2>
    <form method="post" action="/submit_effort_form">
        <label>User:</label><br>
        <input type="text" name="user" required><br>
        <label>Effort Type:</label><br>
        <input type="text" name="effort_type" required><br>
        <label>Description:</label><br>
        <textarea name="description" required></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
    <br>
    <a href="/view_efforts">View All Efforts</a>
</body>
</html>
"""

@app.route('/submit_effort_form', methods=['GET', 'POST'])
@limiter.limit("10 per minute")  # Limit to 10 submissions per minute per IP
def submit_effort_form():
    if request.method == 'POST':
        user = request.form.get('user')
        effort_type = request.form.get('effort_type')
        description = request.form.get('description')
        if not user or not effort_type or not description:
            return "All fields are required.", 400
        effort = {
            'user': user,
            'effort_type': effort_type,
            'description': description
        }
        efforts_db.append(effort)
        return "Effort submitted successfully! <a href='/submit_effort_form'>Submit another</a> | <a href='/view_efforts'>View Efforts</a>"
    return render_template_string(form_html)

@app.route('/view_efforts')
def view_efforts():
    html = "<h2>All Conservation Efforts</h2><ul>"
    for effort in efforts_db:
        html += f"<li><b>{effort['user']}</b>: {effort['effort_type']} - {effort['description']}</li>"
    html += "</ul><a href='/submit_effort_form'>Submit New Effort</a>"
    return html

if __name__ == '__main__':
    app.run(debug=True)