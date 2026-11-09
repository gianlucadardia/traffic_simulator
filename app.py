from flask import Flask, render_template, request, jsonify  
import subprocess  
from generate_events import *
  
app = Flask(__name__)  
  
@app.route('/')  
def index():  
    return render_template('index.html')  # Render html page 
  
@app.route('/run_script', methods=['POST'])  
def run_script():  
    try:  
        # Execute script and get output
        process = subprocess.Popen(  
            ['python', 'generate_events.py'],  # Script execution
            stdout=subprocess.PIPE,  
            stderr=subprocess.PIPE,  
            text=True  
        )  
        # Fetch outpout from the script
        output = []  
        for line in process.stdout:  
            output.append(line.strip())  
  
        # Wait for the process to finish 
        process.wait()  
  
        # Get the return code of the script
        return jsonify({'status': 'success', 'output': output})  
    except Exception as e:  
        return jsonify({'status': 'error', 'error': str(e)})  
  
if __name__ == '__main__':  
    app.run(debug=True)  

