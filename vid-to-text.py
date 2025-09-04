import cv2
import easyocr

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

reader = easyocr.Reader(['en'])

paused = False
last_frame = None

main_color = (255,0,0)

def process_text(input_frame):
    frame = input_frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    results = reader.readtext(gray)
    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))
        cv2.rectangle(frame, top_left, bottom_right, main_color, 2)
        cv2.putText(frame, text, (top_left[0], top_left[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, main_color, 2)

    cv2.imshow("Webcam OCR", frame)

#does this make the window resizable?
cv2.namedWindow("Webcam OCR", cv2.WINDOW_NORMAL)

while True:
    if not paused:
        ret, frame = cap.read()
        if not ret:
            continue
        last_frame = frame.copy()
        cv2.imshow("Webcam OCR", frame) 

    key = cv2.waitKey(1) & 0xFF #because Windows <<<<< Linux or Mac, bitwise AND is needed

    if key == ord('q'):  # Quit
        break

    elif key == 32 and not paused:  # Spacebar
        paused = True
        process_text(last_frame)

    elif key == 32 and paused:  # Spacebar
        paused = False

    elif key == ord('1'):
        main_color = (255,0,0)
        if paused:
            process_text(last_frame)

    elif key == ord('2'):
        main_color = (0,255,0)
        if paused:
            process_text(last_frame)

    elif key == ord('3'):
        main_color = (0,0,255)
        if paused:
            process_text(last_frame)

cap.release()
cv2.destroyAllWindows()
