from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
root=Tk()
root.title("Welcome To Rdonalds")
root.geometry("900x500")

burger=ImageTk.PhotoImage(Image.open("burger1.png"))
label_burger=Label(root,image=burger)
label_burger.place(relx=0.7,rely=0.5,anchor=CENTER)

label_heading=Label(root,font=("times",50,"bold"),text="Rdonalds")
label_heading.place(relx=0.2,rely=0.12,anchor=CENTER)

label_dish=Label(root,text="Select Dish",font=("times",15))
label_dish.place(relx=0.06,rely=0.2,anchor=CENTER)

list_dish=["Burger","Iced Americano"]
dropdown_dish=ttk.Combobox(root,state="readonly",values=list_dish)
dropdown_dish.place(relx=0.12,rely=0.2,anchor=CENTER)

list_toppings=[]
dropdown_toppings=ttk.Combobox(root,state="readonly",values=list_toppings)
dropdown_toppings.place(relx=0.12,rely=0.4,anchor=CENTER)

label_toppings=Label(root,text="Select Toppings",font=("times",15))
label_toppings.place(relx=0.06,rely=0.4,anchor=CENTER)

label_amount=Label(root,font=("times",15,"bold"))
label_amount.place(relx=0.5,rely=0.7,anchor=CENTER)


class parent():
    def __init__(self):
        print("This is the parent class")
    def menu(dish):
        if dish=="Burger":
            print("You can add the following toppings:")
            list_toppings=["Cheese","Jalapeno"]
            dropdown_toppings['values']=list_toppings
        elif dish=="Iced Americano":
            print("You can add one of the following toppings:")
            list_toppings=["Chocolate Flavor","Caramel Flavor"]
            dropdown_toppings['values']=list_toppings
        else:
            print("Please enter a valid dish")
    def final_amount(dish,add_ons):
        if dish=="Burger" and add_ons=="Cheese":
            label_amount['text']="You need to pay 250 USD"
        elif dish=="Burger" and add_ons=="Jalapeno":
            label_amount['text']="You need to pay 350 USD"
        elif dish=="iced_american" and add_ons=="Chocolate Flavor":
            label_amount['text']="You need to pay 350 USD"
        elif dish=="Iced Americano" and add_ons=="Caramel Flavor":
            label_amount['text']="You need to pay 450 USD"
class child1(parent):
    def __init__(self,dish):
        self.new_dish=dish
    def get_menu(self):
        new_dish=dropdown_dish.get()
        parent.menu(new_dish)
class child2(parent):
    def __init__(self,dish,add_ons):
        self.new_dish=dish
        self.add=add_ons
    def get_bill(self):
        new_dish=dropdown_dish.get()
        add=dropdown_toppings.get()
        parent.final_amount(new_dish,add)
        
obj1=child1(dropdown_dish.get())

obj2=child2(dropdown_dish.get(),dropdown_toppings.get())


btn_dish=Button(root,bg="blue",fg="white",text="Check Add-ons",relief=FLAT,command=obj1.get_menu)
btn_dish.place(relx=0.06,rely=0.3,anchor=CENTER)
btn_amount=Button(root,bg="blue",fg="white",text="Final Amount",relief=FLAT,command=obj2.get_bill)
btn_amount.place(relx=0.06,rely=0.5,anchor=CENTER)
root.mainloop()
