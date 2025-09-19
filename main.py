import random
import cipher
import gen

######################################################################################
# UPDATING THE PASSWORDS LIST
def update():
    Key=input("whats the trigger: ")
    value=input("whats the value: ")
    r=random.randint(1,26)
    keyc=cipher.cipher(Key,r)
    valuec=cipher.cipher(value,r)
    print(f"the shift is {r}")
    print("database updated")
    # print(D)
    with open("password.txt","a") as l:
        r=str(r)
        a= r+" "+keyc+" "+valuec+" \n"
        l.write(a)
        l.close()
##################################################################################
#startup dictionary update
with open("password.txt","r")as l:
    D={}
    o=cipher.count()
    if o!=0:
        for _ in range(0,o):
            s=l.readline()
            m=s.split(" ")
            keyd=cipher.cipher(m[1],int(m[0]),"decode")
            valued=cipher.cipher(m[2],int(m[0]),"decode")
            D.update({keyd:valued})
##############################################################
#main code
Passx=input("Enter your Password: ")
the="6374"                                                     ##the password
#######################################################################################
#if else tree
if Passx == the:
   
   while Passx ==the:
        print("Welcome to password manager")
###########################################################################
#the available functions
        print("""What Would you like to do?
1= update passwords list
2= fetch a password 
3= show existing password database
4= generate a password
5= change the password
    """)        
        n=int(input("What function you wanna operate: "))
        if n==1:
            update()
            q=gen.pause()
            if q == "yus":
                break
        elif n==2:
            app=input("which apps password?")
            x=D[app]
            print("password is ",x)
            q=gen.pause()
            if q == "yus":
                break
        elif n==3:
            print(D)
            q=gen.pause()
            if q == "yus":
                break
        elif n==4:
            x=int(input("how many letters:\n"))
            print(gen.generate(x))
            q=gen.pause()
            if q == "yus":
                break
        elif n==5:
            print("you are changing the managers password")
            the=input("what would you like your password to be\n")
            q=gen.pause()
            if q == "yus":
                break
        else:
            print("no such function available")
            q=gen.pause()
            if q == "yus":
                break
else:
    print("wrong password")  
