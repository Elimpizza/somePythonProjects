import cv2
import easyocr

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

reader = easyocr.Reader(['en'])

paused = False
last_frame = None

cv2.namedWindow("Webcam OCR", cv2.WINDOW_NORMAL)

while True:
    if not paused:
        ret, frame = cap.read()
        if not ret:
            continue
        last_frame = frame.copy()
        cv2.imshow("Webcam OCR", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):  # Quit
        break

    elif key == 32 and not paused:  # Spacebar PRESSED
        paused = True

        gray = cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)
        results = reader.readtext(gray)

        for (bbox, text, prob) in results:
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = tuple(map(int, top_left))
            bottom_right = tuple(map(int, bottom_right))
            cv2.rectangle(last_frame, top_left, bottom_right, (0, 255, 0), 2)
            cv2.putText(last_frame, text, (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show paused frame with OCR results
        cv2.imshow("Webcam OCR", last_frame)

    elif key != 255 and paused:  # Any key RELEASED (other than no key)
        paused = False

cap.release()
cv2.destroyAllWindows()
