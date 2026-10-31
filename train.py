from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")

        # ====== Gradient Background ======
        self.bg_color1 = "#141E30"  # Dark blue
        self.bg_color2 = "#243B55"  # Light blue
        self.root.configure(bg=self.bg_color1)

        # ====== Title Label ======
        title_lbl = Label(
            self.root, text="TRAIN DATA SET", font=("times new roman", 40, "bold"),
            bg=self.bg_color1, fg="white", pady=10
        )
        title_lbl.pack(fill=X)

        # ====== Image 1 (Top) ======
        img_top = Image.open("college_images/facial-recognition_0.jpg")
        img_top = img_top.resize((1530, 300), Image.Resampling.NEAREST)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        bgLabel = Label(self.root, image=self.photoimg_top, bd=2, relief=RIDGE)
        bgLabel.pack(pady=5)

        # ====== Train Button (Stylish) ======
        btn = Button(
            self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
            font=("times new roman", 30, "bold"), width=17,
            bg="#F7971E", fg="white", activebackground="#FFB84D", activeforeground="black",
            relief=RAISED, bd=5
        )
        btn.pack(pady=10)

        # ====== Image 2 (Bottom) ======
        img_bottom = Image.open("college_images/Photo.jpg")
        img_bottom = img_bottom.resize((1530, 300), Image.Resampling.NEAREST)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        bgLabel2 = Label(self.root, image=self.photoimg_bottom, bd=2, relief=RIDGE)
        bgLabel2.pack(pady=5)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert('L')  # Gray scale image
                imageNp = np.array(img, 'uint8')
                filename = os.path.split(image)[1]
                id = int(filename.split('.')[1])
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1) == 13
            except Exception as e:
                print(f"Error processing {image}: {e}")

        ids = np.array(ids)

        # Train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training of images completed successfully!", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
