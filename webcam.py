import cv2

# Open webcam
cap = cv2.VideoCapture(0)
background = None

print("📷 Camera is on. Press 'c' to capture background, or 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame (to fix mirror effect)
    frame = cv2.flip(frame, 1)

    # Show live feed
    cv2.imshow("Webcam Feed", frame)

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):  # If 'c' is pressed
        background = frame.copy()
        print("✅ Background captured successfully!")

        # Save background image in the same folder as this script
        cv2.imwrite("background.jpg", background)
        print("💾 Background saved as 'background.jpg' in the current folder.")

        cv2.imshow("Captured Background", background)
        cv2.waitKey(0)
        break

    elif key == ord('q'):  # Quit without capturing
        print("❌ Quit without capturing background.")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
