import mysql.connector as msq
import datetime
import random
from tabulate import tabulate con=msq.connect(host="localhost",user="root",password="anna@cs",data base="project")
if con.is_connected:
         print('Connection Successful')
else:
         print('Check connection')
print('\n\n\n\n')
print('*'*188)
print('   '*25,'WELCOME!')
print('*'*188)
cur=con.cursor()
#FINAL-est  PROJECT
def createtablecustomers():
    query="create table if not exists customers_(cpr int(50) unique, name varchar(30), address varchar(30), if_working varchar(5)\
, place_of_work varchar(35), gender char(10), phone_no varchar(20), lisence_no varchar(25), customer_id varchar(30) primary key,car_id varchar(30) unique, \
status_of_customer varchar(10))"
    cur.execute(query)
createtablecustomers()
def create_table_all_cars(): 
         query="create table if not exists all_cars(Manufacture_yr date, Type varchar(20),\
       Company varchar(20), Model varchar(20), Car_id varchar(30) unique,Plate_no varchar(10) primary key ,\
       Status varchar(20),rent_day int, rent_week int, rent_month int)"
         cur.execute(query)
create_table_all_cars()
def createtable():
    query = 'CREATE TABLE if not exists members (car_id VARCHAR(20) unique,\
            plate_no varchar(10) primary key, rent_date DATE, return_date DATE, amount INT)'
    cur.execute(query)
    con.commit()
createtable()
## CUSTOMER #####
def header_customers(data):
         if not data:
                  print('\t  Match not found')
else:
print(tabulate(data,headers=['CPR','Name','Address'\
                                            ,'If_working','Place_Of_ work','Gender'\
                                            ,'Phone_no','Lisence_no' ,'Customer_id','Car_id','Status_of_customer'],tablefmt='fancy_grid') )
def insertrecord():
    try:
                  print(end='\t  ')
                  cpr=int(input("Enter Cpr  :  "))
                  q="select status_of_customer from customers_ where cpr='{}' ".format(cpr)
                  cur.execute(q)
                  r=cur.fetchall()
                  if cur.rowcount==0:
                      pass
                  elif r[0][0]=='NEW':
                      print('\t  We only allow rent one car per person at a time')
                      raise 
                  print(end='\t  ')
                  name=input("Enter Name  :  ").upper()
                  print(end='\t  ')
                  address=input("Enter Address  :  ").upper()
                  print(end='\t  ')
                  gender=input("Enter Gender (Female/Male)  :  ").upper()
                  print(end='\t  ')
                  phone_no=input("Enter phone no  :  ")
                  print(end='\t  ')
                  lisence_no=input("Enter lisence_no  :  ").upper()
                  print(end='\t  ')
                  for j in range(1):
                           custid=''
                           for k in range(4):
numberhalf=str(random.randint(0,9))
letterhalf=chr(random.randint(ord('A'),ord('Z')))
                                    custid+=numberhalf
                                    custid+=letterhalf
                           print('Your customer id is:',custid)
                  customer_id=custid.upper()
                  print(end='\t  ')
                  car_id=input("Enter car_id  :  ").upper()
                  cur.execute("select * from all_cars where car_id='{}'".format(car_id))
                  data=cur.fetchall()
                  if not data:
                      print("\t  Sorry, this car does not exists")
                      return
                  q="update all_cars set status='NOT AVAILABLE' where car_id='{}'".format(car_id)
                  cur.execute(q)
                  con.commit()
                  status='NEW'
                  query="insert into customers_(cpr, name, address, gender, phone_no,lisence_no, 
customer_id ,car_id,status_of_customer)values\
({},'{}','{}','{}','{}','{}','{}','{}','{}')".format(cpr, name, address,  gender, phone_no, lisence_no, customer_id ,car_id,status)                   cur.execute(query)
                  con.commit()
                  print(end='\t  ')
                  if_working=input("Enter working or not working(Yes/No)  :  ").upper()
                  if if_working=='NO':
                           q="update customers_ set if_working='NO' where cpr='{}'".format(cpr)
                           cur.execute(q)
                           con.commit()
                  elif if_working=='YES':
                           print(end='\t  ')
                           place_of_work=input("Enter Place of 
work  :  ").upper()
                           q="update customers_ set if_working='YES',place_of_work='{}' where cpr='{}'".format(place_of_work,cpr)
                           cur.execute(q)
                           con.commit()
                  query="SELECT * from customers_ where cpr='{}'".format(cpr)
                  cur.execute(query)
                  data=cur.fetchall()
                  header_customers(data)
    except:
        print('\t  Duplicate entry; try again')
    else:
        print('\t  Please fill out rented car details as well')
def searchcpr():
         print(end='\t  ')
         cpr=int(input("Enter Cpr  :  "))
         query="SELECT * from customers_ where cpr='{}'".format(cpr)          cur.execute(query)
         data=cur.fetchall()
         header_customers(data)
def searchname():
         print(end='\t  ')
         name=input('Enter Name  :  ')
         s="SELECT * from customers_ where name like '%{}
%'".format(name)
         cur.execute (s)
         data=cur.fetchall()
         header_customers(data)
def searchplace_of_work():
    print(end='\t  ')
    place_of_work=input('Enter Place of work  :  ')     s="SELECT * from customers_ where place_of_work='{}'".format(place_of_work)
    cur.execute (s)
    data=cur.fetchall()
    header_customers(data)
def searchgender():
    print(end='\t  ')
    gender=input('Enter Female/Male  :  ')
    s="SELECT * from customers_ where gender='{}'".format(gender)     cur.execute (s)
    data=cur.fetchall()
    header_customers(data)
def searchphone_no():
    print(end='\t  ')
    phone_no=input('Enter phone no  :  ')     s="SELECT * from customers_ where phone_no='{}'".format(phone_no)
    cur.execute (s)
    data=cur.fetchall()
    header_customers(data)
def searchif_working():
    print(end='\t  ')
    if_working=input('Enter if working of not (yes/no) :  ')     s="SELECT * from customers_ where if_working='{}'".format(if_working)
    cur.execute (s)
    data=cur.fetchall()
    header_customers(data)
def searchcustomer_id():
    print(end='\t  ')
    customer_id=input('Enter customer id  :  ')     s="SELECT * from customers_ where customer_id='{}'".format(customer_id)
    cur.execute (s)
    data=cur.fetchall()
    header_customers(data)
def searchaddress():
    print(end='\t  ')
    address=input('Enter address  :  ')
    s="SELECT * from customers_ where address='{}'".format(address)     cur.execute (s)
data=cur.fetchall() header_customers(data)
#del 
def deletecpr():
    print(end='\t  ')
    cpr=int(input("Enter Cpr  : "))
    query="select * from customers_ where cpr='{}'".format(cpr)
    cur.execute(query)
    r=cur.fetchall()
    if cur.rowcount==0:
        print('\t  No match found')
    else:
        q="select car_id from customers_ where cpr='{}'".format(cpr)         cur.execute(q)
        for i in cur:
            carid=i[0]
        q="update all_cars set status='AVAILABLE' where car_id='{}'".format(carid)
        cur.execute(q)
        con.commit()
        q="delete from members where car_id='{}'".format(carid)
        cur.execute(q)
        con.commit()
        query="Delete from customers_ where cpr='{}'".format(cpr)
        cur.execute(query)
        con.commit()
        print('\t  Required data has been deleted')
def deletecustomer_id():
    print(end='\t  ')
    customer_id=input('Enter customer id  : ')
    query="select * from customers_ where customer_id='{}'".format(customer_id)
    cur.execute(query)
    r=cur.fetchall()
    if cur.rowcount==0:
        print('\t  No match found')
    else:
        q="select car_id from customers_ where customer_id='{}'".format(customer_id)
        cur.execute(q)
        for i in cur:
            carid=i[0]
        q="update all_cars set status='AVAILABLE' where car_id='{}'".format(carid)
        cur.execute(q)
        con.commit()
        q="delete from members where car_id='{}'".format(carid)         cur.execute(q)
        con.commit()
        query="Delete from customers_ where customer_id='{}'".format(customer_id)
        cur.execute(query)
        con.commit()
        print('\t  Required data has been deleted')
#update
def updateaddress(cus_id):
    print(end='\t  ')
    address=input('Enter address  : ')
    print(end='\t  ')
    newaddress=input('Enter new address  : ').upper()     s="update customers_ set address='{}' where customer_id='{}'".format(newaddress,cus_id)
    cur.execute (s)
    con.commit()
def updatecpr():
    print(end='\t  ')
    cpr=int(input("Enter CPR  : "))
    print(end='\t  ')
    new_cpr=int(input('Enter new CPR  : '))
    query="Update customers_ set cpr={} where cpr={}".format(new_cpr,cpr)
    cur.execute(query)
    con.commit()
def updatename(cus_id):
    print(end='\t  ')
    name=input('Enter name  :')
    print(end='\t  ')
    new_name=input('Enter new_name  : ').upper()     s="Update customers_ set name='{}' where customer_id='{}'".format(new_name,cus_id)
    cur.execute (s)
    con.commit()
def  updateplace_of_work(cus_id):
    print(end='\t  ')
    place_of_work=input('Enter place of work  : ')
    print(end='\t  ')
    new_place_of_work=input('Enter new place of work  : ').upper()     s="Update customers_ set  place_of_work='{}' where customer_id='{}'".format(new_place_of_work,cus_id)
    cur.execute (s)
    con.commit()
def updatephone_no():
    print(end='\t  ')
    phone_no=input('Enter phone no  : ')     print(end='\t  ')
    new_phone_no=input('Enter new phone no  : ')
    s="update customers_ set phone_no='{}'  where phone_no='{}'".format(new_phone_no,phone_no)
    cur.execute (s)
    con.commit()
def updateif_working(cus_id):
         print(end='\t  ')
         if_working=input('Were you working before? (yes/no)  :  ').upper()
         if if_working == 'YES':
                  print("\t  You are updating 'Working' to 'Not working'")
                  update='NO'
         elif if_working == 'NO':
                  print("\t  You are updating ' Not Working' to 'Working'")
                  update='YES'
         s="Update customers_ set if_working='{}' where customer_id='{}'".format(update,cus_id)
         cur.execute (s)
         con.commit()
         if update =='YES' and if_working =='NO':
                  print(end='\t  ')
                  place=input('Enter place of work').upper()
                  q="update customers_ set place_of_work='{}' where customer_id ='{}'".format(place,cus_id)      
         elif update =='NO' and if_working =='YES':
                  q="update customers_ set place_of_work=null where customer_id ='{}'".format(cus_id)
cur.execute(q) con.commit()
def displaycust():
         q="select * from customers_"          cur.execute(q)
         data=cur.fetchall()
         header_customers(data)
#### ALL CARS #########
#display for headers
def header_all_cars(data):
         if not data:
                  print('\t  Match not found')
         else:
                  print(tabulate(data,headers=['Manufacture year','Type','Company'\
                                            ,'Model','Car id','Plate_no','Status'\
                                            ,'Rent per day','rent per week','Rent per month'],tablefmt='fancy_grid'))
#search fns
def searchcar_manf():
         manf=input('\t   Enter manufacture year (yyyy-mm-dd)  :  ')          query="select * from all_cars where manufacture_yr='{}'".format(manf)
         cur.execute(query)
         data=cur.fetchall()
         header_all_cars(data)
def searchcar_type():
         print('\t   TYPES AVAILABLE: \n\t\tXLarge\n\t\tLarge\n\t\tMedium\n\t\tSmall\n\t\tCruiser\n')
         tpe=input('\t   Enter type of car  :  ')
         query="select * from all_cars where type='{}'".format(tpe)          cur.execute(query)
         data=cur.fetchall()
         header_all_cars(data)
def searchcar_company():
         print('COMPANY AVAILABLE: \n\tHyundai\n\tHonda\n\tChevrolet\n\tToyota\n\tKia\n\tSkoda\n\tNissa n\n')         
         company=input('Enter company name  :  ')
         query="select * from all_cars where company='{}'".format(company)
         cur.execute(query)
         data=cur.fetchall()
         header_all_cars(data)
def searchcar_model():
         print('MODELS AVAILABLE: \n\tMinivan\n\tCUV\n\tSUV\n\tSedan\n\tMicro\n')          model=input('Enter model:')
         query="select * from all_cars where model='{}'".format(model)
         cur.execute(query)
         data=cur.fetchall()
         header_all_cars(data)
def searchcar_carid():
         carid=input('Enter car id:')
         query="select * from all_cars where car_id='{}'".format(carid)
         cur.execute(query)
         data=cur.fetchall()
         header_all_cars(data)
def searchcar_status():
         status=input('Enter status (available/not available)  : ')          query="select * from all_cars where status='{}'".format(status)
         cur.execute(query)
         data=cur.fetchall()
         header_all_cars(data)
def searchcar_rentd():
         rentd=int(input('Enter rent per day  : '))          query="select * from all_cars where rent_day={}".format(rentd)
         cur.execute(query)
         data=cur.fetchall()
         header_all_cars(data)
def searchcar_rentw():
         rentw=int(input('Enter rent per week  : '))          query="select * from all_cars where rent_week={}".format(rentw)
         cur.execute(query)
         data=cur.fetchall()
         header_all_cars(data)
def searchcar_rentm():
         rentm=int(input('Enter rent per month  : '))          query="select * from all_cars where rent_month={}".format(rentm)
         cur.execute(query)
         data=cur.fetchall()
         header_all_cars(data)
#insert fn
def insert_vals():
    try:
                  day=int(input('\t   Enter date of manufacturing:'))
                  month=int(input('\t   Enter month of manufacturing:'))
                  yr=int(input('\t   Enter yr of manufacturing:'))
                  dt=str(datetime.date(yr,month,day))
                  ty=input('\t   Enter type').upper()
                  com=input('\t   Enter company name:').upper()
                  mod=input('\t   Enter model').upper()
                  caid=input('\t   Enter car id').upper()
                  stat=input('\t   Enter status:').upper()
                  rentd=int(input('\t   Enter rent per day:'))
                  rentw=input('\t   Enter rent per week:')
                  rentm=input('\t   Enter rent per month:')
                  plate=input('\t   Enter plate number: ').upper()
                  query="insert into all_cars values(%s,%s,%s,%s,%s, %s,%s,%s,%s,%s)" data=(dt,ty,com,mod,caid,plate,stat,rentd,rentw,rentm)                   cur.execute(query,data)
                  con.commit()
    except:
        print('Dup entery; try again')
#delete fns
def del_carid():
    carid=input('\t   Enter car id  : ')
    q="Select * from all_cars where car_id='{}'".format(carid)
    cur.execute(q)
    r=cur.fetchall()
    if cur.rowcount==0:
        print('\t   No match found')
    else:
        query="delete from all_cars where car_id='{}'".format(carid)         cur.execute(query)
        con.commit()
        print('\t   Required data has been deleted')
#update fns
def upd_manyr(car_id):
         old=car_id
         new=input('Enter the new date (yyyy-mm-dd):').upper()          query="update all_cars set manufacture_yr='{}' where car_id='{}'".format(new,old)
         cur.execute(query)
         con.commit()
         print('Update Complete')
def upd_type(car_id):
         old=car_id
         new=input('\t   Enter the new type:').upper()          query="update all_cars set type='{}' where car_id='{}'".format(new,old)
         cur.execute(query)
         con.commit()
         print('\t   Update Complete')
def upd_company(car_id):
         old=car_id
         new=input('\t   Enter the new company name:').upper()          query="\t   update all_cars set company='{}' where car_id='{}'".format(new,old)
         cur.execute(query)
         con.commit()
         print('Update Complete')
def upd_model(car_id):
         old=car_id
         new=input('Enter the new model:').upper()
         query="update all_cars set model='{}' where car_id='{}'".format(new,old)
         cur.execute(query)
         con.commit()
         print('Update Complete')
def upd_status(car_id):
         new=input('Enter the new status  : ').upper()          query="update all_cars set status='{}' where car_id='{}'".format(new,car_id)
         cur.execute(query)
         con.commit()
         print('Update Complete')
def upd_carid():
         old=input('Enter the original car id  : ')
         new=input('Enter the new car id:').upper()
         query="update all_cars set car_id='{}' where car_id='{}'".format(new,old)
         cur.execute(query)
         con.commit()
         print('Update Complete')
def upd_rentd(car_id):
         old=car_id
         new=input('Enter the new rent per day:').upper()          query="update all_cars set rent_day='{}' where car_id='{}'".format(new,old)
         cur.execute(query)
         con.commit()
         print('Update Complete')
def upd_rentw(car_id):
         old=car_id
         new=input('Enter the new rent per week:').upper()          query="update all_cars set rent_week='{}' where car_id='{}'".format(new,old)
         cur.execute(query)
         con.commit()
         print('Update Complete')
def upd_rentm(car_id):
         old=car_id
         new=input('Enter the new rent per month:').upper()          query="update all_cars set rent_month='{}' where car_id='{}'".format(new,old)
         cur.execute(query)
         con.commit()
         print('Update Complete')
#display
def displayallcars():
         query="select * from all_cars"
         cur.execute(query)
         data=cur.fetchall()
         print(tabulate(data,headers=['Manufacture year','Type','Company'\
                                            ,'Model','Car id','Plate_no','Status'\
                                            ,'Rent per day','rent per week','Rent per month'],tablefmt='fancy_grid'))
def insert_newrentedcar(car_id):
         print()
         plate_no = input("\t  Enter Car's number plate : ")          rent_date=datetime.date.today()
         print('d=days\tw=week\tm=months')
         time_rent=input('\t  How long will you be renting this car for? (2d, 4w, 6m, etc)  :  ')
         for i in time_rent:
                  if i.isdigit():
                           number=int(i)
                  if i.lower() =='d':
                          q="select rent_day from all_cars where car_id='{}'".format(car_id)
                          numberofdays=1
                  elif i.lower() =='w':
                          q="select rent_week from all_cars where car_id='{}'".format(car_id)
                          numberofdays=7
                  elif i.lower() =='m':
                          q="select rent_month from all_cars where car_id='{}'".format(car_id)
                          numberofdays=30
         cur.execute(q)
         rent=cur.fetchall()
         for r in rent:
                  rentamt=r[0]
         amt=number*rentamt
         query = "INSERT INTO members(car_id,plate_no,rent_date,amount) VALUES (%s,%s,%s,%s)"          data=(car_id, plate_no, rent_date,  amt)
         cur.execute(query,data)
         con.commit()
no_renting_days=number*numberofdays
print("\t  You are renting for ",no_renting_days,"days")
         q="select date_add(%s,interval %s day) from members where rent_date=%s"
         data=(rent_date,no_renting_days,rent_date)          cur.execute(q,data)
         for i in cur:
                  val=i[0]
         q="update members set return_date='{}' where car_id='{}'".format(val,car_id)
         cur.execute(q)
         con.commit
         cur.execute("select * from members where plate_no='{}'".format(plate_no))
         data=cur.fetchall()
         print('\t  Your record is:')
         print(tabulate(data,headers=['Car_id','Car Plate No','Rented date'\
                                            ,'Return date','Amount'],tablefmt='fancy_grid'))
### RENTED CARS####
def search_records():
    query = 'SELECT * FROM members'
    search = input("\t  What do you want to search based on? (car_id, plate_no, rent_date, return_date): ").strip()
    if search == 'car_id':
        car_id = input("\t  Enter car ID to search: ")
        query += " WHERE car_id = '{}'".format(car_id)
    elif search == 'plate_no':
        plate_no = input("\t  Enter plate number to search: ")
        query += " WHERE plate_no = '{}'".format(plate_no)
    elif search == 'rent_date':
        rent_date = input("\t  Enter rent date (YYYY-MM-DD) to search: ")
        query += " WHERE rent_date = '{}'".format(rent_date)
    elif search == 'return_date':
        return_date = input("\t  Enter return date (YYYY-MM-DD) to search: ")
        query += " WHERE return_date = '{}'".format(return_date)
    cur.execute(query)
    data=cur.fetchall()
    print(tabulate(data,headers=['Car_id','Car Plate No','Rented date'\
                                            ,'Return date','Amount'],tablefmt='fancy_grid'))
def insert():     try:
        print()
        car_id = input('\t  Enter Car ID: ')
        cur.execute("select * from all_cars where car_id='{}'".format(car_id))
        data=cur.fetchall()
        if not data:
            print("Sorry, this car does not exists")
            return
        plate_no = input("\t  Enter Car's number plate: ")         rent_date=datetime.date.today()
        return_day = int(input('\t  Enter the return day: '))
        return_month = int(input('\t  Enter the return month: '))         return_year = int(input('\t  Enter the return year: '))
        amt = int(input('\t  Enter the Amount to be paid: '))
        doreturn = str(datetime.date(return_year, return_month, return_day))
        query = "INSERT INTO members \
                        VALUES (%s,%s,%s,%s,%s)"
        data=(car_id, plate_no, rent_date, doreturn, amt)
        cur.execute(query,data)
        con.commit()
        q="update all_cars set status='NOT AVAILABLE' where car_id='{}'".format(car_id)
        cur.execute(q)
        con.commit()
    except:
        print('\t  Dup Entery')
def delete_record():
    delete = input("\t  Which field do you want to use for deletion? (car_id, plate_no, rent_date, return_date): ").strip()
    if delete == 'car_id':
        car_id = input("\t  Enter the car ID to delete: ")
        q="update all_cars set status='AVAILABLE' where car_id='{}'".format(car_id)
        cur.execute(q)
        con.commit()
        query="update customers_ set status_of_customer='OLD' where car_id='{}'".format(car_id)
        cur.execute(query)
        con.commit()
        query = "DELETE FROM members WHERE car_id = '{}'".format(car_id)
    elif delete == 'plate_no':
        plate_no = input("\t  Enter the plate number to delete: ")
        q="select car_id from members where plate_no='{}'".format(plate_no)
        cur.execute(q)
        for i in cur:
            caridf=i[0]
        q="update all_cars set status='AVAILABLE' where car_id='{}'".format(caridf)
        cur.execute(q)
        con.commit()
        query="update customers_ set status_of_customer='OLD' where car_id='{}'".format(caridf)
        cur.execute(query)
        con.commit()
        query = "DELETE FROM members WHERE plate_no = '{}'".format(plate_no)
    elif delete == 'rent_date':
        rent_date = input("\t  Enter the rent date (YYYY-MM-DD) to delete: ")
        q="select car_id from members where rent_date='{}'".format(rent_date)
        cur.execute(q)
        for i in cur:
            caridf=i[0]
        q="update all_cars set status='AVAILABLE' where car_id='{}'".format(caridf)
        cur.execute(q)
        con.commit()
        query="update customers_ set status_of_customer='OLD' where car_id='{}'".format(caridf)
        cur.execute(query)
        con.commit()
        query = "DELETE FROM members WHERE rent_date = '{}'".format(rent_date)
    elif delete == 'return_date':
        return_date = input("\t  Enter the return date (YYYY-MM-DD) to delete: ")
        q="select car_id from members where return_date='{}'".format(return_date)
        cur.execute(q)
        for i in cur:
            caridf=i[0]
        q="update all_cars set status='AVAILABLE' where car_id='{}'".format(caridf)
        cur.execute(q)
        con.commit()
        query="update customers_ set status_of_customer='OLD' where car_id='{}'".format(caridf)
        cur.execute(query)
        con.commit()
        query = "DELETE FROM members WHERE return_date = 
'{}'".format(return_date)
    else:
        print("\t  Try again.")         return
    cur.execute(query)
    con.commit()
def modifydata():
    car_id = input('\t  Enter car ID of the record to update: ')     query = "SELECT * FROM members WHERE car_id = '{}'".format(car_id)
    cur.execute(query)
    p = False
    for record in cur:         p = True
    if p:
        print('\t  Car ID exists')
        plate_no = input("\t  Enter new Car's number plate: ")
        rent_day = int(input('\t  Enter the new rented day: '))
        rent_month = int(input('\t  Enter the new rented month: '))         rent_year = int(input('\t  Enter the new rented year: '))
        return_day = int(input('\t  Enter the new return day: '))
        return_month = int(input('\t  Enter the new return month: '))
        return_year = int(input('\t  Enter the new return year: '))         amt = int(input('\t  Enter the new Amount to be paid: '))
        dorent = str(datetime.date(rent_year, rent_month, rent_day))         doreturn = str(datetime.date(return_year, return_month, return_day))
        update = "UPDATE members SET plate_no = '{}', rent_date = '{}', return_date = '{}', amount = {} WHERE car_id = '{}'".format(plate_no, dorent,\
doreturn, amt, car_id)
        cur.execute(update)
        con.commit()
        print("\t  Record updated successfully.")     else:
        print("\t  Car ID does not exist.")
def display():
         query="select * from members"
         cur.execute(query)
         data=cur.fetchall()
         print(tabulate(data,headers=['Car_id','Car Plate No','Rented date'\
                                            ,'Return date','Amount'],tablefmt='fancy_grid'))
### BOOKING #####
def update_car_vacancy(min_rent, max_rent, rent_type):
    if rent_type == "monthly":
        rent_column = "rent_month"
    elif rent_type == "weekly":
        rent_column = "rent_week"
    else:
        rent_column = "rent_day"
    query = f"SELECT  * FROM all_cars WHERE {rent_column} BETWEEN %s AND %s and status='available'"
    cur.execute(query, (min_rent, max_rent))
    rows = cur.fetchall()
    header_all_cars(rows)
#################################################################### #################################################################### #################################################################### ###########
'''OVERALL FNS'''
def line():
    print()
    print('-'*180)
    print()
while True:
         line()
         print()
         print('Choose an option:')
         print('1.CUSTOMER\n2.ALL CARS\n3.RENTED CAR DETAILS\n4.BOOKING\n5.DISPLAY ALL TABLES\n6.EXIT\n')
         n=int(input('Enter option  :  '))
         if n==1:
             while True:
                           line()
                           print('>>>CUSTOMER<<<')
                           print('\t1. Search Customer\n\t2. Insert Customer\n\t3. Delete Customer \
                                    \n\t4. Update Customer details\n\t5. Display all customers\n\t6. Exit')
                           opt=int(input('\tEnter option  :  '))
                           if opt==1:
                               while True:
                                    line()
                                    print('\t>>Search CUSTOMER by<< ')
                                    print('\t  A. Name  \n\t  B. CPR  \n\t  C. Place of work  \n\t  D. Phone no  \n\t  E. If working  \n\t  F. Customer id  \n\t  G. Address  \
\n\t  H. Gender  \n\t  I. Exit')
                                    so=input('\t  Enter option  :  ')
                                    if so.upper()=='A':
                                             searchname()
                                    elif so.upper()=='B':
                                             searchcpr()
                                    elif so.upper()=='C':
                                             searchplace_of_work()                                     elif so.upper()=='D':
                                             searchphone_no()
                                    elif so.upper()=='E':
                                             searchif_working()
                                    elif so.upper()=='F':
                                             searchcustomer_id()
                                    elif so.upper()=='G':
                                             searchaddress()
                                    elif so.upper()=='H':
                                             searchgender()
                                    else:
                                              break
                           elif opt==2:
                                    line()
                                    print('\t>>Insert customer details<< ')
                                    insertrecord()
                           elif opt==3:
                               while True:
                                    line()
                                    print('\t>>Delete CUSTOMER by<<')
                                    print('\t  A. CPR\n\t  B. Customer id\n\t  C. Exit')
                                    so=input('\t  Enter option  :')                                     if so.upper()=='A':
                                             deletecpr()
                                    elif so.upper()=='B':
                                            deletecustomer_id()
                                    else:
                                              break
                           elif opt==4:
                               while True:
                                   line()
                                   print('\t>>Update CUSTOMER by<< \n\t  A.Customer_id\n\t  B.CPR\n\t  C.Phone number\n\t  D.Exit')
                                   so=input('\t  Enter option : 
').upper()
                                   if so=='A':
                                       cus_id=input('\n\t  Enter the customer_id of the customer whose details you would like to update : ')
                                       cur.execute("select * from customers_ where customer_id='{}'".format(cus_id))
                                       data=cur.fetchall()
                                       if not data:
                                           print('This customer does not exists..')
                                           break
                                       while True:
                                           print('\n\t\tUpdate: \n\t\t    a. Name\n\t\t    b. Place_of_work\n\t\t    c. If_working\n\t\t    d. Address\n\t\t    e. Exit')
                                           opts=input('\t\t    Enter option :').lower()
                                           if opts=='a':
                                               updatename(cus_id)
                                           elif opts=='b':
updateplace_of_work(cus_id)
                                           elif opts=='c':
updateif_working(cus_id)
                                           elif opts=='d':
                                               updateaddress(cus_id)                                            else:
                                               break
                                           print("Updation complete..")
                                   elif so=='B':
                                        print("\t  Updateing cpr:")                                         updatecpr()
                                   elif so=='C':
                                        print("\t  Updating phone number:")
                                        updatephone_no()
                                   else:
                                        break
                           elif opt==5:
                                    displaycust()
                           elif opt==6:
                                    break
         elif n==2:
             while True:
                           line()
                           print()
                           print('>>>ALL CARS<<<')
                           print('\t1. Search Cars\n\t2. Insert Car\n\t3. Delete Car \
                                    \n\t4. Update Car details\n\t5. Display all Cars\n\t6. Exit')
                           print()
                           option=int(input('\tEnter option  : '))
                           if option==1:
                               while True:
                                    line()
                                    print('\t  >> Search Cars <<')
                                    print("\t   a) Manufacture yr\n\t   b) Type\n\t   c) Company\n\t   d) Model\
                                                         \n\t   e) Car_id\n\t   f) Status\n\t   g) Rent per day\n\t   h) Rent per week\n\t   i) Rent per month\n\t   j) Exit")
                                    print()
                                    opt=input('\t   Enter option  :  ')
                                    print()
                                    if opt.lower()=='a':
                                             searchcar_manf()
                                    elif opt.lower()=='b':
                                             searchcar_type()
                                    elif opt.lower()=='c':
                                             searchcar_company()
                                    elif opt.lower()=='d':
                                             searchcar_model()
                                    elif opt.lower()=='e':
                                             searchcar_carid()
                                    elif opt.lower()=='f':
                                             searchcar_status()
                                    elif opt.lower()=='g':
                                             searchcar_rentd()
                                    elif opt.lower()=='h':
                                             searchcar_rentw()
                                    elif opt.lower()=='i':
                                             searchcar_rentm()
                                    else:
                                             break
                           elif option==2:
                                    line()
                                    print('\t  >> Insert Car Details <<')                  
                                    insert_vals()
                           elif option==3:
                                    line()
                                    print('\t  >> Delete Car Details <<')
                                    del_carid()
                                    opt=input('\t  Continue? y/n: ')                                     if opt!='y' or opt!='Y':
                                        continue
                                    else:
                                        break
                           elif option==4:
                               while True:
                                    line()
                                    print('>> Update Car Details <<')
                                    print("\t  a) Manufacture yr\n\t  b) Type\n\t  c) Company\n\t  d) Model\
                                                      \n\t  e) Status\n\t  f) Rent per day\n\t  g) Rent per week\n\t  h) Rent per month\n\t  i) Exit")
                                    print()
                                    opt=input('\t  Enter option  :  ')
                                    if opt.lower()=='i':
                                        break
                                    car_id=input('\t  Enter car_id of the car you would like to update : ')
                                    if opt.lower()=='a':
                                             upd_manyr(car_id)
                                    elif opt.lower()=='b':
                                             upd_type(car_id)
                                    elif opt.lower()=='c':
                                             upd_company(car_id)                                     elif opt.lower()=='d':
                                             upd_model(car_id)
                                    elif opt.lower()=='e':
                                             upd_status(car_id)                                     elif opt.lower()=='f':
                                             upd_rentd(car_id)
                                    elif opt.lower()=='g':
                                             upd_rentw(car_id)
                                    elif opt.lower()=='h':
                                             upd_rentm(car_id)
                                    else:
                                             break
                           elif option==5:
                                    line()
                                    displayallcars()
                           elif option==6:
                                    break
                           else:
                                    print('\t  Option not available')
         elif n==3:
                  while True:
                           line()
                           print()
                           print('>>>RENTED CARS<<<')
                           print("\t  1.Search rented car\n\t  2.Insert rented car\n\t  3.Delete rented car\n\t  4.Update rented car\n\t  5.Display rented car\n\t  6.Exit")
                           print()
                           n=int(input('\t  Enter option  : '))
                           line()
                           if n == 1:
                                    search_records()                            elif n == 2:
                                    insert()
                           elif n == 3:
                                    delete_record()                            elif n == 4:
                                    modifydata()
                           elif n == 5:
                                    display()
                           elif n == 6:
                                    break
         elif n==4:
                  q="select * from all_cars where status='available'"
                  cur.execute(q)
                  data=cur.fetchall()
                  header_all_cars(data)
                  while True:
                           print()
                           print('\t  Book car by \n\t  1.Rent\n\t  2.Finalise booking\n\t  3.Exit\n')
                           n=int(input('\t  Enter option  :  '))
                           line()
                           if n==1:
                                    min_rent = float(input("\t  Enter minimum rent: "))
                                    max_rent = float(input("\t  Enter maximum rent: "))
                                    rent_type = input("\t  Select rent type (monthly/weekly/daily): ").strip().lower()
                                    if rent_type not in ["monthly", "weekly", "daily"]:
                                        print("\t  Invalid rent type. Please select either 'monthly', 'weekly', or 'daily'.")
                                    else:
                                        update_car_vacancy(min_rent, max_rent, rent_type)
                           elif n==2:
                                    chosencar=input('\t  Enter the car_id of car you would like to book  :  ')
                                    query="select * from all_cars where car_id='{}'".format(chosencar)
                                    cur.execute(query)
                                    data=cur.fetchall()
                                    if not data:
                                        print("\t  Car not found")                                     elif data[0][6]=='NOT 
AVAILABLE':
                                        print("\t  Sorry this car has already been booked")
                                    else:
                                        header_all_cars(data)
                                        confi=input('\t  Confirm decision?  :  ').upper()
                                        if confi=='YES' or confi=='Y':
                                                 print('\t  Please fill out the necassasry details\n')
insert_newrentedcar(chosencar)
                                                 print('\n\t  Please enter your details\n')
                                                 insertrecord()
                                                 q="update all_cars set status='NOT AVAILABLE' where car_id='{}'".format(chosencar)
                                                 cur.execute(q)
                                                 con.commit()
                                        elif confi=='NO' or confi=='N':
                                                 print('\t  Please take your time while choosing')
                                                 continue
                           elif n==3:
                                    break
         elif n==5:
print('\t  All records:') display() displayallcars()
print()
displaycust()
         elif n==6:
                  print('-'*180)
                  print('Thank you for choosing us!')                   print('-'*180)
                  break
