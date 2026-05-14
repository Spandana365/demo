from flask import Flask, render_template

# Adding template_folder='.' tells Flask to look in the current directory
app = Flask(__name__, template_folder='.')

@app.route('/')
def hello():
    return render_template('demo.html')

if __name__ == "__main__":
    # Host 0.0.0.0 and Port 80 are perfect for Azure ACI
    app.run(host='0.0.0.0', port=80)
