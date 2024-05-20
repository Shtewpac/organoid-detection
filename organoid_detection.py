import cv2
import numpy as np
import os
import glob

def record_and_save_video(filename):
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))
    
    if not cap.isOpened():
        print("Failed to open the Dino-Lite microscope.")
        return
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to capture frame from the Dino-Lite microscope.")
            break
        
        frame_with_organoid = detect_organoid(frame)
        out.write(frame_with_organoid)
        cv2.imshow('Dino-Lite Microscope', frame_with_organoid)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def detect_organoid(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_pink = np.array([130, 100, 100])
    upper_pink = np.array([170, 255, 255])
    mask = cv2.inRange(hsv, lower_pink, upper_pink)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        percent = 20
        crop_x = x + int(w * percent / 100)
        crop_y = y + int(h * percent / 100)
        crop_w = w - int(w * percent / 100) * 2
        crop_h = h - int(h * percent / 100) * 2
        cropped_pink = frame[crop_y:crop_y+crop_h, crop_x:crop_x+crop_w]
        
        cropped_gray = cv2.cvtColor(cropped_pink, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(cropped_gray, 120, 255, cv2.THRESH_BINARY)
        contours_threshold, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        organoid_contour = None
        max_area = 0
        
        for contour in contours_threshold:
            area = cv2.contourArea(contour)
            if area > max_area:
                organoid_contour = contour
                max_area = area
        
        if organoid_contour is not None:
            xo, yo, wo, ho = cv2.boundingRect(organoid_contour)
            cv2.rectangle(cropped_pink, (xo, yo), (xo+wo, yo+ho), (255, 0, 0), 2)
            frame[crop_y:crop_y+crop_h, crop_x:crop_x+crop_w] = cropped_pink
    
    return frame

def get_last_video_number(directory):
    video_files = glob.glob(os.path.join(directory, '*.mp4'))
    
    if not video_files:
        return 0
    
    video_numbers = [int(os.path.splitext(os.path.basename(video))[0][6:]) for video in video files]
    return max(video_numbers)

last_video_number = get_last_video_number('videos')
record_and_save_video(f'videos/output{last_video_number + 1}.mp4')
