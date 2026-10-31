from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer - Facial Recognition Attendance Software")

        # Title
        title_lbl = Label(self.root, text="DEVELOPERS INFORMATION", font=("times new roman", 35, "bold"), 
                          bg="#001F3F", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=60)

        # Background Image
        bg_img = Image.open("college_images/dev.jpg").resize((1530, 720), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=60, width=1530, height=720)

        # Frame for Developer Info
        main_frame = Frame(bg_label, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=450, y=100, width=650, height=500)

        # Header in Frame
        dev_title = Label(main_frame, text="Creators of Facial Recognition Attendance Software", 
                          font=("times new roman", 18, "bold"), bg="#008080", fg="white")
        dev_title.pack(fill=X)

        # Developer Images (Replace these paths with actual images)
        img_sumit = Image.open("college_images/sumit.jpg").resize((250, 250), Image.Resampling.LANCZOS)
        self.sumit_photo = ImageTk.PhotoImage(img_sumit)

        img_swasthik = Image.open("college_images/swas.jpg").resize((250, 250), Image.Resampling.LANCZOS)
        self.swasthik_photo = ImageTk.PhotoImage(img_swasthik)

        frame_img = Frame(main_frame, bg="white")
        frame_img.pack(pady=10)

        Label(frame_img, image=self.sumit_photo, bg="white").grid(row=0, column=0, padx=20)
        Label(frame_img, image=self.swasthik_photo, bg="white").grid(row=0, column=1, padx=20)

        # Developer Names
        Label(frame_img, text="Sumit Palekar", font=("times new roman", 15, "bold"), bg="white", fg="black").grid(row=1, column=0, pady=5)
        Label(frame_img, text="Swasthik Poojary", font=("times new roman", 15, "bold"), bg="white", fg="black").grid(row=1, column=1, pady=5)

        # Project Information
        project_desc = (
            "🔹 Our Facial Recognition Attendance System is an AI-powered solution\n"
            "🔹 It automates attendance tracking with real-time face detection\n"
            "🔹 Ensures accuracy, security, and seamless attendance management\n"
            "🔹 Features include real-time face detection, CSV export, and database integration\n"
            "🔹 Say goodbye to manual attendance – embrace the future with AI!"
        )
        Label(main_frame, text=project_desc, font=("times new roman", 13), 
              bg="white", justify=LEFT, anchor="w").pack(pady=10, padx=10)

        # Inspirational Quotes
        quotes = [
            "“Technology is best when it brings people together.”",
            "“Innovation distinguishes between a leader and a follower.”",
            "“We are the architects of the future, building a smarter world.”"
        ]
        for quote in quotes:
            Label(main_frame, text=quote, font=("times new roman", 11, "italic"), 
                  bg="white", fg="gray").pack(pady=2)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
