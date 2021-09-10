from tkinter import *
from PIL import Image,ImageTk
import subprocess
import sqlite3
import random
from tkinter import ttk

root=Tk()
root.title("Items")
root.minsize(430,500)
root.resizable(False,False)
root.config(bg="#ffffff")

def details_mainframe(product_image):

        global main_frame

        main_frame = Frame(root)
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=500, height=500)
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=100, height=100)


        my_canvas.create_window((250,0), window=second_frame)


        b1 = Button(second_frame, image=product_image, bg="white", borderwidth=0)
        b1.grid(row=1,column=0)

        add_to_cart=Button(second_frame,text="Add  to cart",bg="black",fg="white")
        add_to_cart.grid(row=3,column=0)
        # lar_ge=Button(second_frame,text="Large",bg="black",fg="white ")
        # lar_ge.grid_info(row=2,column=0)

def description(product_image):
        #============= clear the screen
    for ele in main_frame.winfo_children():
        ele.destroy()

    details_mainframe(product_image)



B1 = Image.open("Balls\B1.jpg")
B2 = Image.open("Balls\B2.jpg")
B3 = Image.open("Balls\B3.jpg")
B4 = Image.open("Balls\B4.jpg")
B5 = Image.open("Balls\B5.jpg")
B6 = Image.open("Balls\B6.jpg")



B1 = B1.resize((200, 200), Image.ANTIALIAS)
B2 = B2.resize((200, 200), Image.ANTIALIAS)
B3 = B3.resize((200, 200), Image.ANTIALIAS)
B4 = B4.resize((200, 200), Image.ANTIALIAS)
B5 = B5.resize((200, 200), Image.ANTIALIAS)
B6 = B6.resize((200, 200), Image.ANTIALIAS)


B1 = ImageTk.PhotoImage(B1)
B2 = ImageTk.PhotoImage(B2)
B3 = ImageTk.PhotoImage(B3)
B4 = ImageTk.PhotoImage(B4)
B5 = ImageTk.PhotoImage(B5)
B6 = ImageTk.PhotoImage(B6)



def mainframe():

        global main_frame


                #----------------    Creating a Frame  --------------------------

        main_frame = Frame(root)
        main_frame.place(x=0, y=0)

        my_canvas = Canvas(main_frame, width=400, height=500)
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=300, height=500)


        my_canvas.create_window((0, 500), window=second_frame)




                #------------------------   All product Labeling  --------------------------------


        

        b1 = Button(second_frame, image=B1, bg="white", borderwidth=0,command=lambda : description(B1))
        b1.grid(row=1,column=0)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=0)
        l11=Label(second_frame,text="NIKE PL BALL")
        l11.grid(row=3,column=0)


        b2 = Button(second_frame, image=B2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(B2))
        b2.grid(row=1,column=2)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=2)
        l22=Label(second_frame,text="Addidas Telstar WC 18 Ball")
        l22.grid(row=3,column=2)


        b3 = Button(second_frame, image=B3, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(B3))
        b3.grid(row=4,column=0)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=0)
        l33=Label(second_frame,text="Classic Black & White Ball")
        l33.grid(row=6,column=0)


        b4 = Button(second_frame, image=B4, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(B4))
        b4.grid(row=4,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=2)
        l44=Label(second_frame,text="UEFA Ball")
        l44.grid(row=6,column=2)


        b5 = Button(second_frame, image=B5, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(B5))
        b5.grid(row=7,column=0)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=8,column=0)
        l55=Label(second_frame,text="Addidas Euro 2020 Ball")
        l55.grid(row=9,column=0)


        b6 = Button(second_frame, image=B6, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(B6))
        b6.grid(row=7,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=8,column=2)
        l44=Label(second_frame,text="Addidas Brazuca WC 14 Ball")
        l44.grid(row=9,column=2)


       
        


mainframe()









root.mainloop()