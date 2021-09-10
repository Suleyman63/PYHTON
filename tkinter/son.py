from tkinter import*
from tkinter import ttk
import data_base
import tkinter.messagebox


class Student:

    def __init__(self, root):
            self.root = root
            self.root.title("STUDENT MANAGEMENT SYSTEM")
            self.root.geometry("1500x800+0+0")
            self.root.config(bg="cadet blue")

            Student_Id = StringVar()
            Firstname = StringVar()
            Lastname = StringVar()
            Age = StringVar()
            Phone = StringVar()
            Email = StringVar()
            Clas = StringVar()



            ############################ Function #################################
            def iExit():
                iExit = tkinter.messagebox.askyesno("confirm if you want to exit")
                if iExit > 0:
                    root.destroy()
                    return 


            # this is function will clear the entry boxes
            def clear_data():
                self.e1.delete(0, END)
                self.e2.delete(0, END)
                self.e3.delete(0, END)
                self.e4.delete(0, END)
                self.e5.delete(0, END)
                self.e6.delete(0, END)
                self.e7.delete(0, END)

            
            def add_student():
                try:
                    if(len(Student_Id.get())!=0):
                        data_base.add_data(
                            Student_Id.get(),
                            Firstname.get(),
                            Lastname.get(),
                            Age.get(),
                            Phone.get(),
                            Email.get(),
                            Clas.get()),

                        self.Studentlist.delete(0, END)
                        self.Studentlist.insert(END, (
                            Student_Id.get(),
                            Firstname.get(),
                            Lastname.get(),
                            Age.get(),
                            Phone.get(),
                            Email.get(),
                            Clas.get()))
                        tkinter.messagebox.showinfo("successfully added")
                except:
                    tkinter.messagebox.showinfo('it is not added')


            def show_all():
                self.Studentlist.delete(0,END)
                for row in data_base.view_data():
                     self.Studentlist.insert(END,row,str("******************************************************"))



            def student_record(event=None):
                global sd
                search = self.Studentlist.curselection()[0]
                sd = self.Studentlist.get(search)

                self.e1.delete(0,END)
                self.e1.insert(END,sd[1])
                self.e2.delete(0,END)
                self.e2.insert(END,sd[2])
                self.e3.delete(0,END)
                self.e3.insert(END,sd[3])
                self.e4.delete(0,END)
                self.e4.insert(END,sd[4])
                self.e5.delete(0,END)
                self.e5.insert(END,sd[5])
                self.e6.delete(0,END)
                self.e6.insert(END,sd[6])
                self.e7.delete(0,END)
                self.e7.insert(END,sd[7])
           

            def delete_student():
                if(len(Student_Id.get())!=0):
                    data_base.delete_data(sd[0])
                    clear_data()
                    show_all()
                    tkinter.messagebox.showinfo('successfully deleted')
                    
            
            
            def update():
                if(len(Student_Id.get())!=0):
                    data_base.delete_data(sd[0])
                if(len(Student_Id.get())!=0):
                   data_base.add_data(
                       Student_Id.get(),
                       Firstname.get(),
                       Lastname.get(),
                       Age.get(),
                       Phone.get(),
                       Email.get(),
                       Clas.get())

                   self.Studentlist.delete(0,END)
                   self.Studentlist.insert(END, (
                       Student_Id.get(),
                       Firstname.get(),
                       Lastname.get(),
                       Age.get(),
                       Phone.get(),
                       Email.get(),
                       Clas.get()))
                  
            
            
            def search_student():
                self.Studentlist.delete(0,END)
                for row in data_base.search_data(
                    Student_Id.get(),
                    Firstname.get(),
                    Lastname.get(),
                    Age.get(),
                    Phone.get(),
                    Email.get(),
                    Clas.get()):
                    self.Studentlist.insert(END,row,str(""))


            #################### FRAME #################################

            title=Label(self.root, text="STUDENT MANAGEMENT SYSTEM", bd=9, relief=GROOVE, bg="orange", font=("arial", 30))
            title.pack(side=TOP, fill=X)

            MainFrame = Frame(self.root, bd=4, relief=RIDGE, bg="orange")
            MainFrame.place(x=20, y=100, width=500, height=550)

            MainTitle = Label(MainFrame, text="Manage Student", fg="black", font=("Arial", 20, "bold"))
            MainTitle.grid(row=0, columnspan=2, pady=10)


            BtnFrame = Frame(self.root, bd=3, relief=RIDGE, bg="cadet blue")
            BtnFrame.pack(side=BOTTOM)

            TblFrame = Frame(root, bd=3, relief=RIDGE, bg="white")
            TblFrame.place(x=550, y=100, width=900, height=550)


            #################### LABEL ##########################################
            self.l1 = Label(MainFrame, text="Studen_Id", width=17, font=("Arial", 11), fg="white", bg="cadet blue", pady=8)
            self.l1.grid(row=1, column=0, pady=10, padx=20, sticky='w')
            self.l2 = Label(MainFrame, text="Firstname", width=17, font=("Arial", 11), fg="white", bg="cadet blue", pady=8)
            self.l2.grid(row=2, column=0, pady=10, padx=20, sticky='w')
            self.l3 = Label(MainFrame, text="Lastname", width=17, font=("Arial", 11), fg="white", bg="cadet blue", pady=8)
            self.l3.grid(row=3, column=0, pady=10, padx=20, sticky='w')
            self.l4 = Label(MainFrame, text="Age", width=17, font=("Arial", 11), fg="white", bg="cadet blue", pady=8)
            self.l4.grid(row=4, column=0, pady=10, padx=20, sticky='w')
            self.l5 = Label(MainFrame, text="Phone", width=17, font=("Arial", 11), fg="white", bg="cadet blue", pady=8)
            self.l5.grid(row=5, column=0, pady=10, padx=20, sticky='w')
            self.l6 = Label(MainFrame, text="Email", width=17, font=("Arial", 11), fg="white", bg="cadet blue", pady=8)
            self.l6.grid(row=6, column=0, pady=10, padx=20, sticky='w')
            self.l7 = Label(MainFrame, text="Clas", width=17, font=("Arial", 11), fg="white", bg="cadet blue", pady=8)
            self.l7.grid(row=7, column=0, pady=10, padx=20, sticky='w')

            ############################################ ENTRY ###############################################################
            self.e1 = Entry(MainFrame, textvariable=Student_Id, font=("Arial", 15, "bold"), bd=5, width=25, relief=GROOVE)
            self.e1.grid(row=1, column=1)
            self.e2 = Entry(MainFrame, textvariable=Firstname, font=("Arial", 15, "bold"), bd=5, width=25, relief=GROOVE)
            self.e2.grid(row=2, column=1)
            self.e3 = Entry(MainFrame, textvariable=Lastname, font=("Arial", 15, "bold"), bd=5, width=25, relief=GROOVE)
            self.e3.grid(row=3, column=1)
            self.e4 = Entry(MainFrame, textvariable=Age, font=("Arial", 15, "bold"), bd=5, width=25, relief=GROOVE)
            self.e4.grid(row=4, column=1)
            self.e5 = Entry(MainFrame, textvariable=Phone, font=("Arial", 15, "bold"), bd=5, width=25, relief=GROOVE)
            self.e5.grid(row=5, column=1)
            self.e6 = Entry(MainFrame, textvariable=Email, font=("Arial", 15, "bold"), bd=5, width=25, relief=GROOVE)
            self.e6.grid(row=6, column=1)
            self.e7 = Entry(MainFrame, textvariable=Clas, font=("Arial", 15, "bold"), bd=5, width=25, relief=GROOVE)
            self.e7.grid(row=7, column=1)

            ################# BUTTON ###############################################################
           

            self.b1 = Button(BtnFrame, text="Add New", width=20, bd=4, bg="dark green", fg="white", height=4, command=add_student)
            self.b1.grid(row=0, column=0,padx=20, pady=20)
            self.b2 = Button(BtnFrame, text="Delete", width=20, bd=4, bg="brown", fg="white", height=4, command=delete_student)
            self.b2.grid(row=0, column=1,padx=20, pady=20)
            self.b3 = Button(BtnFrame, text="Update", width=20, bd=4, bg="orange", fg="white", height=4, command=update)
            self.b3.grid(row=0, column=2,padx=20, pady=20)
            self.b4 = Button(BtnFrame, text="Clear", width=20, bd=4, height=4, bg="gray", fg="white", command=clear_data)
            self.b4.grid(row=0, column=3,padx=20, pady=20)
            self.b5 = Button(BtnFrame, text="Search", width=20, bd=4, bg="dark blue", fg="white", height=4, command=search_student)
            self.b5.grid(row=0, column=6,padx=20, pady=20)
            self.b6 = Button(BtnFrame, text="Show All", width=20, bd=4, bg="tomato", fg="white", height=4, command=show_all)
            self.b6.grid(row=0, column=7,padx=20, pady=20)
            self.b7 = Button(BtnFrame, text="Exit", width=20, bd=4, height=4, bg="skyblue", fg="white", command=iExit)
            self.b7.grid(row=0, column=5,padx=20, pady=20)


            ############################ SEARCH BAR ##########################################################
           

            # self.e8 = Entry(TblFrame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
            # self.e8.grid(row=0, column=1, pady=10, padx=20, sticky="w")


            ############################### SCROLL ######################################################
            # scrollbar = Scrollbar(TblFrame)
            # scrollbar.grid(row=3, column=1, sticky='ns')


            # Studentlist = Listbox(TblFrame, width=97, height=28, font=('Arial', 12), yscrollcommand = scrollbar.set)
            # Studentlist.grid(row=3, column=2, padx=8)
            # Studentlist.bind('<<ListboxSelect>>', student_record)
            # scrollbar.config(command = Studentlist.yview)
            
            

            ################################# eski ##########################################################


            scroll_x = Scrollbar(TblFrame, orient=HORIZONTAL)
            scroll_y = Scrollbar(TblFrame, orient=VERTICAL)

            
            self.Studentlist = ttk.Treeview(TblFrame, column=("Student_Id", "Firstname", "Lastname", "Age", "Phone", "Email", "Clas"), \
                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
           

            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

        
            self.Studentlist.heading("Student_Id",text="Student_Id")
            self.Studentlist.heading("Firstname", text="Firstname")
            self.Studentlist.heading("Lastname", text="Lastname")
            self.Studentlist.heading("Age", text="Age")
            self.Studentlist.heading("Phone", text="Phone")
            self.Studentlist.heading("Email", text="Email")
            self.Studentlist.heading("Clas", text="Clas")

            self.Studentlist['show']='headings'

            self.Studentlist.column("Student_Id", width=100)
            self.Studentlist.column("Firstname", width=100)
            self.Studentlist.column("Lastname", width=100)
            self.Studentlist.column("Age", width=100)
            self.Studentlist.column("Phone", width=100)           
            self.Studentlist.column("Email", width=100)
            self.Studentlist.column("Clas", width=100)

            self.Studentlist.pack(fill=BOTH, expand=1)
            self.Studentlist.bind("<ButtonRelease-1>", student_record)
            show_all()


if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
