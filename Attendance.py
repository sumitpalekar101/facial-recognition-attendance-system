from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
import os
import csv

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Software")

        # Variables
        self.var_attend = StringVar()
        self.var_roll = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance_atten = StringVar()
        self.var_name = StringVar()
        self.mydata = []
        
        # Images
        self.load_images()
        
        # UI Elements
        self.setup_ui()
        
        # Auto import CSV data
        self.auto_import_csv("Sp.csv")

    def load_images(self):
        self.photoimg3 = ImageTk.PhotoImage(Image.open("college_images/gettyimages-1022573162.jpg").resize((800, 200), Image.Resampling.NEAREST))
        self.photoimgs = ImageTk.PhotoImage(Image.open("college_images/smart-attendance.jpg").resize((800, 200), Image.Resampling.NEAREST))
        self.photoimgbg = ImageTk.PhotoImage(Image.open("college_images/hackers2.jpg").resize((1530, 710), Image.Resampling.NEAREST))
        self.photoimg4 = ImageTk.PhotoImage(Image.open("college_images/4.jpeg").resize((720, 130), Image.Resampling.NEAREST))
    
    def setup_ui(self):
        Label(self.root, image=self.photoimg3).place(x=0, y=0, width=800, height=200)
        Label(self.root, image=self.photoimgs).place(x=800, y=0, width=800, height=200)
        bgLabel = Label(self.root, image=self.photoimgbg)
        bgLabel.place(x=0, y=200, width=1530, height=710)
        
        title_lbl = Label(self.root, text="ATTENDANCE MANAGEMENT SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        mainF = Frame(bgLabel, bd=2, bg="white")
        mainF.place(x=20, y=55, width=1480, height=600)

        # Left Frame
        left_fram = LabelFrame(mainF, bd=2, bg="white", text="Attendance Details", relief=RIDGE, font=("times new roman", 10, "bold"))
        left_fram.place(x=10, y=10, width=730, height=580)

        Label(left_fram, image=self.photoimg4).place(x=0, y=0, width=720, height=130)
        
        Lmain_fram = Frame(left_fram, bd=2, bg="white", relief=RIDGE)
        Lmain_fram.place(x=0, y=135, width=720, height=370)
        
        # Labels and Entries
        self.create_labels_entries(Lmain_fram)
        
        # Buttons
        self.create_buttons(Lmain_fram)
        
        # Right Frame (Table)
        self.setup_table(mainF)
    
    def auto_import_csv(self, filename):
        try:
            with open(filename, newline="") as file:
                reader = csv.reader(file)
                self.mydata = list(reader)
                self.update_table()
                print("CSV data imported successfully")
        except FileNotFoundError:
            print("CSV file not found")
    
    def update_table(self):
        self.attendanceTable.delete(*self.attendanceTable.get_children())
        for row in self.mydata:
            self.attendanceTable.insert("", END, values=row)
    
    def create_labels_entries(self, parent):
        labels = ["Attendance ID:", "Name:", "Roll:", "Department:", "Time:", "Date:", "Attendance Status"]
        vars = [self.var_attend, self.var_name, self.var_roll, self.var_dep, self.var_time, self.var_date, self.var_attendance_atten]
        for i, (label, var) in enumerate(zip(labels, vars)):
            Label(parent, text=label, font=("times new roman", 12, "bold"), bg="white").grid(row=i//2, column=(i%2)*2, padx=8, sticky=W)
            if label == "Attendance Status":
                self.atten_status = ttk.Combobox(parent, width=20, textvariable=var, font=("times new roman", 12), state="readonly", values=("Status", "Present", "Absent"))
                self.atten_status.grid(row=i//2, column=(i%2)*2+1, pady=8)
                self.atten_status.current(0)
            else:
                ttk.Entry(parent, width=22, textvariable=var, font=("times new roman", 12)).grid(row=i//2, column=(i%2)*2+1, pady=8)
    
    def create_buttons(self, parent):
        btn_frame = Frame(parent, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)
        
        buttons = [
            ("Import CSV", lambda: self.import_csv("Sp.csv")),
            ("Export CSV", self.export_csv),
            ("Delete", self.delete_data),
            ("Reset", self.reset_data)
        ]
        for i, (text, cmd) in enumerate(buttons):
            Button(btn_frame, text=text, command=cmd, font=("times new roman", 13, "bold"), width=17, bg="blue", fg="white").grid(row=0, column=i)
    
    def import_csv(self, filename):
        try:
            with open(filename, newline="") as file:
                reader = csv.reader(file)
                self.mydata = list(reader)
                self.update_table()
                print("CSV data imported successfully")
        except FileNotFoundError:
            print("CSV file not found")
        
    
    def export_csv(self):
        if not self.mydata:
            messagebox.showerror("No Data", "No data available to export", parent=self.root)
            return
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],parent=self.root)
        if filename:
            try:
                with open(filename, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(self.mydata)
                messagebox.showinfo("Success", "Data exported successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error exporting data: {str(e)}", parent=self.root)
    
    
    def get_cursor(self,event=""):
        cursor_row = self.attendanceTable.focus()
        content = self.attendanceTable.item(cursor_row)
        row = content['values']
        if row:
            self.var_attend.set(row[0])
            self.var_roll.set(row[1])
            self.var_name.set(row[2])
            self.var_dep.set(row[3])
            self.var_time.set(row[4])
            self.var_date.set(row[5])
            self.var_attendance_atten.set(row[6])
        
    def delete_data(self):
        selected_item = self.attendanceTable.selection()
        if selected_item:
            for item in selected_item:
                self.attendanceTable.delete(item)
        else:
            messagebox.showerror("Error", "No record selected", parent=self.root)  
    
    def reset_data(self):
        self.var_attend.set("")          
        self.var_roll.set("")          
        self.var_name.set("")          
        self.var_dep.set("")          
        self.var_time.set("")          
        self.var_date.set("")          
        self.var_attendance_atten.set("Status")
        
    
    def setup_table(self, parent):
        Right_fram = LabelFrame(parent, bd=2, bg="white", text="Student Details", relief=RIDGE, font=("times new roman", 10, "bold"))
        Right_fram.place(x=750, y=10, width=720, height=580)
        
        Table_frame = Frame(Right_fram, bd=2, relief=RIDGE, bg="white")
        Table_frame.place(x=5, y=5, width=700, height=455)
        
        Scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        
        self.attendanceTable = ttk.Treeview(Table_frame, columns=("id", "roll", "name", "department", "time", "date", "attendance"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.config(command=self.attendanceTable.xview)
        Scroll_y.config(command=self.attendanceTable.yview)
        self.attendanceTable.pack(fill=BOTH, expand=1)
        self.attendanceTable.heading("id", text="Attendance ID")
        self.attendanceTable.heading("roll", text="Roll")
        self.attendanceTable.heading("name", text="Name")
        self.attendanceTable.heading("department", text="Department")
        self.attendanceTable.heading("time", text="Time")
        self.attendanceTable.heading("date", text="Date")
        self.attendanceTable.heading("attendance", text="Attendance")
        self.attendanceTable["show"] = "headings"
        
        self.attendanceTable.bind("<ButtonRelease>",self.get_cursor)

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
