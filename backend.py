# vulnerable_example.py

from flask import Flask, request, render_template_string, make_response

app = Flask(__name__)

# Unsanitized User Input
@app.route('/unsanitized')
def unsanitized_input():
    user_input = request.args['input']  # Vulnerability: Unsanitized User Input
    return f"User input is: {user_input}"

# Direct Output of User Input
@app.route('/direct_output')
def direct_output():
    user_input = request.args['input']  # Vulnerability: Direct Output of User Input
    return render_template_string(f"{{{{ {user_input} }}}}")

# Use of Unsafe Functions
@app.route('/unsafe_eval')
def unsafe_eval():
    user_code = request.args['code']  # Vulnerability: Use of Unsafe Functions
    eval(user_code)  # Dangerous: Arbitrary code execution

# Missing Output Encoding
@app.route('/missing_encoding')
def missing_encoding():
    user_input = request.args['input']  # Vulnerability: Missing Output Encoding
    return make_response(f"<html><body>{user_input}</body></html>")

# Insecure Handling of File Uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']  # Vulnerability: Insecure Handling of File Uploads
    uploaded_file.save(f"/uploads/{uploaded_file.filename}")
    return "File uploaded successfully"

if __name__ == '__main__':
    app.run(debug=True)
