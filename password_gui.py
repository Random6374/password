import tkinter as tk

def switch(x):
    l=[home,login]
    for i in l:
        i.pack_forget()
    x.pack(fill='both',expand=True)

def login_check():
    pas=e.get()
    if pas=="6374":
        switch(home)
    else:
        label=tk.Label(login,text='Wrong password',bg="Red").grid(row='2',column='1')

#################################################
#GUI STARTS HERE
m=tk.Tk()
m.title("Password Manager")
################################################
#FRAMES
login=tk.Frame(m,bg='lightblue')
home=tk.Frame(m,bg="lightblue") 

###############################################
#LOGIN SCREEN
login.pack(fill='both',expand=True)
label=tk.Label(login,text='Enter the Password',background="lightgray").grid(row='0',column='0')
e=tk.Entry(login)
e.grid(row=0,column='1')
button=tk.Button(login,text="login",bg='lightgray',activebackground='black',command=login_check)
button.grid(row='1',column='1')
################################################
#HOME SCREEN
label=tk.Label(home,text="What would you like to do?",bg='lightgray').pack()
m.mainloop()
