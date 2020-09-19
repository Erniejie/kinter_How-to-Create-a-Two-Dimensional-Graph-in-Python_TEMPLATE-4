from tkinter import *
import tkinter.messagebox
root =Tk()
root.title(" ERNIE'S TWO DIMENSIONAL GRAPH")
root.geometry("1020x650+0+0")
root.config(bg="Cadet Blue")



#--- Outer Frame--------------------
MainFrame = Frame(root,bg="Powder Blue")
MainFrame.grid()

#------------Inner Frame
DataFrame2 =Frame(MainFrame,bd=1,width=1000,height=600,padx=38,pady=29,relief =RIDGE,
                  bg ="Cadet Blue")
DataFrame2.grid()

#-----------------------------

lblTitle = Label(DataFrame2, font =("Arial",16,"bold"),text ="DATA SCIENCE",
                 bg="Cadet Blue",fg="White")
lblTitle.grid(row=0,column=0,sticky=W)


#--------------- Creating Canvas--------------------------

canvas =Canvas(DataFrame2,width=900,height=510,bg="Powder Blue")
canvas.grid(row=1,column=0)


#-------- Creating Cartesian Coordinates X-Y--------

canvas.create_line(100,450,800,450,width =5) #------ x Coordinates: x = 800

canvas.create_line(100,450,100,50,width =5)   #----- y Coordinates

#--- Labeling   X Axis -------------------

for i in range(11):   # 11 is the number of x axle
    x = 100 +(i*60)
    canvas.create_line(x,450,x,445, width=5)# --- For Number of Graduations
    canvas.create_text(x,454,text ="%d"%(50*i),anchor=N)


#--- Labeling   Y Axis -------------------

for i in range(10):
    y = 450 -(i*40)
    canvas.create_line(100,y,105,y, width=5)   #--- For Number of Graduations
    canvas.create_text(96,y,text ="%5.1f"%(50*i),anchor=E)


#---- For Both Axes-Scattering

for x,y in [(20,89),(40,184),(66,198),(90,220),(82,260),
            (95,321),(108,446),(88,446)]:
    x= 50 +7*x
    y= 450-(4*y)/5
    canvas.create_oval(x-6,y-6,x+6,y+6,width=2,outline="Red",fill="Yellow")

#------------Function-------------------

def iExit():
    qExit = tkinter.messagebox.askyesno("Quit the System", "Do You Want to Quit?")
    if qExit > 0:
        root.destroy()
        return

Button(root, text = "Exit",font=("arial",12,"bold"),width=16,bd=2, padx=8,
       bg="Cadet Blue",fg="White", command=iExit).grid()







root.mainloop()
