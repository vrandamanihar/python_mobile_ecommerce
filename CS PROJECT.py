import os
import mysql.connector as sqltor
from tkinter import *
from PIL import Image, ImageTk
import tkinter
def wquit():
        print("WELCOME to the ONLINE_MOBILE_SHOPPEE ONE OF THE FINEST AND THE BEST ONILE MOBILE CENTRES.") 
def close_window():
        root.destroy()

root =tkinter.Tk()
root.title("ONLINE MOBILE SHOPPING")
root.geometry("600x800")
tkinter.Button(root,text='WELCOME LADIES AND GENTLEMEN.CLICK HERE AND VIEW THE MESSAGE ON IDLE',command=wquit).pack()
tkinter.Button(root,text="click here to quit this screen",command=close_window).pack()
class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("out.png")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)



e = Example(root)
e.pack(fill=BOTH, expand=YES)
root.mainloop()



mycon=sqltor.connect(host='localhost',user='root',passwd='27513471',charset="utf8")
if mycon.is_connected()==False:
    print('ERROR')
cursor=mycon.cursor()

cursor.execute("create database if not exists ONLINE_MOBILE_SHOPPING ")
cursor.execute("use ONLINE_MOBILE_SHOPPING")
cursor.execute("create table if not exists phone(MOBILE_ID integer primary key,\
                                   MOBILE_NAME char(20),\
                                   OS char(20),\
                                   RAM char(20),\
                                   STORAGE char(20),\
                                   EXPANDABLE_STORAGE char(20),\
                                   MANUFACTURER char(20),\
                                   PRODUCT_DIMENSIONS char(20),\
                                   COLOUR char(20),\
                                   WIRELESS_COMMUNICATIONS_TECHNOLOGY char(50),\
                                   SPECIAL_FEATURES varchar(200),\
                                   DEVICE_INTERFACE char(20),\
                                   RESOLUTION char(20),\
                                   REAR_CAMERA_IN_MP integer,\
                                   FRONT_CAMERA_IN_MP integer,\
                                   WEIGHT_IN_GRAMS integer,\
                                   BATTERY_In_MAH integer,\
                                   IN_BOX BLOB,\
                                   STOCK integer,\
                                   RATINGS_OUT_OF_5 float (3,2),\
                                   PRICE float(8,2),\
                                   SHIPPING char(20))")

###################################################################################################################################################
admin_id='ecommerce@cs.com'
password='12345'
#########################################################################################################################################################
cursor.execute("create table if not exists USERS(GMAIL_ACCOUNT char(50) primary key,\
PASSWORD CHAR(20) NOT NULL,\
name char(30),\
MOBILE_NUMBER varchar(30) unique NOT NULL,\
city char(50),\
address char(60))")
mycon.commit()
########################################################################################################################################################

#########################################################################################################################################################
def advance_features():
    MOBILE_ID=int(input('enter MOBILE_ID:'))
    query="select MOBILE_ID,MOBILE_NAME,EXPANDABLE_STORAGE,PRODUCT_DIMENSIONS,WIRELESS_COMMUNICATIONS_TECHNOLOGY,SPECIAL_FEATURES,DEVICE_INTERFACE,RESOLUTION,WEIGHT_IN_GRAMS,BATTERY_In_MAH,IN_BOX from  phone where MOBILE_ID='%s'"
    val=(MOBILE_ID,)
    cursor.execute(query,val)
    data=cursor.fetchall()
    c=[('MOBILE_ID','NAME','EXP_STORAGE','DIMENSIONS','WIFI_TECH','FEATURES','INTERFACE','RESOLUTION','WEIGHT','BATTERY','IN_BOX')]
    for row in data:
            a=(row,)
            b=list(a)
            c=c+b
    def table7():
            class Table7:
                    def __init__(self,root): 
                 # code for creating table 
                        for i in range(total_rows1): 
                                for j in range(total_columns1): 
                  
                                       self.e = Entry(root, width=15, fg='blue', 
                                                   font=('Arial',9))
                
                  
                                       self.e.grid(row=i, column=j)
                                       self.e.insert(END, c[i][j])
   
    # find total number of rows and 
    # columns in list 
            total_rows1 = len(c)
            total_columns1=len(c[0])
        

   
    # create root window 
            root= Tk() 
            root.title("THE PHONE TABLE")
            t=Table7(root)
    table7()
    root.mainloop()
##########################################################################################################################################       
def insert_mobile():
#to insert records in table mobile
    MOBILE_ID=int(input('Enter MOBILE_ID:'))
    MOBILE_NAME=input('Enter MOBILE_NAME:')
    OS=input('Enter OS:')
    RAM=input('Enter RAM:')
    STORAGE=input('Enter STORAGE:')
    EXPANDABLE_STORAGE=input('Enter EXPANDABLE_STORAGE:')
    MANUFACTURER=input('Enter MANUFACTURER:')
    PRODUCT_DIMENSIONS=input('Enter PRODUCT_DIMENSIONS:')
    COLOUR=input('Enter COLOUR:')
    WIRELESS_COMMUNICATIONS_TECHNOLOGY=input('Enter  WIRELESS_COMMUNICATIONS_TECHNOLOGY:')
    SPECIAL_FEATURES=input('Enter  SPEACIAL FEATURES:')
    DEVICE_INTERFACE=input('Enter  DEVICE INTERFERENCE:')
    RESOLUTION=input('Enter  RESOLUTION:')
    REAR_CAMERA_IN_MP=int(input('Enter REAR_CAMERA_IN_MP:'))
    FRONT_CAMERA_IN_MP=int(input('Enter FRONT_CAMERA_IN_MP:'))
    WEIGHT_IN_GRAMS=int(input('Enter WEIGHT_IN_GRAMS:'))
    BATTERY_In_MAH=int(input('Enter BATTERY_IN_MAH:'))
    IN_BOX=input('Enter IN_BOX:')
    STOCK=int(input('Enter STOCK:'))
    RATINGS_OUT_OF_5=float(input('Enter RATINGS_OUT_OF_5:'))
    PRICE=float(input('Enter PRICE:'))
    SHIPPING=input('Enter SHIPPING:')
    query="insert into phone values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(MOBILE_ID,\
         MOBILE_NAME,\
         OS,\
         RAM,\
         STORAGE,\
         EXPANDABLE_STORAGE,\
         MANUFACTURER,PRODUCT_DIMENSIONS,\
         COLOUR,WIRELESS_COMMUNICATIONS_TECHNOLOGY,SPECIAL_FEATURES,DEVICE_INTERFACE,RESOLUTION,\
         REAR_CAMERA_IN_MP,FRONT_CAMERA_IN_MP,WEIGHT_IN_GRAMS,BATTERY_In_MAH,IN_BOX,\
         STOCK,RATINGS_OUT_OF_5,PRICE,SHIPPING)
    cursor.execute(query,val)
    mycon.commit()
############################################################################################################################################################
def delete_mobile():
#to delete required records from table mobile
    M_ID=int(input('ENTER MOBILE_ID:'))
    query="delete from phone where MOBILE_ID=%s"
    val=(M_ID,)
    cursor.execute(query,val)
    mycon.commit()
############################################################################################################################################################
def update_mobile():
#to update the required record from table mobile
    COLOUR=input('Enter  NEW COLOUR:')
    STOCK=int(input('Enter NEW STOCK:'))
    RATINGS_OUT_OF_5=float(input('Enter NEW RATINGS_OUT_OF_5:'))
    PRICE=float(input('Enter NEW PRICE:'))
    MID=int(input('Enter MOBILE_ID:'))
    query="update phone set COLOUR=%s where MOBILE_ID=%s"
    val=(COLOUR,MID)
    cursor.execute(query,val)
    mycon.commit()
    #########################################################
    query="update phone set STOCK=%s where MOBILE_ID=%s"
    val=(STOCK,MID)
    cursor.execute(query,val)
    mycon.commit()
    ###########################################################
    query="update phone set RATINGS_OUT_OF_5=%s where MOBILE_ID=%s"
    val=(RATINGS_OUT_OF_5,MID)
    cursor.execute(query,val)
    mycon.commit()
    ############################################################
    query="update phone set PRICE=%s where MOBILE_ID=%s"
    val=(PRICE,MID)
    cursor.execute(query,val)
    mycon.commit()
        
#############################################################################################################################################################
def display_required_records():
# to display records according to MOBILE_ID
    MOBILE_ID=int(input('enter MOBILE_ID:'))
    query="select MOBILE_ID,MOBILE_NAME,OS,RAM,STORAGE,MANUFACTURER,COLOUR,REAR_CAMERA_IN_MP,FRONT_CAMERA_IN_MP,STOCK,RATINGS_OUT_OF_5,PRICE,SHIPPING from phone where MOBILE_ID='%s'"
    val=(MOBILE_ID,)
    cursor.execute(query,val)
    data=cursor.fetchall()
    c=[('MOBILE_ID','NAME','OS','RAM','STORAGE','MANUFACTURER','COLOR','REAR_CAMERA','FRONT_CAMERA','STOCK','RATINGS','PRICE','SHIPPING')]
    for row in data:
            a=(row,)
            b=list(a)
            c=c+b
            
    def table2():
            class Table1:
                    def __init__(self,root): 
                 # code for creating table 
                        for i in range(total_rows1): 
                                for j in range(total_columns1): 
                  
                                       self.e = Entry(root, width=11, fg='blue', 
                                                   font=('Arial',10))
                
                  
                                       self.e.grid(row=i, column=j)
                                       self.e.insert(END, c[i][j])
   
    # find total number of rows and 
    # columns in list 
            total_rows1 = len(c)
            total_columns1=len(c[0])
        

   
    # create root window 
            root= Tk() 
            root.title("THE PHONE TABLE")
            t=Table1(root)
    table2()
    root.mainloop()
###########################################################################################################################################################
def display_all_records():
# to display all records from table phone
      query="select MOBILE_ID,MOBILE_NAME,OS,RAM,STORAGE,MANUFACTURER,COLOUR,REAR_CAMERA_IN_MP,FRONT_CAMERA_IN_MP,STOCK,RATINGS_OUT_OF_5,PRICE,SHIPPING from phone"
      cursor.execute(query)
      data=cursor.fetchall()
      c=[('MOBILE_ID','NAME','OS','RAM','STORAGE','MANUFACTURER','COLOR','REAR_CAMERA','FRONT_CAMERA','STOCK','RATINGS','PRICE','SHIPPING')]
      for row in data:
                a=(row,)
                b=list(a)
                c=c+b
      def table1():

            
              class Table:
                def __init__(self,root): 
                         # code for creating table 
                  for i in range(total_rows): 
                    for j in range(total_columns): 
                          
                           self.e = Entry(root, width=11, fg='blue', 
                                       font=('Arial',10))
                        
                          
                           self.e.grid(row=i, column=j) 
                           self.e.insert(END, c[i][j])
   
    # find total number of rows and 
    # columns in list 
              total_rows = len(c)
              total_columns=len(c[0])
        

   
    # create root window 
              root= Tk() 
              root.title("THE PHONE TABLE")
    
              t=Table(root)
      table1()
      root.mainloop()  
    
          

            
###############################################################################################################################################################################################################################
def user_details():
# to display records of users
    query="select * from USERS "
    cursor.execute(query)
    data=cursor.fetchall()
    c=[]
    for row in data:
            a=(row,)
            b=list(a)
            c=c+b
    def table3():
            class Table3:
                    def __init__(self,root): 
                 # code for creating table 
                      for i in range(total_rows1): 
                                for j in range(total_columns1): 
                  
                                       self.e = Entry(root, width=30, fg='blue', 
                                                   font=('Arial',10))
                
                  
                                       self.e.grid(row=i, column=j) 
                                       self.e.insert(END, c[i][j])
   
    # find total number of rows and 
    # columns in list 
            total_rows1 = len(c)
            total_columns1=len(c[0])
        

   
    # create root window 
            root= Tk() 
            root.title("THE PHONE TABLE")
            t=Table3(root)
    table3()
    root.mainloop()

######################################################################################################################################################################
def sign_up():
#to insert into user table
    gmail_account=input("enter gmail_account:")
    password=input("enter password:")
    name=input("enter name:")
    contact_no=int(input('enter contact no:'))
    city=input('enter city:')
    address=input('enter address:')
    query="insert into USERS values(%s,%s,%s,%s,%s,%s)"
    val=(gmail_account,password,name,contact_no,city,address)
    cursor.execute(query,val)
    mycon.commit()
##########################################################################################################################################################################
def place_order():
#to place order for mobiles
    query1="create table if not exists payment(MOBILE_ID integer primary key,MOBILE_NAME char(20),PRICE float )as(select MOBILE_ID,MOBILE_NAME,PRICE from phone)"
    MOBILE_ID=int(input('enter MOBILE_ID:'))
    query2="select * from payment where MOBILE_ID=%s"
    val=(MOBILE_ID,)
    cursor.execute(query1)
    mycon.commit()
    cursor.execute(query2,val)
    data=cursor.fetchall()
    for row in data:
            print('='*50)
            print("MOBILE_ID:",row[0])
            print("MOBILE_NAME:",row[1])
            print("PRICE:",row[2])
###################################################################################################################################################################################
def sign_in():
# to sign in to already existing gmail account
    query="select GMAIL_ACCOUNT from USERS"
    cursor.execute(query)
    data=cursor.fetchall()
    rows1=[]
    for row in data:
        rows1=rows1+list(row)
    query="select PASSWORD from USERS"
    cursor.execute(query)
    data2=cursor.fetchall()
    rows2=[]
    for row2 in data2:
        rows2=rows2+list(row2)
    return rows1,rows2
a=sign_in()
####################################################################################################################################################################

def display_userdefined_records():
    def price():
        PRICE=int(input('enter suitable price:'))
        query="select MOBILE_ID,MOBILE_NAME,OS,RAM,STORAGE,MANUFACTURER,COLOUR,REAR_CAMERA_IN_MP,FRONT_CAMERA_IN_MP,STOCK,RATINGS_OUT_OF_5,PRICE,SHIPPING from  phone where PRICE between 0 and '%s'"
        val=(PRICE,)
        cursor.execute(query,val)
        data=cursor.fetchall()
        c=[('MOBILE_ID','NAME','OS','RAM','STORAGE','MANUFACTURER','COLOR','REAR_CAMERA','FRONT_CAMERA','STOCK','RATINGS','PRICE','SHIPPING')]
        for row in data:
                a=(row,)
                b=list(a)
                c=c+b
        def table4():
            class Table4:
                    def __init__(self,root): 
                 # code for creating table 
                        for i in range(total_rows1): 
                                for j in range(total_columns1): 
                  
                                       self.e = Entry(root, width=11, fg='blue', 
                                                   font=('Arial',10))
                
                  
                                       self.e.grid(row=i, column=j) 
                                       self.e.insert(END, c[i][j])
   
    # find total number of rows and 
    # columns in list 
            total_rows1 = len(c)
            total_columns1=len(c[0])
        

   
    # create root window 
            root= Tk() 
            root.title("THE PHONE TABLE")
            t=Table4(root)
        table4()
        root.mainloop()  
######################################################################        
    def company():
        COMPANY=input('enter suitable company:')
        query="select MOBILE_ID,MOBILE_NAME,OS,RAM,STORAGE,MANUFACTURER,COLOUR,REAR_CAMERA_IN_MP,FRONT_CAMERA_IN_MP,STOCK,RATINGS_OUT_OF_5,PRICE,SHIPPING from  phone where MANUFACTURER=%s"
        val=(COMPANY,)
        cursor.execute(query,val)
        data=cursor.fetchall()
        c=[('MOBILE_ID','NAME','OS','RAM','STORAGE','MANUFACTURER','COLOR','REAR_CAMERA','FRONT_CAMERA','STOCK','RATINGS','PRICE','SHIPPING')]
        for row in data:
                a=(row,)
                b=list(a)
                c=c+b
        def table5():
            class Table5:
                    def __init__(self,root): 
                 # code for creating table 
                        for i in range(total_rows1): 
                                for j in range(total_columns1): 
                  
                                       self.e = Entry(root, width=11, fg='blue', 
                                                   font=('Arial',10))
                
                  
                                       self.e.grid(row=i, column=j) 
                                       self.e.insert(END, c[i][j])
   
    # find total number of rows and 
    # columns in list 
            total_rows1 = len(c)
            total_columns1=len(c[0])
        

   
    # create root window 
            root= Tk() 
            root.title("THE PHONE TABLE")
            t=Table5(root)
        table5()
        root.mainloop()  
    print('1.SHOP BY PRICE\n2.SHOP BY COMPANY')
    CH='y'
    while CH=='y':
        ch=int(input('enter choice as 1,2:'))
        if ch==1:
            price()
        elif ch==2:
            company()
        print('1.SHOP BY PRICE\n2.SHOP BY COMPANY')
        CH=input('DO YOU WANT TO CONTINUE?enter choice y or n:')
        if CH=='n':
            break
####################################################################################################################################################################
'''MENU DRIVEN PROGRAM'''
while True:
    print("1.LOGIN AS ADMIN\n2.LOGIN AS USER\n3.EXIT")
    choice=int(input('enter choice as 1 or 2:'))
    if choice==1:
        CH='y'
        while CH=='y':
            
            adminid=input('enter your email id:')
            passwd=input('enter password:')
            if adminid==admin_id and passwd==password:
                print("WELCOME ADMIN")
                print("1.INSERT DETAILS INTO TABLE MOBILE\n2.DELETE DETAILS FROM TABLE MOBILE\n3.TO UPDATE DETAILS IN TABLE MOBILE \n4. TO SEE REQUIRED DETAILS FROM TABLE MOBILE\n5.TO SEE TABLE MOBILE\n6.TO SEE DETAILS OF CUSTOMERS")
                ch1=int(input('enter choice as 1,2,3,4,5,6:'))
                if ch1==1:
                    insert_mobile()
                    print('DO YOU WANT TO CONTINUE AS ADMIN')
                    CH=input("enter 'y' for yes and 'n' for no:")
                elif ch1==2:
                    delete_mobile()
                    print('DO YOU WANT TO CONTINUE AS ADMIN')
                    CH=input("enter 'y' for yes and 'n' for no:")
                elif ch1==3:
                    update_mobile()
                    print('DO YOU WANT TO CONTINUE AS ADMIN')
                    CH=input("enter 'y' for yes and 'n' for no:")
                elif ch1==4:
                    display_required_records()
                    print('DO YOU WANT TO SEE ADVANCE FEATUES?')
                    ch5=input('enter y for yes and n for no:')
                    if ch5=='y':
                            advance_features()
                    print('DO YOU WANT TO CONTINUE AS ADMIN')
                    CH=input("enter 'y' for yes and 'n' for no:")
                elif ch1==5:
                    display_all_records()
                    print('DO YOU WANT TO SEE ADVANCE FEATUES?')
                    ch5=input('enter y for yes and n for no:')
                    if ch5=='y':
                            advance_features()
                    print('DO YOU WANT TO CONTINUE AS ADMIN')
                    CH=input("enter 'y' for yes and 'n' for no:")
                elif ch1==6:
                    user_details()
                    print('DO YOU WANT TO CONTINUE AS ADMIN')
                    CH=input("enter 'y' for yes and 'n' for no:")
                else:
                    print('invalid choice')
            else:
                print("INCORRECT DETAILS")
                print('DO YOU WANT TO CONTINUE AS ADMIN')
                CH=input("enter 'y' for yes and 'n' for no:")
            
    elif choice==2:
        ch4='y'
        while ch4=='y':
            print("1.SIGN IN\n2.SIGN UP")
            ch2=int(input('enter choice as 1,2:'))
            if ch2==2:
                sign_up()
            elif ch2==1:
                a=sign_in()
                userid=input("enter user_id:")
                pas=input("enter password:")
                query="select name from USERS where GMAIL_ACCOUNT=%s"
                val=(userid,)
                cursor.execute(query,val)
                name=cursor.fetchone()
                userid=str(userid)
                passwd=str(pas)
                count=0
                count1=0
                for i in range(0,len(a[0])) :
                    if userid==a[0][i]:
                        count+=1
                        for j in range(0,len(a[1])):
                            if passwd==a[1][j]:
                                count1+=1
                                print('WELCOME',str(name))
                            
                if count==0 and count1==0:
                    print('incorrect details')
                    break
                elif count1==0:
                    print('incorrect passwd')
                    break
                elif count==0:
                    print('incorrect username')
                    break
                    
            else:
                print('INCORRECT CHOICE')
                break
              
            ch='y'
            while ch=='y':
                print('1.SEE DETAILS MOBILE\n2.PLACE ORDER\n3.FILTER')
                ch3=int(input('enter choice 1,2,3:'))
                if ch3==1:
                    display_all_records()
                    print('DO YOU WANT TO SEE ADVANCE FEATUES?')
                    ch5=input('enter y for yes and n for no:')
                    if ch5=='y':
                            advance_features()
                elif ch3==2:
                    place_order()
                    #cursor.execute("drop table payment")
                elif ch3==3:
                    display_userdefined_records()
                    print('DO YOU WANT TO SEE ADVANCE FEATUES?')
                    ch5=input('enter y for yes and n for no:')
                    if ch5=='y':
                            advance_features()
                else:
                    print('INCORRECT DETAILS')
                print('do you want to continue shopping')
                ch=input("enter 'y' for yes and 'n' for no:")
            print('do you want to enter as user')
            ch4=input("enter 'y' for yes and 'n' for no:")
        else:
            print('THANK YOU!!!')
    else:
        print('EXIT')
        break


