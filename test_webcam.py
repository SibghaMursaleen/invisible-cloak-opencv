import cv2
import numpy as np

# Load saved background
background = cv2.imread("background.jpg")

# Open webcam
cap = cv2.VideoCapture(0)

print("🪄 Invisible Cloak Activated! Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame
    frame = cv2.flip(frame, 1)

    # Resize background to match webcam size
    background = cv2.resize(background, (frame.shape[1], frame.shape[0]))

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Black cloak range
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])

    mask = cv2.inRange(hsv, lower_black, upper_black)


    # #Red cloak range
    # # Lower red (expanded)
    # lower_red1 = np.array([0, 100, 50])
    # upper_red1 = np.array([15, 255, 255])

    # # Upper red (expanded)
    # lower_red2 = np.array([165, 100, 50])
    # upper_red2 = np.array([180, 255, 255])

    # # Mask for cloak
    # mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    # mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # mask = mask1 + mask2

    # Optional: clean up the mask
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    # Refine mask (remove noise, smooth edges)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))

    # Cloak region from background
    cloak_area = cv2.bitwise_and(background, background, mask=mask)

    # Rest of the frame without cloak
    rest_area = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))

    # Final output
    final = cv2.addWeighted(cloak_area, 1, rest_area, 1, 0)

    # Show
    cv2.imshow("Invisible Cloak", final)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
