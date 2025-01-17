from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Flask will automatically look for this in the 'templates' folder

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
