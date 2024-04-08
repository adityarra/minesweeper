import tkinter as tk
import tkinter.messagebox
import random

length=0
breadth=0
mines=0

def minesetting():
    root = tk.Tk()
    global length
    global breadth
    global mines
    global l123
    global w123
    length1 = tk.DoubleVar()
    breadth1 = tk.DoubleVar()
    mines1 = tk.DoubleVar()
    tk.Label(root, text="Enter number of rows: ").grid(row=0)
    tk.Label(root, text="Enter number of columns: ").grid(row=1)
    tk.Label(root, text="Enter percentage of mines: ").grid(row=2)
    length1.set(10)
    breadth1.set(10)
    mines1.set(10)
    e1 = tk.Scale(root, variable = breadth1, from_ = 3, to = 33, orient = tk.HORIZONTAL)
    e2 = tk.Scale(root, variable = length1, from_ = 3, to = 66, orient = tk.HORIZONTAL)
    e3 = tk.Scale(root, variable = mines1, from_ = 1, to = 99, orient = tk.HORIZONTAL)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    tk.Button(root, text="Submit", command=root.destroy).grid(column=1, row=3)
    root.mainloop()

    l1=[]
    l2=[]

    length=int(length1.get())
    breadth=int(breadth1.get())
    mines=int(mines1.get())

    if length>20 or breadth>20:
        w123 = 1
        l123 = 3
    else:
        w123 = 0
        l123 = 0

def minereset():
    global l1
    l1=[]
    global l2
    l2=[]
    global length
    global breadth
    global mines
    for i in range(length):
        l1.append([])
        for j in range(breadth):
            l1[i].append(True)
    count=0
    minecount = int(length*breadth*mines/100)
    if (minecount==0):
        minecount=1
    elif(minecount==length*breadth):
        minecount-=1
    while(count<minecount):
        r1=random.randrange(length)
        r2=random.randrange(breadth)
        if(l1[r1][r2]):
            l1[r1][r2]=False
            count+=1

    def minecounter(x,y,l1):
        numcount = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if(i!=-1 and i!=length and j!=-1 and j!=breadth):
                    if(l1[i][j]):
                        l1[i][j]=True
                    else:
                        l1[i][j]=False
                        
                        numcount+=1
        return numcount

    root2 = tk.Tk()

    def numpress(i,j,l1):
        if [i,j] in l2:
            return None
        if(i<=-1 or i>=length or j-5<=-1 or j-5>=breadth):
            return None
        l2.append([i,j])
        if (minecounter(i,j-5,l1)==0):
            tk.Label(root2, width=5-l123, height = 2-w123, bg="light grey").grid(column=i, row=j)
            for var1 in [-1,0,1]:
                for var2 in [-1,0,1]:
                    numpress(i+var1,j+var2,l1)
        else:
            tk.Label(root2, width=5-l123, height = 2-w123, bg="light grey", text=str(minecounter(i,j-5,l1))).grid(column=i, row=j)
        if(length*breadth-len(l2) == minecount):
            tkinter.messagebox.showinfo(root2, message="You won")
            root2.destroy
        return None
    label1 = tk.Label(root2, text="MINESWEEPER", height=2).grid(column=0, row=0, columnspan=length)
    def btnprs(i,j):
        tk.Label(root2, width=5-l123, height = 2-w123, bg="red").grid(column=i, row=j)
        tkinter.messagebox.showinfo(root2, message="You lost") 
        root2.destroy()

    for i in range(length):
        for j in range(breadth):
            if(l1[i][j]):
                tk.Button(root2, width=5-l123, height = 2-w123, activebackground="dark grey", bg="grey", command=lambda i=i, j=j+5:numpress(i,j,l1)).grid(column=i, row=j+5)
            else:
                tk.Button(root2, width=5-l123, height = 2-w123, activebackground="dark grey", bg="grey", command=lambda i=i, j=j+5:btnprs(i,j)).grid(column=i, row=j+5)
    
    def setting():
        global Flag1
        Flag1=True
        root2.destroy()
    tk.Button(root2, text="Quit", command=lambda:exit()).grid(column=i-1-l123, row=0, columnspan = 2+l123)
    tk.Button(root2, text="Settings", command=lambda:setting()).grid(column=0, row=0, columnspan = 2+l123)

    if(length*breadth-len(l2) == minecount):
        tkinter.messagebox.showinfo(root2, message="You won")
    root2.mainloop()

    return None

Flag=True
Flag1=True

while(Flag):
    if(Flag1):
        minesetting()
        Flag1=False
    minereset()
    
    if(not Flag1):
        root3=tk.Tk()
        def setting():
            global Flag1
            Flag1=True
            root3.destroy()
        tk.Label(root3, text="Game Over").pack(pady=20)
        tk.Button(root3, text="Continue", command=root3.destroy).pack(pady=20)
        tk.Button(root3, text="Quit", command=lambda:exit()).pack(pady=20)
        tk.Button(root3, text="Settings", command=lambda:setting()).pack(pady=20)
        root3.mainloop()