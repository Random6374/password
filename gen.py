import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
num=['1','2','3','4','5','6','7','8','9','0']
char=['!', '#', '$', '%', '&', '(', ')', '*', '+']

l=len(letters)
n=len(num)
c=len(char)
def generate(x):
    gen=""
    for _ in range (0,x):
        if random.randint(1,3)==1:
            gen+=letters[random.randint(0,l-1)]
        if random.randint(1,3)==2:
            gen+=num[random.randint(0,n-1)]
        if random.randint(1,3)==3:
            gen+=char[random.randint(0,c-1)]
    return gen




def pause():
    print("do you want to exit the program ?")
    z=input("type yes if you want to: ")
    if ("yes".lower() in z.lower()):
        return "yus"
    else:
        print()



