import random
import mysql.connector
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
from student import Student
from train import Train
from face_recognition import Face_Recognition
from Attendance import Attendance
from develop import Developer
from time import strftime
from datetime import datetime 
from chatbot import chatBot

import os


def mainw():
    win=Tk()
    app=Login_Windows(win)
    win.mainloop()


class Login_Windows:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        # self.root.wm_iconbitmap("")
        
        
        
         # =================================varibles======================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        
        
        self.bg=ImageTk.PhotoImage(file="college_images/10803215.jpg")
    
        lblimg1=Label(self.root,image=self.bg,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        # self.bg=ImageTk.PhotoImage(file=r"C:\Users\dell\OneDrive\Desktop\Login_form\Images\HotelBGcollege_images/Stanford.jpgng")  
        
        # lbl_bg=Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        # ======
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1 = Image.open("college_images/LoginIconAppl.png")
        img1= img1.resize((100,100),Image.Resampling.LANCZOS )
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
              
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        Password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        Password.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        #==========Icon Images===============
        img2=Image.open("college_images/login2.jpeg")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)     
        
        
        img3=Image.open("college_images/lock-512.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=393,width=25,height=25)      
        
       # LoginButton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),borderwidth=3,bd=3,fg="white",bg="red",activeforeground="white",activebackground="red",relief=RAISED)
        loginbtn.place(x=110,y=300,width=120,height=35)
        
       # registerButton
        loginbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=15,y=360,width=160)
        
        # forgetpassButton 
        loginbtn=Button(frame,text="Forget Password ",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=10,y=385,width=160)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window) 
        
        
    def login(self):
        if self.txtuser.get()==" "or self.txtpass.get()==" ":
            messagebox.showerror("Error","all fields required")
        elif self.txtuser.get()=="Chikku" and self.txtpass.get()=="Anu":
            messagebox.showinfo("Sucess","Welcome to Facial Attendance Software,Have a great day")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="sumit@123",database="newtable")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.var_email.get(),
                                                                                        self.var_pass.get()
                                                                                ))
                
            row=my_cursor.fetchone()
        if row==None:
            messagebox.showerror("Error","Invalid Username & Password")
        else:
            open_main=messagebox.askyesno("YesNo","Access only admin")
            if open_main>0:
                self.new_window=Toplevel(self.root)
                self.app=Facial_Attendance(self.new_window)
                self.reData()
        
                
            else:
                if not open_main:
                    return
                conn.commit()
                conn.close()
                
    def reData(self):
        self.var_email.set("")
        
        self.var_pass.set("")
# ===================reset password==============================================
    def reset_pass(self):
        if self.combo_security_q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else: 
            conn=mysql.connector.connect(host="localhost",user="root",password="sumit@123",database="newtable")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_q.get(),self.txt_security.get())
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,please login new password",parent=self.root2)
                self.root2.destroy()
            
                        
                
     # ==================================forgot password window====================================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="sumit@123",database="newtable")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
               
            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")  
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("comic sans ms",15,"bold"),fg="white",bg="black")
                l.place(x=0,y=10,relwidth=1)
                
                security_q=Label(self.root2,text="Select Security Questions",font=("comic sans ms",15,"bold"),bg="tan",fg="black")
                security_q.place(x=50,y=80)
                
                self.combo_security_q=ttk.Combobox(self.root2,font=("comic sans ms",15,"bold"),state="readonly")
                self.combo_security_q["values"]=("Select","Your Birth Place","Your School name","Your BestFriend name")
                
                self.combo_security_q.place(x=50,y=110,width=250)
                self.combo_security_q.current(0)


                security_a=Label(self.root2,text="Security Answer",font=("comic sans ms",15,"bold"),bg="tan",fg="black")
                security_a.place(x=50,y=150)
                self.txt_security=ttk.Entry(self.root2,font=("comic sans ms",15))
                self.txt_security.place(x=50,y=180,width=250)
                             
                new_pass=Label(self.root2,text="New Password",font=("comic sans ms",15,"bold"),bg="tan",fg="black")
                new_pass.place(x=50,y=220)


                self.txt_newpass=ttk.Entry(self.root2,font=("comic sans ms",15))
                self.txt_newpass.place(x=50,y=250,width=250)
                        
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("comic sans ms",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)
                        
                # btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("comic sans ms",15,"bold"),fg="white",bg="green")
                # btn.place(x=100,y=290)   

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x800+0+0")

       # =================================varibles======================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


         # ===============bg image================
        self.bg=ImageTk.PhotoImage(file="college_images/6.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

       
         # ===============left image================
        leftframe=Frame(self.root,bg="white")
        leftframe.place(x=50,y=100,width=470,height=550)
        
        bg1=Image.open("college_images/password.jpg")
        bg1=bg1.resize((470,550),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(bg1)
        
        left_lbl=Label(leftframe,image=self.photoimage2,bd=0,relief=RIDGE)
        left_lbl.place(x=0,y=0,width=470,height=550)

         # =============main frame============
        frame=Frame(self.root,bg="#fff")
        frame.place(x=520,y=100,width=800,height=550)
        
          
        # bg3=Image.open("college_images/bg1.jpg")
        # bg3=bg3.resize((800,550),Image.Resampling.LANCZOS)
        # self.photoimage5=ImageTk.PhotoImage(bg3)
        # left_lbl=Label(frame,image=self.photoimage5,bd=0,relief=RIDGE)
        # left_lbl.place(x=0,y=0,width=800,height=550)
        
        Register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",25,"bold"),fg="DARK BLUE",bg="#fff")
        Register_lbl.place(x=30,y=20)

         #===================label and entry====================

         # -------------------row1 
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="white",bg="#008080")
        fname.place(x=50,y=100)
       
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="white",bg="#008080")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        # -----------------row2

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="white",bg="#008080")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="UserName",font=("times new roman",15,"bold"),fg="white",bg="#008080")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

     
         # -----------------row3

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),fg="white",bg="#008080") 
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your School name","Your BestFriend name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)



        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="white",bg="#008080")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

         # --------------------row4
        
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="#008080")
        password.place(x=50,y=310)

        self.txt_password=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_password.place(x=50,y=340,width=250)

        confirm_password=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="white",bg="#008080")
        confirm_password.place(x=370,y=310)

        self.txt_confirm_password=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_password.place(x=370,y=340,width=250)

         # =====================checkbutton=================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms and Conditions",font=("times new roman",12,"bold"),bg="dark grey",onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

         # ==================buttons===================
        img=Image.open("college_images/ref.webp")
        img=img.resize((200,50),Image.Resampling.LANCZOS)
        
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand1",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=50,y=422,width=200)

        img1=Image.open("college_images/back.jpeg")
        img1=img1.resize((200,50),Image.Resampling.LANCZOS)
     
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",14,"bold"))
        b1.place(x=330,y=422,width=190)


   # ======================Function declarition=========================    
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password and confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our term and conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="sumit@123",database="newtable")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                     self.var_fname.get(),
                                                                                         self.var_lname.get(),
                                                                                         self.var_contact.get(),
                                                                                         self.var_email.get(),
                                                                                         self.var_securityQ.get(),
                                                                                         self.var_securityA.get(),
                                                                                         self.var_pass.get()
                                                                                         
                                                                                       ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucess","Registered Sucessfully",parent=self.root) 
            self.root.destroy()
               
    def return_login(self):
        self.root.destroy()         







class Facial_Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Software")
    
    # images 
       
        img=Image.open("college_images/Stanford.jpg")
        img= img.resize((500,130),Image.Resampling.NEAREST)
        self.photoimg = ImageTk.PhotoImage(img)
        PhotoLabel=Label(self.root,image=self.photoimg)
        PhotoLabel.place(x=0,y=0,width=500,height=130)
        
        img1=Image.open("college_images/facialrecognition.png")
        img1= img1.resize((500,130),Image.Resampling.NEAREST)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        PhotoLabel2=Label(self.root,image=self.photoimg1)
        PhotoLabel2.place(x=500,y=0,width=500,height=130)
        
        img2=Image.open("college_images/u.jpg")
        img2= img2.resize((500,130),Image.Resampling.NEAREST)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        PhotoLabel3=Label(self.root,image=self.photoimg2)
        PhotoLabel3.place(x=1000,y=0,width=550,height=130)
    
    # bg image
    
        img3=Image.open("college_images/6.jpg")
        img3= img3.resize((1530,710),Image.Resampling.NEAREST)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bgLabel=Label(self.root,image=self.photoimg3)
        bgLabel.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bgLabel,text="FACE RECOGNITION ATTENDANCE SOFTWARE",font=("times new roman",34,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # =============TimeoutError
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font = ('times new roman', 14, 'bold'), background = 'white', foreground = 'blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        
    # student button
        img4=Image.open("college_images/7103025.jpg                                                             ")
        img4= img4.resize((220,220),Image.Resampling.NEAREST)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
         
        b1=Button(bgLabel,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        b11=Button(bgLabel,command=self.student_details,text="USER DETAILS",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b11.place(x=200,y=300,width=220,height=40)
      
    
    # detect face button
        img5=Image.open("college_images/face_detector1.jpg")
        img5= img5.resize((220,220),Image.Resampling.NEAREST)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
         
        b2=Button(bgLabel,image=self.photoimg5,cursor="hand2",command=self.Face_reg)
        b2.place(x=500,y=100,width=220,height=220)
        b21=Button(bgLabel,text="FACE DETAILS",cursor="hand2",command=self.Face_reg,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b21.place(x=500,y=300,width=220,height=40)
        
        
    # Attendance button
        img6=Image.open("college_images/Att.jpg")
        img6= img6.resize((220,220),Image.Resampling.NEAREST)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
         
        b3=Button(bgLabel,image=self.photoimg6,cursor="hand2",command=self.Attenda_reg)
        b3.place(x=800,y=100,width=220,height=220)
        b31=Button(bgLabel,text="ATTENDANCE",cursor="hand2",command=self.Attenda_reg,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b31.place(x=800,y=300,width=220,height=40)
      
    # CHat bot deck button
        img7=Image.open("college_images/chat.jpg")
        img7= img7.resize((220,220),Image.Resampling.NEAREST)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
         
        b3=Button(bgLabel,image=self.photoimg7,cursor="hand2",command=self.Chatboot)
        b3.place(x=1100,y=100,width=220,height=220)
        b31=Button(bgLabel,text="MAY I HELP YOU",cursor="hand2",command=self.Chatboot,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b31.place(x=1100,y=300,width=220,height=40)
      
    
    # Train face button
        img8=Image.open("college_images/Train.jpg")
        img8= img8.resize((220,220),Image.Resampling.NEAREST)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
         
        b31=Button(bgLabel,image=self.photoimg8,cursor="hand2",command=self.Train_data)
        b31.place(x=200,y=380,width=220,height=220)
        b32=Button(bgLabel,text=" TRAIN DATA",cursor="hand2",command=self.Train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b32.place(x=200,y=580,width=220,height=40)
      
    
    
    # photos button
        img9=Image.open("college_images/1398829.jpg")
        img9= img9.resize((220,220),Image.Resampling.NEAREST)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        
        b3=Button(bgLabel,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b3.place(x=500,y=380,width=220,height=220)
        b31=Button(bgLabel,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b31.place(x=500,y=580,width=220,height=40)
      
    
    
    # Developer button
        img10=Image.open("college_images/deve.jpg")
        img10= img10.resize((220,220),Image.Resampling.NEAREST)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
         
        b3=Button(bgLabel,image=self.photoimg10,cursor="hand2",command=self.Developer)
        b3.place(x=800,y=380,width=220,height=220)
        b31=Button(bgLabel,text=" DEVELOPER",cursor="hand2",command=self.Developer,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b31.place(x=800,y=580,width=220,height=40)
      
    
    
    #  Exit face button
        img11=Image.open("college_images/exit.jpg")
        img11= img11.resize((220,220),Image.Resampling.NEAREST)
        self.photoimg11 = ImageTk.PhotoImage(img11)


        b3=Button(bgLabel,image=self.photoimg11,cursor="hand2",command=self.exit)
        b3.place(x=1100,y=380,width=220,height=220)
        b31=Button(bgLabel,text="EXIT",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b31.place(x=1100,y=580,width=220,height=40)
        
        
        # =====================function btns=================
    def open_img(self):
        os.startfile("data")  
        
    def exit(self):
        self.root.destroy()
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
      
    def Train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
      
    def Face_reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
      
    def Attenda_reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
      
    def Developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
      
      
    def Chatboot(self):
        self.new_window=Toplevel(self.root)
        self.app=chatBot(self.new_window)
      
    
          
    
        
       
       
       
       
       
       
       
       
       
       
       
        
        
       
       
       
       
       
    
                      
if __name__=="__main__":
    
    mainw()
    