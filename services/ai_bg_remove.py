import cv2
import numpy as np

class BackgroundRemover:
    def __init__(self):
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    def remove_background(self, frame):
        mask = self.bg_subtractor.apply(frame)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        return result

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)  # Use the default camera
    remover = BackgroundRemover()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = remover.remove_background(frame)
        cv2.imshow('Background Removal', result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()