from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import login
import pymysql


def c_db():
    if emailE.get()=='' or usernameE.get()=='' or fullnameE.get()=='' or emailE.get()=='' or contactE.get()=='':
        messagebox.showerror('All feilds are required')





window=Tk()

window.geometry('1280x700+0+0')
window.title('Registration page')
window.resizable(False,False)

bi=PhotoImage(file='bg.png')

bglabel=Label(window,image=bi)
bglabel.place(x=0,y=0)

rFrame=Frame(window,bg ='white')

rFrame.place(x=400,y=60)

regi=PhotoImage(file='reg.png')
regl=Label(rFrame,image=regi,text='Registration',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
regl.grid(row=0,column=0,columnspan=2,pady=10,padx=30)


fullname = Label(rFrame,text="Full Name",compound=LEFT,font=('times new roman',20,'bold'),bg='white')
fullname.grid(row=1,column=0,pady=10)

username = Label(rFrame,text="Username",compound=LEFT,font=('times new roman',20,'bold'),bg='white')
username.grid(row=2,column=0,pady=10)

email = Label(rFrame,text="Email",compound=LEFT,font=('times new roman',20,'bold'),bg='white')
email.grid(row=3,column=0,pady=10)

contact = Label(rFrame,text="Contact",compound=LEFT,font=('times new roman',20,'bold'),bg='white')
contact.grid(row=4,column=0,pady=10)

password = Label(rFrame,text="Password",compound=LEFT,font=('times new roman',20,'bold'),bg='white')
password.grid(row=5,column=0,pady=10)

gender = Label(rFrame,text="Gender",compound=LEFT,font=('times new roman',20,'bold'),bg='white')
gender.grid(row=6,column=0,pady=10)


fullnameE=Entry(rFrame,font=('times new roman',20),bd=5,fg='gray')
fullnameE.grid(row=1,column=1,pady=10,padx=30)

usernameE=Entry(rFrame,font=('times new roman',20),bd=5,fg='gray')
usernameE.grid(row=2,column=1,pady=10,padx=30)

emailE=Entry(rFrame,font=('times new roman',20),bd=5,fg='gray')
emailE.grid(row=3,column=1,pady=10,padx=30)


contactE=Entry(rFrame,font=('times new roman',20),bd=5,fg='gray')
contactE.grid(row=4,column=1,pady=10,padx=30)


passwordE=Entry(rFrame,font=('times new roman',20),bd=5,fg='gray')
passwordE.grid(row=5,column=1,pady=10,padx=30)

genderE=Entry(rFrame,font=('times new roman',20),bd=5,fg='gray')
genderE.grid(row=6,column=1,pady=10,padx=30)


ok=Button(rFrame,text='Get started',font=('times new roman',14,'bold'),fg='white',bg='black',width=20,cursor='hand2',command=c_db)
ok.grid(row=7,column=1,pady=10)










window.mainloop()