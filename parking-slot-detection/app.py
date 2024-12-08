from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import time
import csv
from threading import Thread
from ultralytics import YOLO
import cv2

# Flask setup
app = Flask(__name__)
socketio = SocketIO(app)

# File log
LOG_FILE = 'parking_log.csv'

# YOLO model
model = YOLO('best.pt')  # Replace with your model path

# Initialize webcam
cap = cv2.VideoCapture(0)  # Change index for your webcam

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Initialize timers
prev_time = 0
detection_interval = 2

TOTAL_SLOTS = 12

# Detection function
def detect_and_log():
    global prev_time
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture image")
                break

            curr_time = time.time()
            if curr_time - prev_time >= detection_interval:
                prev_time = curr_time
                results = model(frame)

                occupied_count = sum(1 for result in results for box in result.boxes if int(box.cls) == 0)
                vacant_count = TOTAL_SLOTS - occupied_count

                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                with open(LOG_FILE, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([timestamp, vacant_count, occupied_count])

                socketio.emit('update_counters', {'vacant': max(vacant_count, 0), 'occupied': occupied_count})
                socketio.emit('update_log', {'timestamp': timestamp, 'vacant': vacant_count, 'occupied': occupied_count})

                annotated_frame = results[0].plot()
                cv2.putText(annotated_frame, f'Vacant: {vacant_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(annotated_frame, f'Occupied: {occupied_count}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow('YOLOv5 Detection', annotated_frame)

            else:
                cv2.imshow('YOLOv5 Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

# Start detection in a separate thread
Thread(target=detect_and_log, daemon=True).start()

# Flask route to serve the web dashboard
@app.route('/')
def dashboard():
    # Read the latest log entry
    log_data = []
    with open(LOG_FILE, 'r') as file:
        reader = csv.reader(file)
        log_data = list(reader)

    return render_template('dashboard.html', log_data=log_data)

# Flask route to get the log data in real-time
@app.route('/log_data')
def log_data():
    # Read the latest log entries
    log_data = []
    with open(LOG_FILE, 'r') as file:
        reader = csv.reader(file)
        log_data = list(reader)
    
    # Return data as JSON
    return jsonify({'log_data': log_data})

# Start Flask app with SocketIO
if __name__ == '__main__':
    # Initialize log file with headers
    with open(LOG_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Vacant Slots', 'Occupied Slots'])

    socketio.run(app, host='0.0.0.0', port=5000, debug=False)