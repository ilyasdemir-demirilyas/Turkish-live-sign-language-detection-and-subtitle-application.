
import torch
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

import time


class ObjectDetection:
    """
    Class implements Yolo5 model to make inferences on a youtube video using OpenCV.
    """
    
    def __init__(self):
        """
        Initializes the class with youtube url and output file.
        :param url: Has to be as youtube URL,on which prediction is made.
        :param out_file: A valid output file name.
        """
        self.model = self.load_model()
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("\n\nDevice Used:",self.device)




    def load_model(self):
        """
        Loads Yolo5 model from pytorch hub.
        :return: Trained Pytorch model.
        """
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='agırlık_dosyası.pt')   # local repo

        #model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

        return model


    def score_frame(self, frame):
        """
        Takes a single frame as input, and scores the frame using yolo5 model.
        :param frame: input frame in numpy/list/tuple format.
        :return: Labels and Coordinates of objects detected by model in the frame.
        """
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
     
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]

        return labels, cord


    def class_to_label(self, x):
        """
        For a given label value, return corresponding string label.
        :param x: numeric label
        :return: corresponding string label
        """

        return self.classes[int(x)]


    def plot_boxes(self, results, frame):
        """
        Takes a frame and its results as input, and plots the bounding boxes and label on to the frame.
        :param results: contains labels and coordinates predicted by model on the given frame.
        :param frame: Frame which has been scored.
        :return: Frame with bounding boxes and labels ploted on it.
        """
        
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.65:
                x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
                cv2.putText(frame, str(row[4]) , (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
                print(str(row[4]) , " - ", self.class_to_label(labels[i]) )
                metin.append(self.class_to_label(labels[i]))
                sonhal=" "
                for i in metin :
                    if(sonhal[-1]==i):
                        pass
                    else:
                        sonhal+=i
                    
                # Alt yazı metninin boyutunu hesapla
                text_size = cv2.getTextSize(str(sonhal), cv2.FONT_HERSHEY_SIMPLEX, 0.9, 2)
                text_width = text_size[0][0]
                text_height = text_size[0][1]

                # Alt yazı arka planını çiz
                rectangle_top_left = (int((frame.shape[1] - text_width) / 2) - 10, frame.shape[0] - 30 - text_height - 10)
                rectangle_bottom_right = (int((frame.shape[1] + text_width) / 2) + 10, frame.shape[0] - 30 + 10)
                cv2.rectangle(frame, rectangle_top_left, rectangle_bottom_right, (200, 200, 0), cv2.FILLED)

                # Alt yazıyı çiz
                text_x = int((frame.shape[1] - text_width) / 2)  # X koordinatını görüntünün ortasına al
                text_y = frame.shape[0] - 30  # Y koordinatını görüntünün altına al
                cv2.putText(frame, str(sonhal), (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)



        return frame


    def __call__(self):
        """
        This function is called when class is executed, it runs the loop to read the video frame by frame,
        and write the output into a new file.
        :return: void
        """
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            
            start_time = time.perf_counter()
            ret, frame = cap.read()
            if not ret:
                break
            results = self.score_frame(frame)
            frame = self.plot_boxes(results, frame)
            end_time = time.perf_counter()
            fps = 1 / np.round(end_time - start_time, 3)
            cv2.putText(frame, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)
            cv2.imshow("img", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

metin=[]
# Create a new object and execute.
detection = ObjectDetection()
detection()