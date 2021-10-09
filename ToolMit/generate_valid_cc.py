# It Is Just For Educational Purpose . Created By Nick_Z Copyright 2020 Some Right Reseverd
from tkinter import*
import random

binx=[460811,439393,646031,440098,432399,552493,552478,554962,556115,492882,498706,491113,
492866,633450,548815,552689,409724,420540,421686,445304,400672,554371,415054,555009,677262,512437]

check_on=[]

root=Tk()
root.geometry("400x450+70+80")
root.title("Credit Card Generator v2.0")
Label(root,text="Credit Card Generator",font=("verdana",18)).pack(side=TOP,pady=10)
root_fm=Frame(root,cursor="heart")
root_fm.pack(side=TOP)
photo=PhotoImage(file=r"io.png")
photoimage=photo.subsample(6,10)
Button(root_fm,text="Credit Card",image=photoimage).pack(side=TOP,pady=10)
ent=Entry(root_fm,relief="flat",font=("Verdana",18),justify=RIGHT)
ent.pack(side=TOP,pady=21)



def check():

    bins=binx[random.randint(0,len(binx)-1)]
    asem=str(bins)
    last_10=[]

    for i in range(0,10):
        l=random.randint(0,9)
        last_10.append(l)
    
    aj=""

    for i in last_10:
        aj=str(aj)+str(i)

    adex=str(bins)+str(aj)

    sum_gss_10=[]
    gss_or_equ10=[]
    lss10=[]
    odd=[]
    valid=list(adex)
    for i in range(0,len(valid),2):
        ss=int(valid[i])*2
        
        if (ss>=10):
            gss_or_equ10.append(ss)
        else:
            lss10.append(ss)
    
    for j in range(0,len(gss_or_equ10)):
        io=str(gss_or_equ10[j])
        dim=0
        for i in io:
            dim=int(dim)+int(i)
        sum_gss_10.append(dim)
    
    dim=0
    for n in sum_gss_10:
        dim = dim + n

    lim=0
    for l in lss10:
        lim=lim+l

    sid = dim + lim

    for i in range(1,len(valid),2):
        ss=int(valid[i])
        odd.append(ss)
    
    lid=0

    for u in odd:
        lid=lid+u


    mid=sid+lid

    rim=mid % 10

    if (rim==0):
        print("it's a valid credit card & Check Sum ",mid,"And Credit Card Is ",adex)
        check_on.append(1)
        ent.delete(0,END)
        ent.insert( 0, adex )

    else:
        pass

def generated ():
    while(1):
        check()
        if(len(check_on)==1):
            check_on.clear()
            break

Button(root_fm,text="Generate",font=("verdana",14),command=generated).pack(side=TOP,pady=10)

root.mainloop()


