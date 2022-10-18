

#open() function
import csv
f1=open(r'C:\sqlite\student.csv','r')
data=csv.reader(f1)
print(data)
print('*'*50)
for a in data:
    print(a[0],'%20s'%a[1],'%20s'%a[2],'%20s'%a[3])
print('*'*50)

#close() function
f1.close()

#with open() function with next() method
with open(r'C:\sqlite\student.csv','r') as f1:
    data=csv.reader(f1)
    col=next(data)
    print('*'*50)
    print(col)
    print('*'*50)

    for a in data:
        if int(a[3])>=90:
            print(a)

#reader() with line_num
import csv
with open(r'C:\sqlite\student.csv','r') as f1:
    r1=csv.reader(f1)
    print('Line Number: ',r1.line_num)
    col=next(r1)
    print('Line Number: ',r1.line_num)
    print('*'*50)
    print(col)
    print('*'*50)
    print('Line Number: ',r1.line_num)
    for row in r1:
        if row[2]=='Female':
            print(row)
    print('Line Number: ',r1.line_num)        

#writer,writerow,writerows
import csv
cols=['Rollno','Name','Gender','Per']
rows=[[1,'Gazal','Female',98],
[2,'Pawan','Male',99],
[3,'Meera','Female',88],
[4,'Om','Male',88],
[5,'Prakash','Mal',59],
[6,'Isha','Female',65],
[7,'Komal','Female',80],
[8,'Lalit','Male',60],
[9,'Manish','Male',70],
[10,'Sunita','Female',99]]
with open (r'C:\sqlite\student.csv','w') as f1:
    w1=csv.writer(f1)
    w1.writerow(cols)
    w1.writerows(rows)


#lineterminator
import csv
cols=['Rollno','Name','Gender','Per']
rows=[[1,'Gazal','Female',98],
[2,'Pawan','Male',99],
[3,'Meera','Female',88],
[4,'Om','Male',88],
[5,'Prakash','Mal',59],
[6,'Isha','Female',65],
[7,'Komal','Female',80],
[8,'Lalit','Male',60],
[9,'Manish','Male',70],
[10,'Sunita','Female',99]]
with open(r'C:\sqlite\student.csv','w') as f1:
    w1=csv.writer(f1,lineterminator='\n')
    w1.writerow(cols)

    
#append mode()
import csv
l=eval(input('Enter list: '))
with open(r'C:\sqlite\student.csv','a') as f1:
    w1=csv.writer(f1,lineterminator='\n')
    w1.writerow(l)
    w1.writerow([12,'Hiral','Female',82])
    print('Data write succesfully')

#Dict reader
import csv
with open(r'c:\sqlite\student.csv','r') as f1:
    d1=csv.DictReader(f1)
    for i in d1:
        print(dict(i))

#DictWriter
import csv
cols=['Rollno','Name','Gender','Per']
rows=[{'Rollno':1,'Name':'Gazal','Gender':'Feamale','Per':90},
      {'Rollno':2,'Name':'Pawan','Gender':'Male','Per':55},
      {'Rollno':3,'Name':'Meera','Gender':'Female','Per':80},
      {'Rollno':4,'Name':'Lara','Gender':'Female','Per':70},
      {'Rollno':5,'Name':'Sumita','Gender':'Female','Per':69}]
with open(r'c:\sqlite\student.csv','w') as f1:
    w1=csv.DictWriter(f1,fieldnames=cols,lineterminator='\n')
    w1.writeheader()
    w1.writerows(rows)

#DictWriter append()
import csv
cols=['Rollno','Name','Gender','Per']
with open(r'c:\sqlite\student.csv','a') as f1:
    w1=csv.DictWriter(f1,fieldnames=cols,lineterminator='\n')
    w1.writeheader()
    w1.writerow({'Rollno':1,'Name':'Gazal','Gender':'Feamale','Per':90})
    w1.writerow({'Rollno':2,'Name':'Pawan','Gender':'Male','Per':55})
    w1.writerow({'Rollno':3,'Name':'Meera','Gender':'Female','Per':80})
    w1.writerow({'Rollno':4,'Name':'Lara','Gender':'Female','Per':70})
    w1.writerow({'Rollno':5,'Name':'Sumita','Gender':'Female','Per':69})

from numpy import *
#one diamentional array
a=array([1,2,3,4,5])
print(a)
print('Third Values is: ',a[2])

#two diamentional array
b=array([[1,2,3],[4,5,6]])
print(b)
print('First row second value: ',b[1,2])

#three diamentional array
c=array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(c)
print('a[0,1,1]: ',c[0,1,1])

#check the diamentional
print("a is :",a.ndim)
print("b is :",b.ndim)
print("c is :",c.ndim)

#slicing the array
a=array([1,2,3,4,5,6,7,8,9])
print("a        : ",a)
print("a[1:3]   : ",a[1:3])
print("a[1:]    : ",a[1:])
print("a[:3]    : ",a[:3])
print("a[0:5:2] : ",a[0:5:2])
print("a[5:0:-1]: ",a[5:0:-1])


#create a table using numpy
from numpy import *
cols=['Rollno','Name','Marks']
a=array([[1,'Gazal',90],[2,'Pawan',80],[3,'Om',70]])
print(cols)
print(a)
print('*'*30)
print(cols[0],'\t',cols[1],'\t',cols[2])
print('*'*30)
for i in a:
    print(i[0],'\t',i[1],'\t',i[2])


#Dataframe using pandas
import pandas as pd
import numpy as np

a=np.array([[1,'Gazal',90],[2,'Pawan',70],[3,'Meera',80]])
row=[1,2,3]
col=['rno','name','marks']
#df=pd.DataFrame(data=a,columns=col)
df=pd.DataFrame(data=a,index=row,columns=col)
print(df)



#DataFrame using Disctionary
import pandas as pd
import numpy as np

a={'Rollno':[1,2,3],'Name':['Gazal','Pawan','Meera'],'Marks':[90,80,70]}
df=pd.DataFrame(a)
print(df)


#Dataframe using read_csv(using pandas)
import pandas as pd
df=pd.read_csv(r"C:\sqlite\student.csv")
print(df)


#read_csv with all options
import pandas as pd
#df=pd.read_csv(r"C:\sqlite\student.csv",index_col='Name')
#df=pd.read_csv(r"C:\sqlite\student.csv",header=1)
#df=pd.read_csv(r"C:\sqlite\student.csv",names=['A','B','C','D'])
#df=pd.read_csv(r"C:\sqlite\student.csv",header=0,names=['A','B','C','D'])
#df=pd.read_csv(r"C:\sqlite\student.csv",skiprows=3)
df=pd.read_csv(r"C:\sqlite\student.csv",nrows=3)
print(df)


#writing to csv file using pandas(to_csv)
import pandas as pd
a={'Rollno':[1,2,3],'Name':['Gazal','Pawan','Meera'],'Marks':[90,80,70]}
df=pd.DataFrame(a)
#df.to_csv(r"C:\sqlite\student.csv")
#df.to_csv(r"C:\sqlite\student.csv",index=False)
df.to_csv(r"C:\sqlite\student.csv",index=False,columns=['Marks'])
print(df)


#creating DataFrame using Excel File(read_excel)
#pip install openpyxl

import pandas as pd
#df=pd.read_excel(r"C:\sqlite\temp.xlsx")
#df=pd.read_excel(r"C:\sqlite\temp.xlsx"."sheet1")
#df=pd.read_excel(r"C:\sqlite\temp.xlsx",index_col='Rollno')
print(df)


#writing into excel file(to_excel)
import pandas as pd

df=pd.read_excel(r"C:\sqlite\temp.xlsx")
#df.to_excel(r"C:\sqlite\temp1.xlsx",sheet_name='sheet3')
#df.to_excel(r"C:\sqlite\temp1.xlsx",sheet_name='sheet3',index=False)
df.to_excel(r"C:\sqlite\temp1.xlsx",sheet_name='sheet3',index=False,columns=['Marks'],startrow=5,startcol=3)
print(df)
print('Successfully write data')


#Operation on DataFrame
import pandas as pd
df=pd.read_excel(r"C:\sqlite\temp.xlsx")
print(df)
print(df.shape)
r,c=df.shape
print('Number of row: ',r)
print('Number of column: ',c)
print(df.columns)
print(df['Name'])
print(df[(df.Marks>70) & (df.Rollno>5)])
print('Minimum: ',df['Marks'].min())
print('Maximum: ',df['Marks'].max())
print('sum: ',df['Marks'].sum())
print(df[df.gender=='Female'])
print(df[df.Marks==df['Marks'].max()])
print(df['Name'])
print(df[['Rollno','Name']])
print(df['Rollno'][df.Marks>70])
print(df[['Rollno','Marks']][df.Marks>70])

#Function on DataFrame
import pandas as pd
df=pd.read_excel(r"C:\sqlite\temp.xlsx")
print(df.head())
print(df.head(3))
print(df.tail())
print(df.tail(3))
#slice
print(df[5:8])
print(df[:4])
print(df[5:])
print(df.Name.describe())
p=[.10,.20,.30,.40,.50,.60]
print(df.Marks.describe(percentiles=p))
print(df.values)
print(df.to_numpy())

import pandas as pd
df=pd.read_excel(r"C:\sqlite\temp.xlsx")
print(df)
print()
print(df.loc[5])

df=pd.read_excel(r"C:\sqlite\temp.xlsx",index_col='Rollno')
print(df)
print()
print(df.loc[10])

df=pd.read_excel(r"C:\sqlite\temp.xlsx",index_col='Name')
print(df)
print()
print(df.loc['Gazal'])

df=pd.read_excel(r"C:\sqlite\temp.xlsx",index_col='Rollno')
print(df)
print()
print(df.loc[[10,11]])

df=pd.read_excel(r"C:\sqlite\temp.xlsx",index_col='Rollno')
print(df)
print()
print(df.loc[10:15])

#iloc integer location

df=pd.read_excel(r"C:\sqlite\temp.xlsx")
print(df)
print()
print(df.iloc[5])
print(df.iloc[[2,5,9]])
print(df.iloc[3:8])

df=pd.read_excel(r"C:\sqlite\temp.xlsx",index_col='Marks')
print(df)
print()
print(df.iloc[5])


#central tendacy measures mean(),mode(),median()


import pandas as pd
cols=['Rno','Sub1','Sub2']
a=[[1,77,89],[2,85,88],[3,99,90],[4,99,88],[5,77,66]]
df=pd.DataFrame(data=a,columns=cols)
print(df)
m1=df[['Sub1','Sub2']].mean()
m2=df[['Sub1','Sub2']].median()
m3=df[['Sub1','Sub2']].mode()
v1=df[['Sub1','Sub2']].var()
s1=df[['Sub1','Sub2']].std()

m1=df[['Sub1','Sub2']].mean(axis=1)
m2=df[['Sub1','Sub2']].median(axis=1)
m3=df[['Sub1','Sub2']].mode(axis=1)
v1=df[['Sub1','Sub2']].var(axis=1)
s1=df[['Sub1','Sub2']].std(axis=1)

print('Mean: ',m1)
print('Median: ',m2)
print('Mode: ',m3)
print('variances: ',v1)
print('standrad deviation:',s1)
