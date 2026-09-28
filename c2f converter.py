import tkinter as tk 
screen=tk.Tk()
screen.title("imperial to normal temp converter")
screen.configure(bg= "white")
screen.geometry("500x500")

def c2f():
    celcius= int(e1.get())
    faarenheit= (celcius*1.8)+32
    l2.config(text=str(faarenheit) + "F")


l1= tk.Label(text="Write down the temperature in celcius below", width=40, height= 3, bg="white", fg="black")
l1.place(x= 6, y=6) 
e1= tk.Entry(width= 30)
e1.place(x=300, y= 20 )
b1= tk.Button(text= "Convrrt", bg= "white", fg= "black", command= c2f)
b1.place(x=200, y= 100)
l2=tk.Label(text="", width=40, height= 3, bg="white", fg="black")
l2.place(x= 150, y= 200)


screen.mainloop()