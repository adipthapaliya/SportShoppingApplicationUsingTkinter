
from tkinter import *
from PIL import Image,ImageTk
import subprocess
import sqlite3
import random
from tkinter import ttk
from argparse import ArgumentParser





 #===========================================     Main Window         =========================================================

root=Tk()


root.title("SOD")
# root.attributes("-fullscreen", True)
root.state("zoomed")
root.resizable(False,False)
root.config(bg="#ffffff")





#========================================     ALL Funtions     ============================================================




        #--------------     Login Page   -----------------------------

def run_login():
    root.destroy()
    subprocess.call(["python","login.py"])

def sec_window ():
        root.destroy
        subprocess.call(["python","command.py"])

def g_window ():
        root.destroy
        subprocess.call(["python","girls.py"])

def b1_window ():
        root.destroy
        subprocess.call(["python","Fballs.py"])




def b2_window ():
        root.destroy
        subprocess.call(["python","Bballs.py"])


def bb_window ():
       root.destroy
       subprocess.call(["python","BB.py"])

        #----------------------     Home page Function   -------------------


def back_home():

    for ele in main_frame.winfo_children():
        ele.destroy()


    mainframe()





        #--------------   Product Details Function ----------------------

def details_mainframe(product_image):

        global main_frame

        main_frame = Frame(root)
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=1500, height=740)
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=1500, height=740)


        my_canvas.create_window((0, 0), window=second_frame)


        passed_image = Label(second_frame, image=product_image, bg="white", borderwidth=0)
        passed_image.grid(row=1,column=0)

        add_to_cart=Button(second_frame,text="Add  to cart",bg="black",fg="white")
        add_to_cart.grid(row=1,column=1)
        Large=Button(second_frame,text="Large",bg="black",fg="white")
        Large.grid(row=2,column=0)
        Medium=Button(second_frame,text="Medium",bg="black",fg="white")
        Medium.grid(row=0,column=2)
        small=Button(second_frame,text="small",bg="black",fg="white")
        small.grid(row=0,column=3)







        #-----------------------        Clearing the screen passing image --------------------

def description(product_image):
        #============= clear the screen
    for ele in main_frame.winfo_children():
        ele.destroy()

    details_mainframe(product_image)



        #-----------------------     Cart     --------------------------- 


                #------------------      adding cart function        ----------------- 
def add_to_cart():
        pass




                #-------------------    for your prodcut cart     --------------------------------

                
def cart_window():

        global main_frame

        main_frame = Frame(root)
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=1500, height=740)
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=1500, height=740)


        my_canvas.create_window((0, 0), window=second_frame)

        add_to_cart=Button(second_frame,text="Add  to cart")
        add_to_cart.grid(row=1,column=1)
        


def cart_frame():
    for ele in main_frame.winfo_children():
        ele.destroy()

    cart_window()


"""

def football():

        global main_frame

        main_frame = Frame(root)
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=1500, height=740)
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=1500, height=740)


        my_canvas.create_window((0, 0), window=second_frame)



def footbal_frame():
    for ele in main_frame.winfo_children():
        ele.destroy()

    football()      

"""




#=====================================        Database        ================================================================

conn=sqlite3.connect('register.db')

c=conn.cursor()




        #--------------------        Table for database       -------------------

# c.execute(""" CREATE TABLE login(
        
#         name String NOT NULL,
#         username String PRIMARY KEY,
#         email String NOT NULL,
#         phoneno Integer NOT NULL,
#         password String NOT NULL

#         )""")

      


        #-----------------------      passing username through argyument     --------------------

parser = ArgumentParser()
parser.add_argument("-u", "--user")

args = vars(parser.parse_args())
user = args['user']





#============================================       GUI        =============================================================



#-----------------------        Images     ---------------------------------------------


logo=Image.open("Home\sw.png")
search=Image.open("Home\search.png")
profile=Image.open("Home\profile.png")
contact=Image.open("Home\contact.png")
cart=Image.open("Home\cart.png")

logo=logo.resize((300,50),Image.ANTIALIAS)
search=search.resize((45,35),Image.ANTIALIAS)
profile=profile.resize((30,30),Image.ANTIALIAS)
contact=contact.resize((90,40),Image.ANTIALIAS)
cart=cart.resize((30,30),Image.ANTIALIAS)

logo_img=ImageTk.PhotoImage(logo)
search_img=ImageTk.PhotoImage(search)
profile_img=ImageTk.PhotoImage(profile)
contact_img=ImageTk.PhotoImage(contact)
cart_img=ImageTk.PhotoImage(cart)





        #---------------------         offer image     --------------------


offer=Image.open("Dress\offer.png")
offer1=Image.open("Dress\offer1.png")
offer2=Image.open("Dress\offer2.jpg")

offer=offer.resize((1500,500),Image.ANTIALIAS)
offer1=offer1.resize((1500,500),Image.ANTIALIAS)
offer2=offer2.resize((1500,500),Image.ANTIALIAS)

offer_img=ImageTk.PhotoImage(offer)
offer1_img=ImageTk.PhotoImage(offer1)
offer2_img=ImageTk.PhotoImage(offer2)

offer_list=[offer_img,offer1_img,offer2_img]




        #----------------------------------      Shopping Product     -----------------

F1 = Image.open("Dress\F1.jpg")
F2 = Image.open("Dress\F2.jpg")
F3 = Image.open("Dress\F3.png")
F4 = Image.open("Dress\F4.jpg")
F5 = Image.open("Dress\F5.jpg")
F6 = Image.open("Dress\F6.jpg")
F7 = Image.open("Dress\F7.png")
B1 = Image.open("Dress\B1.jpg")
B2 = Image.open("Dress\B2.jpg")


F1 = F1.resize((400, 400), Image.ANTIALIAS)
F2 = F2.resize((400, 400), Image.ANTIALIAS)
F3 = F3.resize((400, 400), Image.ANTIALIAS)
F4 = F4.resize((400, 400), Image.ANTIALIAS)
F5 = F5.resize((400, 400), Image.ANTIALIAS)
F6 = F6.resize((400, 400), Image.ANTIALIAS)
F7 = F7.resize((400, 400), Image.ANTIALIAS)
B1 = B1.resize((400, 400), Image.ANTIALIAS)
B2 = B2.resize((400, 400), Image.ANTIALIAS)

F1 = ImageTk.PhotoImage(F1)
F2 = ImageTk.PhotoImage(F2)
F3 = ImageTk.PhotoImage(F3)
F4 = ImageTk.PhotoImage(F4)
F5 = ImageTk.PhotoImage(F5)
F6 = ImageTk.PhotoImage(F6)
F7 = ImageTk.PhotoImage(F7)
B1 = ImageTk.PhotoImage(B1)
B2= ImageTk.PhotoImage(B2)

        



        #------------------------   Headlines    ------------------------------

logo_button=Button(root,image=logo_img,borderwidth=0,command=back_home)
logo_button.place(x=0,y=0)

search_entry=Entry(root,width=71,fg="black",justify="right",borderwidth=2,font="50")
search_entry.place(x=320,y=0,height=50)

search_button=Button(root,image=search_img,borderwidth=0)
search_button.place(x=1160,y=0)

cart_button=Button(root,image=cart_img,borderwidth=0,command=cart_frame)
cart_button.place(x=1250,y=0)

contact_button=Button(root,image=contact_img,borderwidth=0)
contact_button.place(x=1310,y=0)






        #---------------------    Label for Username   --------------------------------


welcome_label=Label(root,text="WELCOME!")
welcome_label.place(x=1420,y=0)

try:
        c.execute('SELECT * FROM login WHERE username = ?',(user,))

        records=c.fetchone()
        username=records[1]



        username_label=Label(root,text=username)
        username_label.place(x=1420,y=15)

except:
        pass


        #-------------------     Profile pic     ------------------------

profile_button=Button(root,image=profile_img,borderwidth=0,command=run_login)
profile_button.place(x=1500,y=0)





        #---------------------------------     Menu  BUttons     --------------------------


mb1 = Menubutton(root, text="MENS       ▼", relief=GROOVE, padx=25, pady=8, bg="black", fg="white")
mb1.place(x=320, y=50)
mb1.menu = Menu(mb1, tearoff=0, bg="white", fg="black")
mb1["menu"] = mb1.menu
mb2 = Menu(mb1, tearoff=0, bg="white", fg="black")
mb2.add_command(label="Wear", activebackground="black", activeforeground="white",command=sec_window)
mb2.add_separator()
mb2.add_command(label="Balls", activebackground="black", activeforeground="white",command=b1_window)

mb0 = Menu(mb1, tearoff=0, bg="white", fg="black")
mb0.add_command(label="Wear", activebackground="black", activeforeground="white",command=bb_window)
mb0.add_separator()
mb0.add_command(label="Balls", activebackground="black", activeforeground="white",command=b2_window)



mb1.menu.add_cascade(label="Football", menu=mb2, activebackground="black", activeforeground="white")
mb1.menu.add_separator()
mb1.menu.add_cascade(label="Basketball", menu=mb0, activebackground="black", activeforeground="white")



mb3 = Menubutton(root, text="WOMENS       ▼", relief=GROOVE, padx=25, pady=8, bg="black", fg="white")
mb3.place(x=650, y=50)
mb3.menu = Menu(mb3, tearoff=0, bg="white", fg="black")
mb3["menu"] = mb3.menu
mb4 = Menu(mb3, tearoff=0, bg="white", fg="black")
mb4.add_command(label="Wear", activebackground="black", activeforeground="white",command=g_window)
mb4.add_separator()
mb4.add_command(label="Balls", activebackground="black", activeforeground="white",command=b1_window)


mb7 = Menu(mb3, tearoff=0, bg="white", fg="black")
mb7.add_command(label="Wear", activebackground="black", activeforeground="white",command=bb_window)
mb7.add_separator()
mb7.add_command(label="Balls", activebackground="black", activeforeground="white",command=b2_window)


mb3.menu.add_cascade(label="Football", menu=mb4, activebackground="black", activeforeground="white")
mb3.menu.add_separator()
mb3.menu.add_cascade(label="Basketball", menu=mb7, activebackground="black", activeforeground="white")

mb5 = Button(root, text="⚽    Balls    ⚽", relief=GROOVE, padx=25, pady=4, bg="black", fg="white",command=b1_window)
mb5.place(x=955, y=50)

mb6 = Button(root, text="⌂ HOME", relief=GROOVE, padx=25, pady=4, bg="black", fg="white",command=back_home )
mb6.place(x=2, y=52)

        



      
        #-------------------    Function for Home Page       ---------------------------------

def mainframe():

        global main_frame


                #----------------    Creating a Frame  --------------------------

        main_frame = Frame(root)
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=1500, height=740)
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=1500, height=740)


        my_canvas.create_window((0,880), window=second_frame)




                #------------------------   All product Labeling  --------------------------------


        offer_random=random.randint(0,2)
        offer_label=Label(second_frame,image=offer_list[offer_random])
        offer_label.grid(row=0,column=0,columnspan=3)


        b1 = Button(second_frame, image=F1, bg="white", borderwidth=0,command=lambda : description(F1))
        b1.grid(row=1,column=0)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=0)
        l11=Label(second_frame,text="Adidas Real Madrid Jersy(White)")
        l11.grid(row=3,column=0)


        b2 = Button(second_frame, image=F2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F2))
        b2.grid(row=1,column=1)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=1)
        l22=Label(second_frame,text="Nike PSG Jersy(Blue)")
        l22.grid(row=3,column=1)


        b3 = Button(second_frame, image=F3, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F3))
        b3.grid(row=1,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=2,column=2)
        l33=Label(second_frame,text="Jordan Messi PSG Jersy(Blue)")
        l33.grid(row=3,column=2)


        b4 = Button(second_frame, image=F4, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F4))
        b4.grid(row=4,column=0)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=0)
        l44=Label(second_frame,text="Addidas Manchester United Jersy(Red)")
        l44.grid(row=6,column=0)


        b5 = Button(second_frame, image=F5, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F5))
        b5.grid(row=4,column=1)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=1)
        l55=Label(second_frame,text="Addidas Modrić Real Madrid Jersy(Pink)")
        l55.grid(row=6,column=1)


        b6 = Button(second_frame, image=F6, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F6))
        b6.grid(row=4,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=2)
        l44=Label(second_frame,text="Addidas Bayern Munich Jersy(Red)")
        l44.grid(row=6,column=2)


        b7 = Button(second_frame, image=B1, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(B1))
        b7.grid(row=7,column=0)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=8,column=0)
        l44=Label(second_frame,text="Nike LA Lakers Jersy(Yellow)")
        l44.grid(row=9,column=0)


        b8 = Button(second_frame, image=B2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(B2))
        b8.grid(row=7,column=1)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=8,column=1)
        l44=Label(second_frame,text="Jordan Chicago Bull Jersy(Red)")
        l44.grid(row=9,column=1)




        b9 = Button(second_frame, image=F7, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F7))
        b9.grid(row=7,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=8,column=2)
        l44=Label(second_frame,text="Adiddas Ronaldo Manchester United Jersy(Red)")
        l44.grid(row=9,column=2)









mainframe()



conn.commit()
conn.close()




root.mainloop()