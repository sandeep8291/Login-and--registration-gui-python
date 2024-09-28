from tkinter import *
from tkinter import messagebox
#login button action
def login():
    if usernameE.get()=='' or  passwordE=='':
        messagebox.showerror('Error','your feilds are empty')

    else:
        messagebox.showinfo('Sucsses,Wellcome')
            
def reg():
    messagebox.showinfo("Registration page")
    
    window.destroy()
    import registr

#window
window=Tk()

window.geometry('1280x700+0+0')
window.title('Login page')
window.resizable(False,False)

#bg
bi=PhotoImage(file='bg.png')

bglabel=Label(window,image=bi)
bglabel.place(x=0,y=0)

#login frame
loginFrame=Frame(window,bg ='white')

loginFrame.place(x=400,y=150)

logoi=PhotoImage(file='l.png')

logo=Label(loginFrame,image=logoi,bg='white')
logo.grid(row=0,column=0,columnspan=2,pady=10)


#username lable and entry
usernamei=PhotoImage(file='user.png')

userName=Label(loginFrame,image=usernamei,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
userName.grid(row=1,column=0,pady=10,padx=30)

usernameE=Entry(loginFrame,font=('times new roman',20),bd=5,fg='gray')
usernameE.grid(row=1,column=1,pady=10,padx=30)


#passwor lable and entry
passwi=PhotoImage(file='password.png')

password=Label(loginFrame,image=passwi,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
password.grid(row=2,column=0,pady=10,padx=30)

passwordE=Entry(loginFrame,font=('times new roman',20),bd=5,fg='gray')
passwordE.grid(row=2,column=1,pady=10,padx=30)


#login button

login=Button(loginFrame,text='Login',font=('times new roman',14,'bold'),fg='white',bg='black',width=15,cursor='hand2',command=login)
login.grid(row=3,column=1,pady=10)

#registration button
reg=Button(loginFrame,text='Register',font=('italic',14,'bold'),fg='black',bg='white',cursor='hand2',command=reg)
reg.grid(row=4)




window.mainloop()