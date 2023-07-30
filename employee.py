from tkinter import*
from tkinter import messagebox,ttk
import pymysql
import time
class EmplyoeeSystem:
    def __init__(self, node):
        self.node=node
        self.node.title("Employe Payroll System")
        self.node.geometry("1350x700+0+0")
        self.node.config(bg="white")
        title=Label(self.node,text="Employee Payroll System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        btn_show_employees=Button(self.node,text="Employee Details",command=self.employee_frame,font=("times new roman",13),bg="lightblue",fg="black").place(x=1100,y=10, height=30, width=150)


        #Frame1
        Frame1=Frame(self.node,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=580,height=300)

        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_medical=StringVar()
        self.var_fund=StringVar()
        self.var_convenence=StringVar()
        self.var_salary=StringVar()
        self.var_net=StringVar()
        self.var_absent=StringVar()
        self.var_t_days=StringVar()

        title1=Label(Frame1,text="Employee Salary Details",font=("times new roman",20),bg="LIGHTGRAY",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lbl_month=Label(Frame1,text="Month",font=("times new roman",18),bg="white",fg="black").place(x=10,y=60)
        text_month=Entry(Frame1,font=("times new roman",15),textvariable=self.var_month,bg="LIGHTyellow",fg="black").place(x=90,y=62,width=80)

        lbl_year=Label(Frame1,text="Year",font=("times new roman",18),bg="white",fg="black").place(x=190,y=60)
        text_year=Entry(Frame1,font=("times new roman",15),textvariable=self.var_year,bg="LIGHTyellow",fg="black").place(x=250,y=62,width=80)
        
        lbl_salary=Label(Frame1,text="Base Salary",font=("times new roman",18),bg="white",fg="black").place(x=360,y=60)
        text_salary=Entry(Frame1,font=("times new roman",15),textvariable=self.var_salary,bg="LIGHTyellow",fg="black").place(x=490,y=62,width=80)

        #row1
        lbl_days=Label(Frame1,text="Total Days",font=("times new roman",18),bg="white",fg="black").place(x=10,y=100)
        text_days=Entry(Frame1,font=("times new roman",15),textvariable=self.var_t_days,bg="LIGHTyellow",fg="black").place(x=140,y=105,width=100)
        lbl_absent=Label(Frame1,text="Absent",font=("times new roman",18),bg="white",fg="black").place(x=260,y=100)
        text_absent=Entry(Frame1,font=("times new roman",15),textvariable=self.var_absent,bg="LIGHTyellow",fg="black").place(x=370,y=105, width=100)

        #row2
        lbl_medical=Label(Frame1,text="Medical",font=("times new roman",18),bg="white",fg="black").place(x=10,y=150)
        text_medical=Entry(Frame1,font=("times new roman",15),textvariable=self.var_medical,bg="LIGHTyellow",fg="black").place(x=140,y=155,width=100)
        lbl_fund=Label(Frame1,text="Provident Fund",font=("times new roman",18),bg="white",fg="black").place(x=260,y=150)
        text_fund=Entry(Frame1,font=("times new roman",15),textvariable=self.var_fund,bg="LIGHTyellow",fg="black").place(x=430,y=155, width=100)        

        #row3
        lbl_convenence=Label(Frame1,text="Convenence",font=("times new roman",18),bg="white",fg="black").place(x=10,y=190)
        text_convenence=Entry(Frame1,font=("times new roman",15),textvariable=self.var_convenence,bg="LIGHTyellow",fg="black").place(x=140,y=195,width=100)
        lbl_net=Label(Frame1,text="Net Salary",font=("times new roman",18),bg="white",fg="black").place(x=260,y=190)
        text_net=Entry(Frame1,font=("times new roman",15),textvariable=self.var_net,bg="LIGHTyellow",fg="black").place(x=370,y=195, width=200)      

        #row4
        btn_calculate=Button(Frame1,text="Calculate",command=self.calculate,font=("times new roman",20),bg="lightgray",fg="black").place(x=180,y=240, height=30, width=120)
        btn_save=Button(Frame1,text="Save",command=self.add,font=("times new roman",20),bg="lightgray",fg="black").place(x=310,y=240, height=30, width=120)
        btn_clear=Button(Frame1,text="Clear",font=("times new roman",20),bg="lightgray",fg="black").place(x=440,y=240, height=30, width=120)

        #frame2
        Frame2=Frame(self.node,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=10,y=380,width=580,height=310)

        #----------Calculator----------
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)    
            self.var_operator=''
        def clear_cal():
            self.var_txt.set('')    
            self.var_operator=''

        cal_frame=Frame(Frame2,bg="white",bd=2,relief=RIDGE)
        cal_frame.place(x=2,y=2,width=247,height=300)

        txt_result=Entry(cal_frame,bg="lightyellow",textvariable=self.var_txt,font=("times new roman",20,"bold")).place(x=0,y=0,relwidth=1,height=50)

        #row1
        btn_7=Button(cal_frame,text="7",command=lambda:btn_click(7),font=("times new roman",15,"bold")).place(x=0,y=53,w=60,height=60)
        btn_8=Button(cal_frame,text="8",command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=61,y=53,w=60,height=60)
        btn_9=Button(cal_frame,text="9",command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=122,y=53,w=60,height=60)
        btn_r=Button(cal_frame,text="/",command=lambda:btn_click('/'),font=("times new roman",15,"bold")).place(x=183,y=53,w=60,height=60)

        #row2
        btn_4=Button(cal_frame,text="4",command=lambda:btn_click(4),font=("times new roman",15,"bold")).place(x=0,y=113,w=60,height=60)
        btn_5=Button(cal_frame,text="5",command=lambda:btn_click(5),font=("times new roman",15,"bold")).place(x=61,y=113,w=60,height=60)
        btn_6=Button(cal_frame,text="6",command=lambda:btn_click(6),font=("times new roman",15,"bold")).place(x=122,y=113,w=60,height=60)
        btn_m=Button(cal_frame,text="*",command=lambda:btn_click('*'),font=("times new roman",15,"bold")).place(x=183,y=113,w=60,height=60)

        #row3
        btn_1=Button(cal_frame,text="1",command=lambda:btn_click(1),font=("times new roman",15,"bold")).place(x=0,y=173,w=60,height=60)
        btn_2=Button(cal_frame,text="2",command=lambda:btn_click(2),font=("times new roman",15,"bold")).place(x=61,y=173,w=60,height=60)
        btn_3=Button(cal_frame,text="3",command=lambda:btn_click(3),font=("times new roman",15,"bold")).place(x=122,y=173,w=60,height=60)
        btn_s=Button(cal_frame,text="-",command=lambda:btn_click('-'),font=("times new roman",15,"bold")).place(x=183,y=173,w=60,height=60)

        #row4
        btn_0=Button(cal_frame,text="0",command=lambda:btn_click(0),font=("times new roman",15,"bold")).place(x=0,y=233,w=60,height=60)
        btn_f=Button(cal_frame,text="AC",command=clear_cal,font=("times new roman",15,"bold")).place(x=61,y=233,w=60,height=60)
        btn_p=Button(cal_frame,text="+",command=lambda:btn_click('+'),font=("times new roman",15,"bold")).place(x=122,y=233,w=60,height=60)
        btn_e=Button(cal_frame,text="=",command=result,font=("times new roman",15,"bold")).place(x=183,y=233,w=60,height=60)

        #Salary Frame
        sal_frame=Frame(Frame2,bg="white",bd=2,relief=RIDGE)
        sal_frame.place(x=251,y=2,width=320,height=300)
        title_sal1=Label(sal_frame,text="Salary Reciept",font=("times new roman",20),bg="LIGHTGRAY",fg="black",anchor="w",padx=10).place(x=3,y=1,width=320)

        sal_frame2=Frame(Frame2,bg="white",bd=2,relief=RIDGE)
        sal_frame2.place(x=254,y=37,width=318,height=220)
        sample = f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
-----------------------------------------
Employee ID\t\t:  
Salary of\t\t:  DD-MM-YYYY
Generated On\t\t:  DD-MM-YYYY
-----------------------------------------
Total Days\t\t:  DD
Total Present\t\t:  DD
Total Absent\t\t:  DD
Convence\t\t:  Rs.----
Medical\t\t:  Rs.----
PF\t\t:  Rs. ----
Gross Payment \t\t:  Rs.------
Net Salary\t\t:  Rs.-----
-----------------------------------------
This is computer generated slip, not
required any signature
'''

        scroll_y=Scrollbar(sal_frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_recipt=Text(sal_frame2,font=("times new roman",15),bg='lightyellow', yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)
        self.txt_salary_recipt.insert(END,sample)

        btn_print=Button(sal_frame,text="Print",font=("times new roman",20),bg="lightblue",fg="black").place(x=180,y=260, height=30, width=120)



        #frame3
        #variables
        self.var_emp_code=StringVar()
        self.var_designstion=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_proof_id=StringVar() #aadhar card as a proof Id
        self.var_contact=StringVar()
        self.var_status=StringVar()
        self.var_experience=StringVar()
        self.var_address=StringVar()

        Frame3=Frame(self.node,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=600,y=70,width=930,height=620)
        title3=Label(Frame3,text="Employee Details",font=("times new roman",20),bg="LIGHTGRAY",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        lbl_code=Label(Frame3,text="Employee Code",font=("times new roman",20),bg="white",fg="black").place(x=10,y=70)
        text_code=Entry(Frame3,font=("times new roman",15),textvariable=self.var_emp_code,bg="LIGHTyellow",fg="black").place(x=210,y=74,width=200)
        # btn_search=Button(Frame3,text="Search",font=("times new roman",20),bg="lightgray",fg="black").place(x=440,y=72, height=30)

        #row1
        lbl_designation=Label(Frame3,text="Designation",font=("times new roman",20),bg="white",fg="black").place(x=10,y=120)
        text_designation=Entry(Frame3,font=("times new roman",15),textvariable=self.var_designstion,bg="LIGHTyellow",fg="black").place(x=170,y=125,width=200)
        lbl_dob=Label(Frame3,text="D.O.B",font=("times new roman",20),bg="white",fg="black").place(x=430,y=120)
        text_dob=Entry(Frame3,font=("times new roman",15),textvariable=self.var_dob,bg="LIGHTyellow",fg="black").place(x=570,y=125)

        #row2
        lbl_Name=Label(Frame3,text="Name",font=("times new roman",20),bg="white",fg="black").place(x=10,y=180)
        text_Name=Entry(Frame3,font=("times new roman",15),textvariable=self.var_name,bg="LIGHTyellow",fg="black").place(x=170,y=185,width=200)
        lbl_doj=Label(Frame3,text="D.O.J",font=("times new roman",20),bg="white",fg="black").place(x=430,y=180)
        text_doj=Entry(Frame3,font=("times new roman",15),textvariable=self.var_doj,bg="LIGHTyellow",fg="black").place(x=570,y=185)        

        #row3
        lbl_age=Label(Frame3,text="Age",font=("times new roman",20),bg="white",fg="black").place(x=10,y=230)
        text_age=Entry(Frame3,font=("times new roman",15),textvariable=self.var_age,bg="LIGHTyellow",fg="black").place(x=170,y=235,width=200)
        lbl_experience=Label(Frame3,text="Experience",font=("times new roman",20),bg="white",fg="black").place(x=430,y=230)
        text_experience=Entry(Frame3,font=("times new roman",15),textvariable=self.var_experience,bg="LIGHTyellow",fg="black").place(x=570,y=235)      

        #row4
        lbl_gender=Label(Frame3,text="Gender",font=("times new roman",20),bg="white",fg="black").place(x=10,y=280)
        text_gender=Entry(Frame3,font=("times new roman",15),textvariable=self.var_gender,bg="LIGHTyellow",fg="black").place(x=170,y=285,width=200)
        lbl_proof=Label(Frame3,text="Proof ID",font=("times new roman",20),bg="white",fg="black").place(x=430,y=280)
        text_proof=Entry(Frame3,font=("times new roman",15),textvariable=self.var_proof_id,bg="LIGHTyellow",fg="black").place(x=570,y=285)  

        #row5
        lbl_email=Label(Frame3,text="Email",font=("times new roman",20),bg="white",fg="black").place(x=10,y=330)
        text_email=Entry(Frame3,font=("times new roman",15),textvariable=self.var_email,bg="LIGHTyellow",fg="black").place(x=170,y=335,width=200)
        lbl_contact=Label(Frame3,text="Contact",font=("times new roman",20),bg="white",fg="black").place(x=430,y=330)
        text_contact=Entry(Frame3,font=("times new roman",15),textvariable=self.var_contact,bg="LIGHTyellow",fg="black").place(x=570,y=335)   

        #row6
        lbl_address=Label(Frame3,text="Address",font=("times new roman",20),bg="white",fg="black").place(x=10,y=430)
        self.text_address=Text(Frame3,font=("times new roman",15),bg="LIGHTyellow",fg="black").place(x=170,y=435,width=600,height=100)

        self.check_connection()

    def add(self):
        if self.var_emp_code.get()=='' or self.var_net.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error", "Employee details are Required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                rows=cur.fetchone()
                # print(rows)
                if rows!= None:
                    messagebox.showerror("Error","This employee ID is already available in our record, try again with another ID", parent=self.node)
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (
                                self.var_emp_code.get(),
                                self.var_designstion.get(),
                                self.var_name.get(),
                                self.var_age.get(),
                                self.var_gender.get(),
                                self.var_email.get(),
                                self.var_dob.get(),
                                self.var_doj.get(),
                                self.var_experience.get(),
                                self.var_proof_id.get(),
                                self.var_contact.get(),
                                self.var_address.get(),
                                self.var_month.get(),
                                self.var_year.get(),
                                self.var_salary.get(),
                                self.var_t_days.get(),
                                self.var_absent.get(),
                                self.var_medical.get(),
                                self.var_convenence.get(),
                                self.var_fund.get(),
                                self.var_net.get(),
                                "reciept"
                            )
                            )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Record added Successfully")
                
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to{str(ex)}')



    def calculate(self):
        if self.var_month.get()=='' or self.var_year=='' or self.var_convenence=='' or self.var_absent==''or self.var_medical=='':
            messagebox.showerror("error","All feilds are Required")
        else:
            #self.var_net_salary.set("RESULT")
            #35000/31--1752
            #31-10-21 1752
            per_day=int(self.var_salary.get())/int(self.var_t_days.get())
            work_day=int(self.var_t_days.get())-int(self.var_absent.get())
            sal_=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_fund.get())
            addition=int(self.var_convenence.get())
            net_sal=sal_-deduct+addition
            self.var_net.set(str(round(net_sal,2)))
            #update the reciept
            new_sample = f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
-----------------------------------------
Employee ID\t\t:  {self.var_emp_code.get()}
Salary of\t\t:  {self.var_month.get()}-{self.var_year.get()}
Generated On\t\t:  {str(time.strftime("%d-%M-%Y"))}
-----------------------------------------
Total Days\t\t:  {self.var_t_days.get()}
Total Present\t\t:  {self.var_t_days.get()}-{self.var_absent.get()}
Total Absent\t\t:  {self.var_absent.get()}
Convence\t\t:  {self.var_convenence.get()}
Medical\t\t:  {self.var_medical.get()}
PF\t\t:  {self.var_fund.get()}
Gross Payment \t\t:  {self.var_salary.get()}
Net Salary\t\t:  {self.var_net.get()}
-----------------------------------------
This is computer generated slip, not
required any signature
'''
            self.txt_salary_recipt.delete('1.0',END)
            self.txt_salary_recipt.insert(END,new_sample)


    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            print(rows)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to{str(ex)}')

    def show(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()    
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to{str(ex)}')        


    def employee_frame(self):
        self.node2=Toplevel(self.node)
        self.node2.title("Employe Payroll System")
        self.node2.geometry("900x500+120+100")
        self.node2.config(bg="white")
        title=Label(self.node2,text="All Employee Details",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).pack(side=TOP,fill=X)
        self.node2.focus_force()

        Scrolly=Scrollbar(self.node2,orient=VERTICAL)
        Scrollx=Scrollbar(self.node2,orient=HORIZONTAL)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)


        self.employee_tree=ttk.Treeview(self.node2,columns=('e_id', 'designation', 'name', 'age', 'gender', 'email', 'dob', 'doj', 'experience', 'proof_id', 'contact', 'address', 'month', 'year', 'basic_salary', 'total_days', 'absents', 'medical', 'convenence', 'provident_fund', 'net_sal', 'receipt'), yscrollcommand=Scrolly.set,xscrollcommand=Scrollx.set)
        self.employee_tree.heading('e_id', text='E ID')
        self.employee_tree.heading('designation', text='Designation')
        self.employee_tree.heading('name', text='Name')
        self.employee_tree.heading('age', text='Age')
        self.employee_tree.heading('gender', text='Gender')
        self.employee_tree.heading('email', text='Email')
        self.employee_tree.heading('dob', text='DOB')
        self.employee_tree.heading('doj', text='DOJ')
        self.employee_tree.heading('experience', text='Experience')
        self.employee_tree.heading('proof_id', text='Proof Id')
        self.employee_tree.heading('contact', text='Contact')
        self.employee_tree.heading('address', text='Address')
        self.employee_tree.heading('month', text='Month')
        self.employee_tree.heading('year', text='Year')
        self.employee_tree.heading('basic_salary', text='Basic Salary')
        self.employee_tree.heading('total_days', text='Total Days')
        self.employee_tree.heading('absents', text='Absents')
        self.employee_tree.heading('medical', text='Medical')
        self.employee_tree.heading('convenence', text='Convenence')
        self.employee_tree.heading('provident_fund', text='PF')
        self.employee_tree.heading('net_sal', text='Net Salary')
        self.employee_tree.heading('receipt', text='Receipt')
        self.employee_tree['show']='headings'

        self.employee_tree.column('e_id', width= 50)
        self.employee_tree.column('designation', width=100)
        self.employee_tree.column('name', width=100)
        self.employee_tree.column('age', width=100)
        self.employee_tree.column('gender', width=100)
        self.employee_tree.column('email', width=100)
        self.employee_tree.column('dob', width=100)
        self.employee_tree.column('doj', width=100)
        self.employee_tree.column('experience', width=100)
        self.employee_tree.column('proof_id', width=100)
        self.employee_tree.column('contact', width=100)
        self.employee_tree.column('address', width=200)
        self.employee_tree.column('month', width=100)
        self.employee_tree.column('year', width=100)
        self.employee_tree.column('basic_salary', width=100)
        self.employee_tree.column('total_days', width=100)
        self.employee_tree.column('absents', width=100)
        self.employee_tree.column('medical', width=100)
        self.employee_tree.column('convenence', width=100)
        self.employee_tree.column('provident_fund', width=100)
        self.employee_tree.column('net_sal', width=100)
        self.employee_tree.column('receipt', width=100)
        Scrollx.config(command=self.employee_tree.xview)
        Scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH, expand=1)
        self.show()



        self.node2.mainloop()


node=Tk()
obj=EmplyoeeSystem(node)
node.mainloop()