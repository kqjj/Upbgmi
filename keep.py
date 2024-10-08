
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return "Alive"

# Define multiple runs for different ports
def run_on_port(port):
    app.run(host='0.0.0.0', port=port)

# Launch threads for multiple ports
def keep_alive():
    ports = [8080, 1111, 8888, 9001, 9002, 9003, 9004, 9005, 9006, 9007, 9008, 9009, 9010, 9011, 9012, 9013, 9014, 9015, 9016, 9017, 9018, 9019, 9020]
    
    # Start a thread for each port
    for port in ports:
        t = Thread(target=run_on_port, args=(port,))
        t.start()
