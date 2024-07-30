
'''from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font

from menu import Menu

def main():
    root = Tk()
    app= MainWindow(root)
#MAIN WINDOW FOR LOG IN
class MainWindow:
    # constructor
    def __init__(self,master):
        # public data mambers
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="powder blue")
        self.frame = Frame(self.master,bg="powder blue")
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame,text = "HOSPITAL MANAGEMENT SYSTEM", font="Helvetica 20 bold",bg="powder blue",fg="black")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=40)
        #======================
        self.LoginFrame1 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame1.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #======LABEL AND ENTRY=========
        self.lblUsername = Label(self.LoginFrame1,text="Username",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblUsername.grid(row=0,column=0)
        self.lblUsername = Entry(self.LoginFrame1,font="Helvetica 14 bold",textvariable= self.Username,bd=2)
        self.lblUsername.grid(row=0,column=1)
        self.lblPassword = Label(self.LoginFrame1,text="Password ",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblPassword .grid(row=1,column=0)
        self.lblPassword  = Entry(self.LoginFrame1,font="Helvetica 14 bold",show="*",textvariable= self.Password,bd=2)
        self.lblPassword .grid(row=1,column=1)
        #===========BUTTONS====
        self.btnLogin = Button(self.LoginFrame2,text = "Login" ,font="Helvetica 10 bold", width =10 ,bg="powder blue",command = self.Login_system)
        self.btnLogin.grid(row=3,column=0)
        self.btnExit = Button(self.LoginFrame2,text = "Exit" ,font="Helvetica 10 bold", width =10 ,bg="powder blue",command = self.Exit)
        self.btnExit.grid(row=3,column=1)
    # public member function  
    #Function for LOGIN
    def Login_system(self):

        S1=(self.Username.get())
        S2=(self.Password.get())
        if(S1=='admin' and S2=='1234'):
            self.newWindow = Toplevel(self.master)
            self.app = Menu(self.newWindow)
        elif(S1=='root' and S2=='4321'):
            self.newWindow = Toplevel(self.master)
            self.app = Menu(self.newWindow)
        else:
            tkinter.messagebox.askretrycancel("HOSPITAL MANAGEMENT SYSTEM" , "PLEASE ENTER VALID USERNAME AND PASSWORD")
    #Function for Exit
    def Exit(self):
        self.master.destroy()
''''''
root = Tk()
login_form = main()
root.mainloop()



    







if __name__ == "__main__":
    main()
'''
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font

from menu import Menu

def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()

# MAIN WINDOW FOR LOG IN
class MainWindow:
    # constructor
    def __init__(self, master):
        # public data members
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="powder blue")
        self.frame = Frame(self.master, bg="powder blue")
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text="HOSPITAL MANAGEMENT SYSTEM", font="Helvetica 20 bold", bg="powder blue", fg="black")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40)
        # ======================
        self.LoginFrame1 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        # ======LABEL AND ENTRY=========
        self.lblUsername = Label(self.LoginFrame1, text="Username", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblUsername.grid(row=0, column=0)
        self.lblUsername = Entry(self.LoginFrame1, font="Helvetica 14 bold", textvariable=self.Username, bd=2)
        self.lblUsername.grid(row=0, column=1)
        self.lblPassword = Label(self.LoginFrame1, text="Password", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblPassword.grid(row=1, column=0)
        self.lblPassword = Entry(self.LoginFrame1, font="Helvetica 14 bold", show="*", textvariable=self.Password, bd=2)
        self.lblPassword.grid(row=1, column=1)
        # ===========BUTTONS====
        self.btnLogin = Button(self.LoginFrame2, text="Login", font="Helvetica 10 bold", width=10, bg="powder blue", command=self.login_system)
        self.btnLogin.grid(row=3, column=0)
        self.btnExit = Button(self.LoginFrame2, text="Exit", font="Helvetica 10 bold", width=10, bg="powder blue", command=self.exit)
        self.btnExit.grid(row=3, column=1)

    # public member function
    # Function for LOGIN
    def login_system(self):
        username = self.Username.get()
        password = self.Password.get()
        if username == 'admin' and password == '1234':
            self.open_menu()
        elif username=='root' and password=='4321':
            self.open_menu()
        else:
            self.show_error_message("Invalid Username or Password")

    

    # Function for Exit
    def exit(self):
        self.master.destroy()
    # Function to open the menu window
    def open_menu(self):
        self.newWindow = Toplevel(self.master)
        self.app = Menu(self.newWindow)

    # Function to show error message
    def show_error_message(self, message):
        tkinter.messagebox.showerror("HOSPITAL MANAGEMENT SYSTEM", message)


if __name__ == "__main__":
    main()
