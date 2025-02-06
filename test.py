from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to store user efforts
efforts_db = []

@app.route('/submit_effort', methods=['POST'])
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

if __name__ == '__main__':
    app.run(debug=True)