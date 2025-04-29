from flask import Flask, request
import os

app = Flask(__name__)

counter_file = "counter.txt"

# Ensure counter.txt exists
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")

@app.route('/', methods=['GET', 'POST'])
def add_100():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    
    # Read current count
    with open(counter_file, "r") as f:
        count = int(f.read())
    
    # Initial menu (if text is empty)
    if text == '':
        response = "CON What would you like to do? \n"
        response += "1. View current count \n"
        response += "2. Add 100"
        
    # Add 100 and show the updated count
    elif text == '2':
        count += 100
        with open(counter_file, "w") as f:
            f.write(str(count))
        response = f"END Count updated! New count is: {count}"
    
    # Show the current count (if text is 1)
    elif text == '1':
        response = f"END Current count is: {count}"
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
