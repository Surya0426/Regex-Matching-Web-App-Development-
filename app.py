from flask import Flask, render_template, request

import re 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']

    matches = re.findall(regex_pattern, test_string, re.IGNORECASE)
    
    num_matches = len(matches)
    matched_words = matches

    return render_template('matches.html',test_string=test_string, regex_pattern=regex_pattern, num_matches=num_matches, matched_words=matches)

@app.route('/validate-email', methods=['POST'])
def validate_email():
    email = request.form['email']
    regex_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    is_valid_email = re.match(regex_pattern, email) is not None

    return render_template('validate_email.html', email=email, is_valid_email=is_valid_email)

# to run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)