from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess
import platform

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome! Please visit <a href='/htop'>/htop</a> to see the server information.</h1>"

@app.route("/htop")
def htop():
    # Your full name
    name = "Ekta Rajkumar Ghosh"

    # System username
    username = os.getenv('USER', os.getenv('USERNAME', subprocess.getoutput('whoami')))

    # Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Get system info based on OS
    if platform.system() == 'Windows':
        system_output = subprocess.getoutput("tasklist")
    else:
        system_output = subprocess.getoutput("top -bn1")

    # Render the data as a webpage
    return f"""
    <html>
    <head>
        <title>System Monitor</title>
        <style>
            body {{ 
                font-family: Arial, sans-serif; 
                margin: 20px; 
                line-height: 1.6;
            }}
            pre {{ 
                background-color: #f5f5f5; 
                padding: 15px; 
                overflow-x: auto;
                border-radius: 5px;
                border: 1px solid #ddd;
            }}
            .info-item {{
                margin-bottom: 10px;
            }}
        </style>
    </head>
    <body>
        <h1>Server Info</h1>
        <div class="info-item"><b>Name:</b> {name}</div>
        <div class="info-item"><b>User:</b> {username}</div>
        <div class="info-item"><b>Server Time (IST):</b> {server_time}</div>
        <div class="info-item"><b>Operating System:</b> {platform.system()}</div>
        <h2>Process List:</h2>
        <pre>{system_output}</pre>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)