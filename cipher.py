
_l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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


def count():
    line_count = 0
    with open("password.txt", 'r') as f:
        for line in f:
            line_count += 1
    return line_count

    