from tkinter import *
from tkinter import messagebox, ttk
import random
import database
import sqlite3


randomnum = random.randint(1,10000)


class Student:
    def __init__(self, root):
        self.root=root
        self.root.title('STUDENT MANAGEMENT SYSTEM')
        self.root.geometry('1600x800+0+0')


        # variables #
        self.Nummer = StringVar()
        self.Firstname = StringVar()
        self.Lastname = StringVar()
        self.Age = StringVar()
        self.Email = StringVar()
        self.Phone = StringVar()  
        self.Gender = StringVar()
        self.Class = StringVar()


############################################## FRAME ####################################################################

        self.top=Label(self.root, text='STUDENT MANAGEMENT SYSTEM', font=('arial', 20), bg='#164A58', fg='white', pady=10)
        self.top.place(x=0, y=0, relwidth=1)

        self.leftframe = Frame(self.root, bg='#164A58')
        self.leftframe.place(x=10, y=64, width=450, height=700)

        self.lefttitle= Label(self.leftframe, text='Student Form', font=('arial', 15), bg='#164A58', fg='white' )
        self.lefttitle.place(x=0, y=10, relwidth=1)


########################## LABEL ##################################################################################

        self.l1 = Label(self.leftframe, text='Nummer', font=('arial', 12), bg='#164A58', fg='white')
        self.l1.place(x=30, y=80) 

        self.l2 = Label(self.leftframe, text='Firstname', font=('arial', 12), bg='#164A58', fg='white')
        self.l2.place(x=30, y=130)

        self.l3 = Label(self.leftframe, text='Lastname', font=('arial', 12), bg='#164A58', fg='white')
        self.l3.place(x=30, y=180)

        self.l4 = Label(self.leftframe, text='Age', font=('arial', 12), bg='#164A58', fg='white')
        self.l4.place(x=30, y=230)

        self.l5 = Label(self.leftframe, text='Email', font=('arial', 12), bg='#164A58', fg='white')
        self.l5.place(x=30, y=280)

        self.l6 = Label(self.leftframe, text='Phone', font=('arial', 12), bg='#164A58', fg='white', pady=10)
        self.l6.place(x=30, y=330)

        self.l7 = Label(self.leftframe, text='Gender', font=('arial', 12), bg='#164A58', fg='white', pady=10)
        self.l7.place(x=30, y=380)

        self.l8 = Label(self.leftframe, text='Class', font=('arial', 12), bg='#164A58', fg='white', pady=10)
        self.l8.place(x=30, y=430)



###################### ENTRY #######################################################################

        self.e1 =Entry(self.leftframe, textvariable=self.Nummer, font=('arial', 14))
        self.e1.place(x=150, y=80, width=280)
        self.e1.insert(END, str(randomnum))
        

        self.e2 =Entry(self.leftframe, textvariable=self.Firstname, font=('arial', 14))
        self.e2.place(x=150, y=130, width=280)

        self.e3 =Entry(self.leftframe, textvariable=self.Lastname, font=('arial', 14))
        self.e3.place(x=150, y=180, width=280)

        self.e4 =Entry(self.leftframe, textvariable=self.Age, font=('arial', 14))
        self.e4.place(x=150, y=230, width=280)

        self.e5 =Entry(self.leftframe, textvariable=self.Email, font=('arial', 14))
        self.e5.place(x=150, y=280, width=280)

        self.e6 =Entry(self.leftframe, textvariable=self.Phone, font=('arial', 14))
        self.e6.place(x=150, y=330, width=280)

        self.e7 =ttk.Combobox(self.leftframe, textvariable=self.Gender, font=('arial', 14))
        self.e7['values'] = ('Male', 'Female')
        self.e7.config(width=23)
        self.e7.current(0)
        self.e7.place(x=150, y=380)

        self.e8 =ttk.Combobox(self.leftframe, textvariable=self.Class, font=('arial', 14))
        self.e8['values'] = ('A', 'B', 'C', 'D')
        self.e8.config(width=23)
        self.e8.current(0)
        self.e8.place(x=150, y=430)


################################  BUTTON #########################################

        self.b1 = Button(self.leftframe, command=self.addnew, text='Add Student', font=('arial', 14), bg="#237A57", fg="white", pady=7, width=10, activebackground='brown')
        self.b1.place(x=30, y=500)

        self.b2 = Button(self.leftframe, command=self.update, text='Update', font=('arial', 14), bg="orange", fg='white', pady=7, width=10, activebackground='brown')
        self.b2.place(x=180, y=500)

        self.b3 = Button(self.leftframe, command=self.deletestudent, text='Delete', font=('arial', 14), bg="brown", fg='white', pady=7, width=10, activebackground='brown')
        self.b3.place(x=320, y=500)

        self.b4 = Button(self.leftframe, command=self.cleardata, text='Clear', font=('arial', 14), bg='gray', fg='white', pady=7, width=10, activebackground='brown')
        self.b4.place(x=30, y=580)

        self.b5 = Button(self.leftframe, command=self.showdata, text='Show All', font=('arial', 14), bg="#302b63", fg='white', pady=7, width=10, activebackground='brown')
        self.b5.place(x=180, y=580)

        self.b6 = Button(self.leftframe, command=self.exit, text='Exit', font=('arial', 14), bg="#004e92", fg='white', pady=7, width=10, activebackground='brown')
        self.b6.place(x=320, y=580)


############################ TABLE HEADER #########################################################

        self.table = Frame(self.root, bg='#164A58')
        self.table.place(x=500, y=64, width=1080, height=720)

        self.tabletitle =Label(self.table, text='Student Table', font=('arial', 15), bg='#164A58', fg='white')
        self.tabletitle.place(x=0, y=10, relwidth=1)

        self.tableframe = Frame(self.table)
        self.tableframe.place(x=25, y=60, width=1020, height=600)

            ### search button ######
        self.b7 = Button(self.table, command=self.searchdata, text='search', pady=4, font=('arial', 12), bg='cadet blue', fg='white', width=7, activebackground='brown')
        self.b7.place(x=970, y=15)

            ### search entry #####
        self.e9 =Entry(self.table, textvariable=self.Nummer, font=('arial', 12))
        self.e9.place(x=848, y=16, height=35, width=120)

     

############################# TABLE DETAILS #################################################
        style = ttk.Style()
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        self.scrollx = Scrollbar(self.table, orient=HORIZONTAL)
        self.scrolly = Scrollbar(self.table, orient=VERTICAL)
        
        self.Studenttable = ttk.Treeview(self.tableframe, columns=('id', 'Nummer', 'Firstname', 'Lastname', 'Age', 'Email', 'Phone', 'Gender', 'Class'), \
             xscrollcommand=self.scrollx.set, yscrollcommand=self.scrolly.set)
        
        self.scrollx.pack(side=BOTTOM, fill=X)
        self.scrolly.pack(side=RIGHT, fill=Y)

        self.scrollx.config(command=self.Studenttable.xview)
        self.scrolly.config(command=self.Studenttable.yview)


       
        self.Studenttable.heading('Nummer', text='Nummer')
        self.Studenttable.heading('Firstname', text='Firstname')
        self.Studenttable.heading('Lastname', text='Lastname')
        self.Studenttable.heading('Age', text='Age')
        self.Studenttable.heading('Email', text='Email')
        self.Studenttable.heading('Phone', text='Phone')
        self.Studenttable.heading('Gender', text='Gender')
        self.Studenttable.heading('Class', text='Class')

       
        self.Studenttable.column('Nummer', width=120, anchor=CENTER)
        self.Studenttable.column('Firstname', width=120, anchor=CENTER)
        self.Studenttable.column('Lastname', width=120, anchor=CENTER)
        self.Studenttable.column('Age', width=50, anchor=CENTER)
        self.Studenttable.column('Email', width=120, anchor=CENTER)
        self.Studenttable.column('Phone', width=120, anchor=CENTER)
        self.Studenttable.column('Gender', width=50, anchor=CENTER)
        self.Studenttable.column('Class', width=50, anchor=CENTER)

        self.Studenttable['show'] ='headings'
        self.Studenttable.pack(fill=BOTH, expand=1)
        self.Studenttable.bind('<ButtonRelease>', self.getrecord)
        self.showdata()
        

#################################################################################################################################

 #                                               -- Functions ----


######## neu data register function ###############################
    def addnew(self):
            
                if self.Nummer.get()=='' or self.Firstname.get()=='' or self.Lastname.get()=='':
                    messagebox.showinfo('some fields are required')
                else:
                    try:                      
                        connection = sqlite3.connect('students.db')
                        cursor = connection.cursor()
                        q="INSERT INTO students VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)" 
                        cursor.execute(q,(self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), self.e5.get(), self.e6.get(), self.e7.get(), self.e8.get()))
                        connection.commit()
                        
                        self.e1.delete(0, END),
                        self.e1.insert(END, str(randomnum))
                        self.e2.delete(0, END),
                        self.e3.delete(0, END),
                        self.e4.delete(0, END),
                        self.e5.delete(0, END),
                        self.e6.delete(0, END),
                        self.e7.current(0),
                        self.e8.current(0)
                        self.showdata()
                        connection.close()
                        messagebox.showinfo(f"ID {self.Nummer.get()} successfully added")
                    except:
                       messagebox.showwarning('error')                            
                  

########### alle daten zeigen function ###################

    def showdata(self):
            connection = sqlite3.connect('students.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            self.Studenttable.delete(*self.Studenttable.get_children())
            for row in rows:
                singlerow = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
                self.Studenttable.insert("",END,values=singlerow)
            connection.close()
                

############# form clear function ##########################
    def cleardata(self):
        message = messagebox.askyesno('do you want to clear form')
        if message > 0:
            self.e1.delete(0, END)
            self.e1.insert(END, str(randomnum))
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
            self.e7.current(0)
            self.e8.current(0)
            
                
        
############### get record function ################################################
    def getrecord(self, event):
       
        copy = self.Studenttable.focus()
        content = self.Studenttable.item(copy)
        row = content['values']
        if (len(row) !=0):
            self.e1.delete(0,END)
            self.e1.insert(END,row[1])
            self.e2.delete(0,END)
            self.e2.insert(END,row[2])
            self.e3.delete(0,END)
            self.e3.insert(END,row[3])
            self.e4.delete(0,END)
            self.e4.insert(END,row[4])
            self.e5.delete(0,END)
            self.e5.insert(END,row[5])
            self.e6.delete(0,END)
            self.e6.insert(END,row[6])
            self.e7.delete(0)
            self.e7.insert(END,row[7])
            self.e8.delete(0)
            self.e8.insert(END,row[8])


#################### update function ########################################################
    def update(self):
        if self.Nummer.get() == "" or self.Firstname.get() == "" or self.Lastname.get() == "" \
            or self.Age.get()== "" or self.Email.get()== ""or self.Phone.get() == "" \
            or self.Gender.get() == "" or self.Class.get() == "":
            messagebox.showerror("some fields are required")
        else:
            try:
                message = messagebox.askyesno("are you sure to update")
                if message > 0:
                    connection = sqlite3.connect("students.db")
                    cursor = connection.cursor()          
                    cursor.execute("UPDATE students SET Firstname=?,Lastname=?,Age=?, \
                    Email=?,Phone=?,Gender=?,Class=? where Nummer=?",(
                    self.Firstname.get(), self.Lastname.get(), self.Age.get(), self.Email.get(),
                    self.Phone.get(),  self.Gender.get(), self.Class.get(), self.Nummer.get()))
                    connection.commit()
                    self.showdata()
                    messagebox.showinfo("successfully updated")
                    self.cleardata()
                    connection.close()
            except:
                messagebox.showwarning('except not updated')                     
                  


############ delete function ############################################### 
    def deletestudent(self):
        if self.Nummer.get() == "" or self.Firstname.get() == "" or self.Lastname.get() == "":
            messagebox.showerror("some fields are required")
        else:
            try:
                    message = messagebox.askyesno("are you sure to delete")
                    if message > 0:
                        connection = sqlite3.connect("students.db")
                        cursor = connection.cursor()         
                        cursor.execute("DELETE from students where Nummer=?",(self.Nummer.get(),))                                                                    
                        connection.commit()
                        self.showdata()
                        self.cleardata()
                        connection.close()
                        messagebox.showinfo("deleted successfully")
            except:
                messagebox.showwarning('except not deleted')



######### exit function ##########################################################
    def exit(self):
            message = messagebox.askyesno("confirm if you want to exit")
            if message > 0:
                root.destroy()
            return 



########## search function ######################################################
    def searchdata(self):
        if self.Nummer.get() == "":
            messagebox.showerror("student nummer required")
        else:
            connection = sqlite3.connect('students.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students WHERE Nummer = ?", [self.e1.get()])
            rows = cursor.fetchall()
            if(len(rows)!=0):
                self.Studenttable.delete(*self.Studenttable.get_children())
                for row in rows:
                    self.Studenttable.insert('',END,values=row)
            connection.commit()
            connection.close()
        
    
if __name__=='__main__':
    root=Tk()
    obj = Student(root)
    root.mainloop()