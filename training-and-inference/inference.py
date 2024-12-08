import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO('best.pt')  # Replace with the path to your .pt file

# Initialize the webcam
cap = cv2.VideoCapture(0)  # Change the index if you have multiple cameras

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        # Run YOLO detection on every frame
        results = model(frame)

        # Initialize counters for current frame
        vacant_count = 0
        occupied_count = 0

        # Process the results
        for result in results:
            for box in result.boxes:
                cls = int(box.cls)  # Class ID
                if cls == 1:  # Assuming 'vacant' class ID is 1
                    vacant_count += 1
                elif cls == 0:  # Assuming 'occupied' class ID is 0
                    occupied_count += 1

        # Annotate the frame with the results
        annotated_frame = results[0].plot()

        # Display counters on the annotated frame
        cv2.putText(annotated_frame, f'Vacant: {vacant_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(annotated_frame, f'Occupied: {occupied_count}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Show the frame
        cv2.imshow('YOLOv8 Real-Time Detection', annotated_frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()