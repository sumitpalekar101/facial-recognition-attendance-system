from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import random,os
import re
from time import strftime
from datetime import datetime 
from tkcalendar import DateEntry





class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Software")
        
    # ====variable=======
    
        self.var_dep=StringVar()
        self.var_role=StringVar()
        self.var_course=StringVar()    
        self.var_year=StringVar()    
        self.var_sem=StringVar()    
        self.var_studid=StringVar()
        x=random.randint(1,9999)  
        self.var_studid.set(str(x))  
        self.var_studnam=StringVar()    
        self.var_div=StringVar()    
        self.var_roll=StringVar()    
        self.var_gender=StringVar()    
        self.var_dob=StringVar()    
        self.var_email=StringVar()    
        self.var_phone=StringVar()    
        self.var_address=StringVar()    
        self.var_teacher=StringVar()    
    # self.=StringVar()    
    # self.=StringVar()    
        
        
        # images 
       
        img=Image.open("college_images/face-recognition.png")
        img= img.resize((500,130),Image.Resampling.NEAREST)
        self.photoimg = ImageTk.PhotoImage(img)
        PhotoLabel=Label(self.root,image=self.photoimg)
        PhotoLabel.place(x=0,y=0,width=500,height=130)
        
        img1=Image.open("college_images/smart-attendance.jpg")
        img1= img1.resize((500,130),Image.Resampling.NEAREST)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        PhotoLabel2=Label(self.root,image=self.photoimg1)
        PhotoLabel2.place(x=500,y=0,width=500,height=130)
        
        img2=Image.open("college_images/gettyimages-1022573162.jpg")
        img2= img2.resize((550,130),Image.Resampling.NEAREST)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        PhotoLabel3=Label(self.root,image=self.photoimg2)
        PhotoLabel3.place(x=1000,y=0,width=550,height=130)
     # bg image
    
        img3=Image.open("college_images/6.jpg")
        img3= img3.resize((1530,710),Image.Resampling.NEAREST)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bgLabel=Label(self.root,image=self.photoimg3)
        bgLabel.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bgLabel,text="STUDENT MANAGEMENT SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        mainF=Frame(bgLabel,bd=2,bg="white")
        mainF.place(x=10,y=55,width=1500,height=600)
        
#    left label frame
        left_fram=LabelFrame(mainF,bd=2,bg="white",text="Student Details",relief=RIDGE,font=("times new roman",10,"bold"))
        left_fram.place(x=10,y=10,width=730,height=580)
        
        
        img4=Image.open("college_images/4.jpeg")
        img4= img4.resize((720,130),Image.Resampling.NEAREST)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        PhotoLabel3=Label(left_fram,image=self.photoimg4)
        PhotoLabel3.place(x=5,y=0,width=720,height=130)
    # information list

        self.role=["Select Role","Student","Faculty"]
        self.subStud1=["Select Department","computer","IT","Civil","Mechnical"]
        self.subStud2=["Select Course","FE","SE","TE","BE"]
        self.subStud3=["Select Year","2020-21","2021-22","2022-23","2023-24","2024-25"]
        self.subStud4=["Select Semester","Semester-1","Semester-2"]
        
        self.subFaculty1=["Select Department","Commerce","Science","Civil","Mechnical"]
        self.subFaculty2=["Select Course",]
        self.subFaculty3=["Select Year","2020-21","2021-22","2022-23","2023-24","2024-25"]
        self.subFaculty4=["Select Semester","Semester-1","Semester-2","All"]
        
    
    # CURRENT course
        current_fram=LabelFrame(left_fram,bd=2,bg="white",text="Current Course Information",relief=RIDGE,font=("times new roman",10,"bold"))
        current_fram.place(x=5,y=135,width=720,height=150)
              
              
              
    # FAculty or Stude
        self.Faculty_label=Label(current_fram,text="User Type",font=("times new roman",12,"bold"),bg="white")
        self.Faculty_label.grid(row=0,column=0,padx=10) 
        self.Faculty_combo=ttk.Combobox(current_fram,value=self.role,textvariable=self.var_role,font=("times new roman",12,"bold"),width=17,state='readonly')
        self.Faculty_combo.current(0)
        self.Faculty_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        self.Faculty_combo.bind("<<ComboboxSelected>>",self.Categories)
        
    # department
        self.dep_label=Label(current_fram,text="Deparment",font=("times new roman",12,"bold"),bg="white")
        self.dep_label.grid(row=1,column=0,padx=10)        
        self.dep_combo=ttk.Combobox(current_fram,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state='readonly')
        self.dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
    # course
        self.course_label=Label(current_fram,text="Course",font=("times new roman",12,"bold"),bg="white")
        self.course_label.grid(row=1,column=2,padx=10) 
        self.course_combo=ttk.Combobox(current_fram,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state='readonly')
        self.course_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
    # year
        self.year_label=Label(current_fram,text="Year",font=("times new roman",12,"bold"),bg="white")
        self.year_label.grid(row=2,column=0,padx=10)
        self.year_combo=ttk.Combobox(current_fram,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state='readonly')
        self.year_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
    
    #semester
        self.sem_label=Label(current_fram,text="Semester",font=("times new roman",12,"bold"),bg="white")
        self.sem_label.grid(row=2,column=2,padx=10,sticky=W) 
        self.sem_combo=ttk.Combobox(current_fram,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=17,state='readonly')
        self.sem_combo.grid(row=2,column=3,padx=2,pady=10,sticky=W)
        
        
 # Class student Info
        Student_fram=LabelFrame(left_fram,bd=2,bg="white",text="Class Student Information",relief=RIDGE,font=("times new roman",10,"bold"))
        Student_fram.place(x=5,y=290,width=720,height=300)
       
    # StudentId
        Student_label=Label(Student_fram,text="UserID: ",font=("times new roman",12,"bold"),bg="white")
        Student_label.grid(row=0,column=0,padx=10,sticky=W)
        StudentID_entry=ttk.Entry(Student_fram,textvariable=self.var_studid,width=20,font=("times new roman",12,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
    # StudentName
        StudentNam_label=Label(Student_fram,text="Name: ",font=("times new roman",12,"bold"),bg="white")
        StudentNam_label.grid(row=0,column=2,padx=10,sticky=W)
        Studentnam_entry=ttk.Entry(Student_fram,textvariable=self.var_studnam,width=20,font=("times new roman",12,"bold"))
        Studentnam_entry.grid(row=0,column=3,padx=10,sticky=W)
                
        
    # class divisions
        class_div_label=Label(Student_fram,text="Class Div: ",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,sticky=W)
        # class_div_entry=ttk.Entry(Student_fram,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,sticky=W)
        classdiv_combo=ttk.Combobox(Student_fram,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state='readonly')
        classdiv_combo["values"]=["A","B","C"]
        classdiv_combo.current(0)
        classdiv_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
         
    #roll NO
        RollNo_label=Label(Student_fram,text="Roll No: ",font=("times new roman",12,"bold"),bg="white")
        RollNo_label.grid(row=1,column=2,padx=10,sticky=W)
        RollNo_entry=ttk.Entry(Student_fram,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        RollNo_entry.grid(row=1,column=3,padx=10,sticky=W)
        
        
    # Gender
        Gender_label=Label(Student_fram,text="Gender: ",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        # Gender_entry=ttk.Entry(Student_fram,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # Gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        Gender_combo=ttk.Combobox(Student_fram,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state='readonly')
        Gender_combo["values"]=["Male","Female","Other"]
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        
    # DOB
        dob_label=Label(Student_fram,text="DOB: ",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=DateEntry(Student_fram,textvariable=self.var_dob,width=24,selectmode='day',date_pattern="dd/mm/Y")
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
    #Email
        email_label=Label(Student_fram,text="Email: ",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        email_entry=ttk.Entry(Student_fram,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
    #phone no
        phone_label=Label(Student_fram,text="Phone No: ",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        phone_entry=ttk.Entry(Student_fram,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
    #Address
        address_label=Label(Student_fram,text="Address: ",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        address_entry=ttk.Entry(Student_fram,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
    #Teacher name
        teacher_label=Label(Student_fram,text="Nationality: ",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        teacher_entry=ttk.Entry(Student_fram,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
    # Radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Student_fram,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0,padx=10) 
        
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(Student_fram,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1) 
    # Button frame
        btn_frame=Frame(Student_fram,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=185,width=715,height=40)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",13,"bold"),width=17,bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        Updated_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",13,"bold"),width=17,bg="blue",fg="white")
        Updated_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",13,"bold"),width=17,bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),width=17,bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn22_frame=Frame(Student_fram,bd=2,relief=RIDGE,bg="white")
        btn22_frame.place(x=0,y=220,width=715,height=35)
        
        Take_photo_btn=Button(btn22_frame,text="Take Photo Sample",command=self.generate_dataset,font=("times new roman",13,"bold"),width=35,bg="blue",fg="white")
        Take_photo_btn.grid(row=0,column=0)
        
        upd_photo_btn=Button(btn22_frame,text="Update Photo Sample",command=self.update_photo_sample,font=("times new roman",13,"bold"),width=35,bg="blue",fg="white")
        upd_photo_btn.grid(row=0,column=1)
        

        

#    Right label frame
        Right_fram=LabelFrame(mainF,bd=2,bg="white",text="Student Details",relief=RIDGE,font=("times new roman",10,"bold"))
        Right_fram.place(x=750,y=10,width=720,height=580)
        
        imgRi=Image.open("college_images/images.jpg")
        imgRi= imgRi.resize((720,130),Image.Resampling.NEAREST)
        self.photoimg5 = ImageTk.PhotoImage(imgRi)
        PhotoLabel=Label(Right_fram,image=self.photoimg5)
        PhotoLabel.place(x=5,y=0,width=720,height=130)
        
# =================SEARCH Software===============
        SEARCH_fram=LabelFrame(Right_fram,bd=2,bg="white",text="Search System",relief=RIDGE,font=("times new roman",10,"bold"))
        SEARCH_fram.place(x=5,y=135,width=710,height=70)
       
        Search_label=Label(SEARCH_fram,text="Search By: ",font=("times new roman",12,"bold"),bg="yellow")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
       
        self.search_var=StringVar() 
        Search_combo=ttk.Combobox(SEARCH_fram,textvariable=self.search_var,font=("times new roman",12,"bold"),width=17,state='readonly')
        Search_combo["values"]=["select","Student_id","Dep","Year"]
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.txt_search=StringVar()
        Search_entry=ttk.Entry(SEARCH_fram,width=20,textvariable=self.txt_search,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,sticky=W)
        
        search_btn=Button(SEARCH_fram,command=self.Search,text="Search",font=("times new roman",11,"bold"),width=12,bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn=Button(SEARCH_fram,command=self.fetch_data,text="ShowAll",font=("times new roman",11,"bold"),width=12,bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
        
        
        # ==============================table frame==================
        table_fram=Frame(Right_fram,bd=2,bg="white",relief=RIDGE)
        table_fram.place(x=5,y=210,width=710,height=350)
        
        Scroll_x=ttk.Scrollbar(table_fram,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_fram,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_fram,columns=("role","dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","Nationality","photo"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("role",text="UserType")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("Nationality",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("role",width=150)
        self.student_table.column("dep",width=150)
        self.student_table.column("course",width=150)
        self.student_table.column("year",width=150)
        self.student_table.column("sem",width=150)
        self.student_table.column("id",width=150)
        self.student_table.column("name",width=150)
        self.student_table.column("div",width=150)
        self.student_table.column("roll",width=150)
        self.student_table.column("gender",width=150)
        self.student_table.column("dob",width=150)
        self.student_table.column("email",width=150)
        self.student_table.column("phone",width=150)
        self.student_table.column("address",width=150)
        self.student_table.column("Nationality",width=150)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    def Categories(self,event=""):
        if self.Faculty_combo.get()=="Faculty":
            self.dep_combo.config(value=self.subFaculty1)
            self.dep_combo.current(0)
            self.course_combo.config(value=self.subFaculty2)
            self.course_combo.current(0)
            self.year_combo.config(value=self.subFaculty3)
            self.year_combo.current(0)
            self.sem_combo.config(value=self.subFaculty4)
            self.sem_combo.current(0)
            
        if self.Faculty_combo.get()=="Student":
            self.dep_combo.config(value=self.subStud1)
            self.dep_combo.current(0)
            self.course_combo.config(value=self.subStud2)
            self.course_combo.current(0)
            self.year_combo.config(value=self.subStud3)
            self.year_combo.current(0)
            self.sem_combo.config(value=self.subStud4)
           
            self.sem_combo.current(0)
        
    # ==========================function declaretion=============

    def validate_email(self,email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email)
    
    def validate_phone(self,phone):
        pattern = r"^\d{10}$"  # Allows only 10-digit numbers
        return re.match(pattern, phone)
    
    def add_data(self):
        # Check for empty fields
        if (
            self.var_dep.get() == "Select Department" 
            or self.var_studnam.get() == "" 
            or self.var_studid.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
    
        # Validate Email
        if not self.validate_email(self.var_email.get()):
            messagebox.showerror("Error", "Invalid Email Format", parent=self.root)
            return
    
        # Validate Phone Number
        if not self.validate_phone(self.var_phone.get()):
            messagebox.showerror("Error", "Phone number must be 10 digits", parent=self.root)
            return
    
        try:
            # Connect to the database
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="sumit@123",
                database="facerecognizer"
            )
            my_cursor = conn.cursor()
    
            # Insert query using parameterized queries
            query = """
                INSERT INTO stud_attend 
                (UserType, Dep, course, Year, Semester, Student_id, Name, Division, Roll, Gender, Dob, Email, Phone, Address, Teacher, PhotoSample) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                self.var_role.get(),
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_studid.get(),
                self.var_studnam.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
            )
    
            # Execute query
            my_cursor.execute(query, values)
            conn.commit()
    
            # Fetch updated data
            self.fetch_data()
    
            # Close connection
            conn.close()
    
            messagebox.showinfo("Success", "Data saved successfully", parent=self.root)
    
        except mysql.connector.Error as db_err:
            messagebox.showerror("Database Error", f"Database Issue: {str(db_err)}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Unexpected Error: {str(es)}", parent=self.root)

    # def add_data(self):
    #     if self.var_dep.get()=="Select Department" or self.var_studnam.get()==""or self.var_studid.get()=="":
    #         messagebox.showerror("Error","All Field are required",parent=self.root)
    #     else:
    #         try:
    #             conn=mysql.connector.connect(host="localhost",username="root",password="sumit@123",database="facerecognizer")
    #             my_cursor=conn.cursor()
    #             my_cursor.execute("insert into stud_attend values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
    #                                                                             self.var_role.get(),
    #                                                                             self.var_dep.get(),
    #                                                                             self.var_course.get(),
    #                                                                             self.var_year.get(),
    #                                                                             self.var_sem.get(),
    #                                                                             self.var_studid.get(),
    #                                                                             self.var_studnam.get(),
    #                                                                             self.var_div.get(),
    #                                                                             self.var_roll.get(),
    #                                                                             self.var_gender.get(),
    #                                                                             self.var_dob.get(),
    #                                                                             self.var_email.get(),
    #                                                                             self.var_phone.get(),
    #                                                                             self.var_address.get(),
    #                                                                             self.var_teacher.get(),
    #                                                                             self.var_radio1.get()
                                                                            
                    
    #                                                                                         ))
    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()
    #             messagebox.showinfo("success","Data saved successfully",parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
                # =====================fetch data =====================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sumit@123",database="facerecognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from stud_attend")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()        
            
            
        # =====================get Cursor========================
    def get_cursor(self,event=""):
    
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_role.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_course.set(data[2]),
        self.var_year.set(data[3]),
        self.var_sem.set(data[4]),
        self.var_studid.set(data[5]),
        self.var_studnam.set(data[6]),
        self.var_div.set(data[7]),
        self.var_roll.set(data[8]),
        self.var_gender.set(data[9]),
        self.var_dob.set(data[10]),
        self.var_email.set(data[11]),
        self.var_phone.set(data[12]),
        self.var_address.set(data[13]),
        self.var_teacher.set(data[14]),
        self.var_radio1.set(data[15])
        # except Exception as es:
            #    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)         
                     
        # ================update ===============
    
    def update_data(self):
    
        # Check if required fields are empty
        if (
            self.var_dep.get() == "Select Department" 
            or self.var_studnam.get() == "" 
            or self.var_studid.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        # Validate Email
        if not self.validate_email(self.var_email.get()):
            messagebox.showerror("Error", "Invalid Email Format", parent=self.root)
            return

        # Validate Phone Number
        if not self.validate_phone(self.var_phone.get()):
            messagebox.showerror("Error", "Phone number must be 10 digits", parent=self.root)
            return

        # Ask for confirmation
        Updated = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)

        if not Updated:  # If user selects "No"
            return

        try:
            # Connect to the database
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="sumit@123",
                database="facerecognizer"
            )
            my_cursor = conn.cursor()

            # Update Query
            query = """
                UPDATE stud_attend 
                SET UserType=%s, Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, 
                    Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, 
                    Address=%s, Teacher=%s, PhotoSample=%s 
                WHERE Student_id=%s
            """
            values = (
                self.var_role.get(),
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_studnam.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get(),
                self.var_studid.get()
            )

            # Execute Query
            my_cursor.execute(query, values)
            conn.commit()

            # Success Message
            messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)

            # Refresh Data
            self.fetch_data()

        except mysql.connector.Error as db_err:
            messagebox.showerror("Database Error", f"Database Issue: {str(db_err)}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Unexpected Error: {str(es)}", parent=self.root)
        finally:
            conn.close()             
                # ============deletete fuN============
    def delete_data(self):
        if self.var_studid.get()=="":
            messagebox.showerror("Error","Student id must required",parent=self.root)
        else:
            try:
                delet=messagebox.askyesno("student Delete Page", "Do you want to delete this student ",parent=self.root) 
                if delet>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sumit@123",database="facerecognizer")
                    my_cursor=conn.cursor()
                    sql="delete from stud_attend where Student_id=%s"
                    val=(self.var_studid.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()   
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)         
            
    # =======================reset======================
    
    def reset_data(self):
        self.var_role.set("Select Role")
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
    
        x=random.randint(1000,9999)
        self.var_studid.set(str(x))
        
        self.var_studnam.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    # ======================update phorotoaosmappel=========================
    
    def update_photo_sample(self):
        if self.var_studid.get() == "":
            messagebox.showerror("Error", "Student ID is required to update the photo sample.", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="sumit@123", database="facerecognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM stud_attend WHERE Student_id = %s", (self.var_studid.get(),))
            record = my_cursor.fetchone()
            if record is None:
                messagebox.showerror("Error", "Student ID not found in the database.", parent=self.root)
                return
            
            # Load predefined data on face frontals from OpenCV
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    face_cropped = img[y:y + h, x:x + w]
                    return face_cropped

            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if face_cropped(my_frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped(my_frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = f"data/user.{self.var_studid.get()}.{img_id}.jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)

                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()

            messagebox.showinfo("Success", "Photo sample updated successfully!", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

        finally:
            conn.close()
    
    def Search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sumit@123",database="facerecognizer")
        my_cursor=conn.cursor()
        
        my_cursor.execute("select * from stud_attend where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in rows:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    
        # ===================== generate data set or take photo sample=========
    
    
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_studnam.get()==""or self.var_studid.get()=="":
            messagebox.showerror("Error","All Field are required",parent=self.root)
        else:
            
            # Updated=messagebox.askyesno("Update","Do you want to update this Photo",parent=self.root)
            # if Updated>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="sumit@123",database="facerecognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from stud_attend")
            myresult=my_cursor.fetchall()
            id=0
            for x in myresult:
                id+=1
            my_cursor.execute("update stud_attend set UserType=%s,Dep=%s,course=%s, Year=%s, Semester=%s,Name=%s ,Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                
                                                                                                                                                                                                        self.var_role.get(),
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                                        self.var_studnam.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_studid.get()==id+1
                                                                                                                                                                                                            ))
            
        conn.commit()
        self.fetch_data()
        self.reset_data()
        conn.close()
            
        # ==========================================load predefined data on face Frontals from opencv========
        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
         
        def face_cropped(img):
            
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_classifier.detectMultiScale(gray,1.3,5)
            #scaling factor=1.3
            #Minimum Neighbour=5
            for (x,y,w,h) in faces:
                face_cropped=img[y:y+h,x:x+w]
                return face_cropped
        cap=cv2.VideoCapture(0)
        img_id=0
        while True:
            ret,my_frame=cap.read()
            if face_cropped(my_frame)is not None:
                img_id+=1
                face=cv2.resize(face_cropped(my_frame),(450,450))
                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                cv2.imwrite(file_name_path,face)
                cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                cv2.imshow("crooped Face",face)
                
            if cv2.waitKey(1)==13 or int(img_id)==100:
                break
        cap.release()
        cv2.destroyAllWindows()
            
        messagebox.showinfo("Result","generating data sets completed!!!!!",parent=self.root)
        # except Exception as es:
        #    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)         
                    
                    
            
        

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
    
    # remove system word from project