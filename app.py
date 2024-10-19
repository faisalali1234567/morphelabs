from flask import Flask
import os
import time
import subprocess
import getpass

app = Flask(__name__)  # Corrected here

@app.route('/htop')
def htop():
    # Get system username
    username = getpass.getuser()

    # Get the server time in IST (Indian Standard Time)
    ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 19800))  # Adding 5 hours 30 minutes to UTC

    # Get the top output (first 10 lines)
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    # Create a response with the details
    response = f"""
    <h1>Name: Faisal Ali</h1>
    <p>Username: {username}</p>
    <p>Server Time (IST): {ist_time}</p>
    <pre>TOP output:<br>{top_output}</pre>
    """

    return response

if __name__ == "__main__":  # Corrected here
    app.run(host="0.0.0.0", port=5000)
