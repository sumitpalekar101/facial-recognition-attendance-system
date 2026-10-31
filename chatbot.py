from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class chatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+700+0")
        self.root.bind('<Return>', self.enter_func)

        frame = Frame(self.root, bg="black", width=610)
        frame.pack()

        img2 = Image.open("college_images/chat.jpg").resize((200, 70), Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        lblimg1 = Label(frame, image=self.photoimage2, bd=3, compound=LEFT, width=730,
                        text="CHAT WITH ME", font=('Times New Roman', 30, 'bold'),
                        fg='green', relief=RAISED, anchor='nw', bg="white")
        lblimg1.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(frame, orient=VERTICAL)
        self.text = Text(frame, width=65, height=20, bd=3, relief=RAISED,
                         font=('arial', 14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, bd=4, bg='white', width=730)
        btn_frame.pack()

        Label(btn_frame, text="Type Something", font=('arial', 14, 'bold'),
              fg='green', bg='white').grid(row=0, column=0, padx=5, sticky=W)

        self.entry1 = StringVar()
        self.entry = ttk.Entry(btn_frame, textvariable=self.entry1, width=40,
                               font=('times new roman', 16, 'bold'))
        self.entry.grid(row=0, column=1, padx=5, sticky=W)

        self.send1 = Button(btn_frame, text="Send", command=self.send,
                            font=('arial', 15, 'bold'), width=8, bg='green')
        self.send1.grid(row=0, column=2, padx=5, sticky=W)

        self.clear_btn = Button(btn_frame, text="Clear Data", command=self.clear,
                                font=('arial', 15, 'bold'), width=8, bg='red', fg='white')
        self.clear_btn.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label1 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'),
                            fg='green', bg='white')
        self.label1.grid(row=1, column=1, padx=5, sticky=W)

    # Function to trigger sending message when Enter key is pressed
    def enter_func(self, event):
        self.send()
        self.entry1.set('')

    # Function to clear the chatbox and entry field
    def clear(self):
        self.text.delete('1.0', END)
        self.entry1.set('')

    # Function to handle sending messages and bot responses
    def send(self):
        user_input = self.entry1.get().strip().lower()
        if not user_input:
            self.msg = 'Please enter some input'
            self.label1.config(text=self.msg, fg='red')
            return

        self.msg = ''
        self.label1.config(text=self.msg, fg='red')

        # Display user message
        self.text.insert(END, f'\n\t\t\tYou: {self.entry1.get()}')
        self.text.yview(END)

        # Predefined responses
        responses = {
            # Basic Conversations
            "hello": "Hi! How can I help you today?",
            "hi": "Hello! How can I assist you?",
            "how are you?": "I'm fine, and you?",
            "fantastic": "Nice to hear!",
            "who created you?": "Mr. Swasthik and Sumit developed me using Python.",
            "what is your name?": "My name is Mr. Jarvis, your assistant.",
            "bye": "Goodbye! Have a great day.",
            "can you speak marathi": "I'm still learning Marathi...",
            "thank you": "You're welcome!",
            "what can you do?": "I can assist with facial recognition attendance software and answer general queries.",

            # Facial Recognition Attendance Software Related
            "what is facial recognition attendance?": "It's an AI-based system that marks attendance using facial recognition technology.",
            "how does facial recognition attendance work?": "It captures facial features, matches them with stored data, and logs attendance automatically.",
            "can the system detect multiple faces?": "Yes, it can detect multiple faces in real-time and mark attendance accordingly.",
            "is facial recognition attendance accurate?": "Yes, with good-quality images, it can achieve over 95% accuracy.",
            "what if someone is absent?": "If a person is absent, their face won`t be detected, and attendance won’t be marked.",
            "can i export attendance data?": "Yes, the system allows exporting attendance data in CSV format.",
            "can i import attendance records?": "Yes, you can import existing attendance data using a CSV file.",
            "how can i delete an entry?": "You can select an entry in the table and click the 'Delete' button.",
            "how can i reset data?": "Click the 'Reset' button to clear the current inputs.",

            # Common Technical Questions
            "do you support real-time attendance?": "Yes, the system works in real-time and updates attendance instantly.",
            "is my data secure?": "Yes, all attendance records are securely stored and protected.",
            "can i integrate this system with other software?": "Yes, it can be integrated with other management systems.",
            "what hardware is needed?": "A webcam or CCTV camera, a computer, and the required software setup.",
            "can this work with low lighting?": "Facial recognition works best in good lighting, but advanced models support low-light recognition.",
            "does it work with masks?": "Some advanced versions can detect partially covered faces, but accuracy may be reduced.",
        }

        # Bot Response
        bot_response = responses.get(user_input, "I'm sorry, I didn't understand that. Can you rephrase?")
        self.text.insert(END, f'\n\nBot: {bot_response}')
        self.entry1.set('')

if __name__ == "__main__":
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
