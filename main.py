# from tkinter import*
# from tkinter import ttk
# import tkinter
# from PIL import Image,ImageTk
# from tkinter import messagebox
# from student import Student
# from train import Train
# from face_recognition import Face_Recognition
# from Attendance import Attendance
# from develop import Developer
# from time import strftime
# from datetime import datetime
# from chatbot import chatBot
# import os



# class Facial_Attendance:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Attendance Software")
    
#     # images 
       
#         img=Image.open("college_images/Stanford.jpg")
#         img= img.resize((500,130),Image.Resampling.NEAREST)
#         self.photoimg = ImageTk.PhotoImage(img)
#         PhotoLabel=Label(self.root,image=self.photoimg)
#         PhotoLabel.place(x=0,y=0,width=500,height=130)
        
#         img1=Image.open("college_images/facialrecognition.png")
#         img1= img1.resize((500,130),Image.Resampling.NEAREST)
#         self.photoimg1 = ImageTk.PhotoImage(img1)
#         PhotoLabel2=Label(self.root,image=self.photoimg1)
#         PhotoLabel2.place(x=500,y=0,width=500,height=130)
        
#         img2=Image.open("college_images/u.jpg")
#         img2= img2.resize((500,130),Image.Resampling.NEAREST)
#         self.photoimg2 = ImageTk.PhotoImage(img2)
#         PhotoLabel3=Label(self.root,image=self.photoimg2)
#         PhotoLabel3.place(x=1000,y=0,width=550,height=130)
    
#     # bg image
    
#         img3=Image.open("college_images/6.jpg")
#         img3= img3.resize((1530,710),Image.Resampling.NEAREST)
#         self.photoimg3 = ImageTk.PhotoImage(img3)
#         bgLabel=Label(self.root,image=self.photoimg3)
#         bgLabel.place(x=0,y=130,width=1530,height=710)
        
#         title_lbl=Label(bgLabel,text="FACE RECOGNITION ATTENDANCE SOFTWARE",font=("times new roman",34,"bold"),bg="white",fg="red")
#         title_lbl.place(x=0,y=0,width=1530,height=45)
        
#         # =============TimeoutError
#         def time():
#             string = strftime('%H:%M:%S %p')
#             lbl.config(text = string)
#             lbl.after(1000, time)

#         lbl = Label(title_lbl, font = ('times new roman', 14, 'bold'), background = 'white', foreground = 'blue')
#         lbl.place(x=0,y=0,width=110,height=50)
#         time()
        
        
#     # student button
#         img4=Image.open("college_images/bg.jpg")
#         img4= img4.resize((220,220),Image.Resampling.NEAREST)
#         self.photoimg4 = ImageTk.PhotoImage(img4)
        
         
#         b1=Button(bgLabel,image=self.photoimg4,command=self.student_details,cursor="hand2")
#         b1.place(x=200,y=100,width=220,height=220)
#         b11=Button(bgLabel,command=self.student_details,text="USER DETAILS",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b11.place(x=200,y=300,width=220,height=40)
      
    
#     # detect face button
#         img5=Image.open("college_images/face_detector1.jpg")
#         img5= img5.resize((220,220),Image.Resampling.NEAREST)
#         self.photoimg5 = ImageTk.PhotoImage(img5)
        
         
#         b2=Button(bgLabel,image=self.photoimg5,cursor="hand2",command=self.Face_reg)
#         b2.place(x=500,y=100,width=220,height=220)
#         b21=Button(bgLabel,text="FACE DETAILS",cursor="hand2",command=self.Face_reg,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b21.place(x=500,y=300,width=220,height=40)
        
        
#     # Attendance button
#         img6=Image.open("college_images/report.jpg")
#         img6= img6.resize((220,220),Image.Resampling.NEAREST)
#         self.photoimg6 = ImageTk.PhotoImage(img6)
        
         
#         b3=Button(bgLabel,image=self.photoimg6,cursor="hand2",command=self.Attenda_reg)
#         b3.place(x=800,y=100,width=220,height=220)
#         b31=Button(bgLabel,text="ATTENDANCE",cursor="hand2",command=self.Attenda_reg,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b31.place(x=800,y=300,width=220,height=40)
      
#     # CHat bot deck button
#         img7=Image.open("college_images/chat.jpg")
#         img7= img7.resize((220,220),Image.Resampling.NEAREST)
#         self.photoimg7 = ImageTk.PhotoImage(img7)
        
         
#         b3=Button(bgLabel,image=self.photoimg7,cursor="hand2",command=self.Chatboot)
#         b3.place(x=1100,y=100,width=220,height=220)
#         b31=Button(bgLabel,text="MAY I HELP YOU",cursor="hand2",command=self.Chatboot,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b31.place(x=1100,y=300,width=220,height=40)
      
    
#     # Train face button
#         img8=Image.open("college_images/Train.jpg")
#         img8= img8.resize((220,220),Image.Resampling.NEAREST)
#         self.photoimg8 = ImageTk.PhotoImage(img8)
        
         
#         b31=Button(bgLabel,image=self.photoimg8,cursor="hand2",command=self.Train_data)
#         b31.place(x=200,y=380,width=220,height=220)
#         b32=Button(bgLabel,text=" TRAIN DATA",cursor="hand2",command=self.Train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b32.place(x=200,y=580,width=220,height=40)
      
    
    
#     # photos button
#         img9=Image.open("college_images/Photo.jpg")
#         img9= img9.resize((220,220),Image.Resampling.NEAREST)
#         self.photoimg9 = ImageTk.PhotoImage(img9)
        
        
#         b3=Button(bgLabel,image=self.photoimg9,cursor="hand2",command=self.open_img)
#         b3.place(x=500,y=380,width=220,height=220)
#         b31=Button(bgLabel,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b31.place(x=500,y=580,width=220,height=40)
      
    
    
#     # Developer button
#         img10=Image.open("college_images/deve.jpg")
#         img10= img10.resize((220,220),Image.Resampling.NEAREST)
#         self.photoimg10 = ImageTk.PhotoImage(img10)
        
         
#         b3=Button(bgLabel,image=self.photoimg10,cursor="hand2",command=self.Developer)
#         b3.place(x=800,y=380,width=220,height=220)
#         b31=Button(bgLabel,text=" DEVELOPER",cursor="hand2",command=self.Developer,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b31.place(x=800,y=580,width=220,height=40)
      
    
    
#     #  Exit face button
#         img11=Image.open("college_images/exit.jpg")
#         img11= img11.resize((220,220),Image.Resampling.NEAREST)
#         self.photoimg11 = ImageTk.PhotoImage(img11)


#         b3=Button(bgLabel,image=self.photoimg11,cursor="hand2",command=self.exit)
#         b3.place(x=1100,y=380,width=220,height=220)
#         b31=Button(bgLabel,text="EXIT",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b31.place(x=1100,y=580,width=220,height=40)
        
        
#         # =====================function btns=================
#     def open_img(self):
#         os.startfile("data")  
        
#     def exit(self):
#         self.root.destroy()
        
#     def student_details(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Student(self.new_window)
      
#     def Train_data(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Train(self.new_window)
      
#     def Face_reg(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Face_Recognition(self.new_window)
      
#     def Attenda_reg(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Attendance(self.new_window)
      
#     def Developer(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Developer(self.new_window)
      
      
#     def Chatboot(self):
#         self.new_window=Toplevel(self.root)
#         self.app=chatBot(self.new_window)
      
    
          
    
        
       
       
       
       
       
       
       
       
       
       
       
        
        
        
# if __name__=="__main__":
#     root=Tk()
#     obj=Facial_Attendance(root)
#     root.mainloop()
