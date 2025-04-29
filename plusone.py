from flask import Flask
import os

app = Flask(__name__)
counter_file = "counter.txt"

# Ensure counter.txt exists
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")

@app.route('/', methods=['GET', 'POST'])
def add_100():
    # Read current count
    with open(counter_file, "r") as f:
        count = int(f.read())
    
    # Add 100
    count += 100

    # Save new count
    with open(counter_file, "w") as f:
        f.write(str(count))
    
    return f"Current count is: {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
