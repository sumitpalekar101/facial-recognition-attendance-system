from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Software")

        # ====== Dark-Themed Background ======
        self.bg_color1 = "#141E30"  # Dark blue
        self.bg_color2 = "#243B55"  # Light blue
        self.root.configure(bg=self.bg_color1)

        # ====== Title Frame (Ensures Title is Visible) ======
        title_frame = Frame(self.root, bg="black")
        title_frame.place(x=0, y=0, width=1530, height=70)  # Increased height for visibility

        title_lbl = Label(
            title_frame, text="FACE RECOGNITION", font=("times new roman", 40, "bold"),
            bg="black", fg="white", pady=10
        )
        title_lbl.pack(fill=X)

        # ====== Image (Left Side) ======
        img_left = Image.open("college_images/face_detector1.jpg")
        img_left = img_left.resize((650, 700), Image.Resampling.NEAREST)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        bgLabel1 = Label(self.root, image=self.photoimg_left, bd=2, relief=RIDGE)
        bgLabel1.place(x=0, y=80, width=650, height=700)  # Moved down

        # ====== Image (Right Side) ======
        img_right = Image.open("college_images/face.jpg")
        img_right = img_right.resize((950, 700), Image.Resampling.NEAREST)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        bgLabel2 = Label(self.root, image=self.photoimg_right, bd=2, relief=RIDGE)
        bgLabel2.place(x=650, y=80, width=950, height=700)  # Moved down

        # ====== Button ======
        btn = Button(
            bgLabel2, text="Face Recognition", command=self.face_recog, cursor="hand2",
            font=("times new roman", 18, "bold"), width=17, bg="#12D8FA", fg="white",
            activebackground="#0AA1C5", activeforeground="black", relief=RAISED, bd=5
        )
        btn.place(x=365, y=620, width=220, height=50)

    #  =================================== Attendance Marking =====================
    def Mark_attendance(self, i, r, n, d):
        with open("Sp.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]

            if i not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="sumit@123", database="facerecognizer"
                )
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name from stud_attend where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else ""

                my_cursor.execute("SELECT Roll from stud_attend where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else ""

                my_cursor.execute("SELECT Dep from stud_attend where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else ""

                my_cursor.execute("SELECT Student_id from stud_attend where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i) if i else ""

                print(f"Predicted ID: {id}, Confidence: {confidence}, {n}")

                if confidence > 77:
                    cv2.putText(img, f"Id: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.Mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCAP = cv2.VideoCapture(0)

        while True:
            ret, img = videoCAP.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        videoCAP.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
