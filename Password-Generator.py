from tkinter import*
from tkinter import messagebox
tk=Tk()
tk.title("Login Form")
tk.geometry("300x300")
tk.resizable(True,True)
tk.configure(bg="blue")
def login():
    username=t1.get()
    password=t2.get()
    if(username=="" and password==""):
        messagebox.showerror("Error","You have to fill the form")
    elif(username=="shivansh" and password=="COER"):
        messagebox.showinfo("Done","Login Successful")
    else:
        messagebox.showerror("Error","Login fail pl enter the correct details")


Label(tk, text="Login here", font="impact 20 bold", bg="black", fg="White").pack()
Label(tk, text="username").place(x=40,y=70)
Label(tk, text="Password").place(x=40,y=120)


t1=Entry(tk,bd="5")
t1.place(x=120,y=60)
t2=Entry(tk,bd="5",show="*")
t2.place(x=120,y=120)

Button(tk, text="login",command=login).place(x=50,y=170)
mainloop()
