from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os


root=Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
	username=user.get()
	password=code.get()
	#instead If else API to verify user if successful run below if condition
	if username=='admin' and password=='123456':
		screen=Toplevel(root)
		screen.title("File Upload and View")
		screen.geometry('925x500+300+200')
		screen.config(bg="white")
     
		def upload_file():
			filename = filedialog.askopenfilename()
			if filename:
				# Copy the file to the uploads directory (if needed)
				destination = os.path.join('uploads', os.path.basename(filename))
				os.makedirs('uploads', exist_ok=True)
				if not os.path.exists(destination):
					os.rename(filename, destination)


		def view_file():
			filename = filedialog.askopenfilename(initialdir='uploads')
			if filename:
				# Open the file for viewing (you can customize this part)
				os.system(f'notepad.exe {filename}')
   
		#root = tk.Tk()
		#root.title("File Upload and View")

		upload_button = tk.Button(screen, text="Upload File", command=upload_file)
		upload_button.pack(pady=10)

		view_button = tk.Button(screen, text="View File", command=view_file)
		view_button.pack(pady=10)

	elif username!='admin'or password!='123456':
		messagebox.showerror("Invalid","invalid username or password")

def signup():
	def usersignup() :
		username=user.get()
		password=code.get()

		#API to add user in DB

		messagebox.showinfo("Successful","Sign Up Successfully")
		SignupScreen.destroy()


	SignupScreen=Toplevel(root)
	SignupScreen.title("Sign Up")
	SignupScreen.geometry('925x500+300+200')
	SignupScreen.configure(bg="#fff")
	SignupScreen.resizable(False,False)

	#img1=PhotoImage(file='login.png')
	Label(SignupScreen,image=img,bg='white').place(x=50,y=50)

	SignupFrame=Frame(SignupScreen,width=350,height=350,bg="white")
	SignupFrame.place(x=480,y=70)

	SignupHeading=Label(SignupFrame,text='sign up',fg='#57a1f8',bg='white',font=('microsoft YaHei UI Light',23,'bold'))
	SignupHeading.place(x=100,y=5)

	def on_enter(e):
		user.delete(0,'end')

	def on_leave(e):
		name=user.get()
		if name==' ':
			user.insert(0,'username')
	user=Entry(SignupFrame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
	user.place(x=30,y=80)
	user.insert(0,'username')
	user.bind('<FocusIn>',on_enter)
	user.bind('<FocusOut>',on_leave)

	Frame(SignupFrame,width=295,height=2,bg='black').place(x=25,y=107)

	def on_enter(e):
		code.delete(0,'end')

	def on_leave(e):
		name=code.get()
		if name==' ':
			code.insert(0,'password')

	code=Entry(SignupFrame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
	code.place(x=30,y=150)
	code.insert(0,'password')
	code.bind('<FocusIn>',on_enter)
	code.bind('<FocusOut>',on_leave)

	Frame(SignupFrame,width=295,height=2,bg='black').place(x=25,y=177)

	Button(SignupFrame,width=39,pady=7,text='sign up',bg='#57a1f8',fg='white',border=0,command=usersignup).place(x=35,y=204)



img=PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='sign in',fg='#57a1f8',bg='white',font=('microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)


def on_enter(e):
	user.delete(0,'end')

def on_leave(e):
	name=user.get()
	if name==' ':
		user.insert(0,'username')
user=Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
	code.delete(0,'end')

def on_leave(e):
	name=code.get()
	if name==' ':
		code.insert(0,'password')

code=Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

Button(frame,width=39,pady=7,text='sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('microsoft YaHei UI Light',9))
label.place(x=75,y=270)


sign_up=Button(frame,width=6,text='sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8', command=signup)
sign_up.place(x=215,y=270)










root.mainloop()