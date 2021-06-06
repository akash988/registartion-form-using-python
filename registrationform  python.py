from tkinter import *
root=Tk()
root.geometry("600x600+100+50")
root.title("Registration Form")

def getvals():
    print("Registration Done")


# Heading
Label(root,text="Python Registration Form", font="arial 15 bold").grid(row=0,column=3)

# Field Name
Name=Label(root,text="Name")
Phone=Label(root,text="Phone")
Email=Label(root,text="Email")
Gender=Label(root,text="Gender")
PaymentMethod=Label(root,text="PaymentMethod")

# Packing Fields
Name.grid(row=1,column=0)
Phone.grid(row=2,column=0)
Email.grid(row=3,column=0)
Gender.grid(row=4,column=0)
PaymentMethod.grid(row=5,column=0)

# Variable For Storinf Data
Namevalue=StringVar
Phonevalue=IntVar
Emailvalue=StringVar
PaymentMethodvalue=StringVar
checkvalue=IntVar
checkvalue1=IntVar
checkvalue2=IntVar
checkvalue3=IntVar
checkvalue4=IntVar
checkvalue5=IntVar

# Creating Entry Fields
Nameentry=Entry(root,textvariable=Namevalue)
Phoneentry=Entry(root,textvariable=Phonevalue)
Emailentry=Entry(root,textvariable=Emailvalue)


# Packing  Entry Fields
Nameentry.grid(row=1,column=3)
Phoneentry.grid(row=2,column=3)
Emailentry.grid(row=3,column=3)


# Creating Checkbox
chechbtn1=Checkbutton(text="Male",variable=checkvalue1)
chechbtn1.grid(row=4,column=3)
chechbtn2=Checkbutton(text="Female",variable=checkvalue2)
chechbtn2.grid(row=4,column=4)
chechbtn3=Checkbutton(text="Paytm",variable=checkvalue3)
chechbtn3.grid(row=5,column=3)
chechbtn4=Checkbutton(text="NEFT",variable=checkvalue4)
chechbtn4.grid(row=5,column=4)
chechbtn5=Checkbutton(text="GPay",variable=checkvalue4)
chechbtn5.grid(row=5,column=5)
checkbtn=Checkbutton(text="Accept terms & conditions",variable=checkvalue)
checkbtn.grid(row=6,column=3)

# submit Button
Button(text="Submit",command=getvals).grid(row=10,column=3)



root.mainloop()