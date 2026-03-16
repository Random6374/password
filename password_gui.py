import tkinter as tk
import random

out_label=None

_l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def cipher(start,x,what="encode"):
    if what=="decode":
        x=x*(-1)
    endr=""
    for i in start:
        if i in _l:
            ind=_l.index(i)+x
            endr+=_l[ind]
        else:
            endr+=i
    return endr

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
num=['1','2','3','4','5','6','7','8','9','0']
char=['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate(x):
    global out_label
    gene = ""
    pools = [letters, num, char]

    for _ in range(x):
        gene += random.choice(random.choice(pools))

    if out_label:
        out_label.destroy()

    out_label = tk.Label(gen, bg='lightgray',
                         text="suggested password is "+gene)
    out_label.grid(row=4, column=1)



def submit():
    key=e_key.get()
    value=e_value.get()
    r=random.randint(1,26)
    keyc=cipher(key,r)
    valuec=cipher(value,r)
    with open ('password.txt','w') as l:
        a=str(r)+' '+keyc+' '+valuec+' \n'
        l.write(a)
        l.close()
    switch(home)
 
def switch(x):
    l=[home,login,update,fetch,gen]
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
update=tk.Frame(m,bg='lightblue') 
fetch=tk.Frame(m,bg='lightblue')
gen=tk.Frame(m,bg='lightblue')

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
button=tk.Button(home,text="Update the database",bg='lightgray',command=lambda:switch(update),activebackground='gray').pack()
button=tk.Button(home,text="grab a password",bg='lightgray',command=lambda:switch(fetch),activebackground='gray').pack()
button=tk.Button(home,text='generate a password',bg='lightgray',activebackground='gray',command=lambda:switch(gen)).pack()

##################################################
#UPDATE SCREEN 
button=tk.Button(update,text="back to home",command=lambda:switch(home),background='lightgray',activebackground='gray').grid(row='1',column='1')
label=tk.Label(update,text="What password are you storing",bg='lightgray').grid(row='2',column='1')
label=tk.Label(update,text="enter the password to store",bg='lightgray').grid(row='3',column='1')
###################################################
#entries 
e_key=tk.Entry(update)
e_value=tk.Entry(update)
e_key.grid(row='2',column='2')
e_value.grid(row='3',column='2')
#################################################
#submit button
button=tk.Button(update,text='submit',activebackground='darkgray',bg='gray',command=lambda:submit()).grid(row='4',column='3')

####################################################
#FETCH SCREEN
button=tk.Button(fetch,text="Back to Home",command=lambda:switch(home),bg="lightgray",activebackground='gray').pack()


##################################################
#GEN SCREEN
button=tk.Button(gen,text="Back to Home",command=lambda:switch(home),bg="lightgray",activebackground='gray').grid(row='1',column='1')
label=tk.Label(gen,text="How long the password should be",bg='lightgray').grid(row='2',column='1')
e_len=tk.Entry(gen)
e_len.grid(row='2',column='2')
button=tk.Button(gen,text="Generate",bg='lightgray',activebackground='blue',command=lambda:generate(int(e_len.get()))).grid(row='3',column='1')
###############################################################################
m.mainloop()