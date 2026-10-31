import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Dell\AppData\Local\Programs\Python\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Dell\AppData\Local\Programs\Python\Python312\tcl\tk8.6"

executables = [cx_Freeze.Executable("Login.py", base=base, icon="facial_recognition_icon.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["facial_recognition_icon.ico",'tcl86t.dll','tk86t.dll', 'college_images','data','AttendanceSheet']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace Software | Developed By Swasthik and Sumit",
    executables = executables
    )