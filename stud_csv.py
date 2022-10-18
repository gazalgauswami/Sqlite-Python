import csv
import pandas as pd

#read mode
with open (r"D:\Code\Database_Python\stud.csv","r") as f1:
    r1=csv.reader(f1)
    print('-'*60)
    for row in r1:
        print('%10s'%row[0],'%10s'%row[1],'%10s'%row[2],'%10s'%row[3])
    print('-'*60)    

#append mode
rows=[[11,'Paresh','Male',85],[12,'Vadana','Feamle',90]]    
with open (r"D:\Code\Database_Python\stud.csv","a") as f1:
    w1=csv.writer(f1,lineterminator='\n')
    w1.writerows(rows)
    

#DictReader
cols=['Rollno','Name','gender','Marks']
rows=[{'Rollno':13,'Name':"Hiral",'gender':"Female",'Marks':99},{'Rollno':14,'Name':"Omkar",'gender':"Male",'Marks':55},{'Rollno':15,'Name':"Yash",'gender':"Male",'Marks':60},{'Rollno':16,'Name':"Swati",'gender':"Female",'Marks':84},{'Rollno':17,'Name':"Nayana",'gender':"Female",'Marks':69}]
with open (r"D:\Code\Database_Python\stud.csv","a") as f1:
    w1=csv.DictWriter(f1,fieldnames=cols,lineterminator='\n')
    w1.writerows(rows)

#central tredancey
a=[[1,'Gazal',90,99,89],[2,'Pawan',80,56,65],[3,'Meera',74,76,65],[4,'Paresh',69,74,72],[5,'Sumita',68,74,96],[6,'Isha',87,62,62],[7,'Om',69,88,56]]
df=pd.DataFrame(data=a,columns=['Rollno','Name','Sub1','Sub2','Sub3'])
#print(df)

cols=['Sub1','Sub2','Sub3']
#mean row-wise
m=df[cols].mean(axis=0)
print(m)

#mean column-wise
m=df[cols].mean(axis=1)
print(m)

#median row-wise
m=df[cols].median(axis=0)
print(m)

#median column-wise
m=df[cols].median(axis=1)
print(m)

#mode row-wise
m=df[cols].mode(axis=0)
print(m)

#mode column-wise
m=df[cols].mode(axis=1)
print(m)

#variance row-wise
m=df[cols].var(axis=0)
print(m)

#variance column-wise
m=df[cols].var(axis=1)
print(m)

#standrad deviation
m=df[cols].std(axis=0)
print(m)

#standrad deviation
m=df[cols].std(axis=1)
print(m)

