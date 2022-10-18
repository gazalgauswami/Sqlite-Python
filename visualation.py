
#plot() line chart
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]

#plt.plot(x,y)
#plt.plot(x,y,marker='>',linestyle='--')
#plt.plot(x,y,'+g-.')
plt.plot(x,y,linewidth='2',label='Lable')
plt.xlabel('Xlable')
plt.ylabel('Ylable')
plt.title('Line Chart')
plt.show()


#legend()
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_excel('data.xlsx')
r=df.Rollno
n=df.Name
s1=df.Sub1
s2=df.Sub2
s3=df.Sub3
plt.plot(n,s1)
plt.plot(n,s2)
plt.plot(n,s3)
plt.title("Student's Subject wise marks")
plt.xlabel('Name')
plt.ylabel('Sub')
plt.legend(['Sub1','SUb2','Sub3'])
plt.legend(['Sub1','SUb2','Sub3'],loc='lower left')
plt.show()

#range()
import matplotlib.pyplot as plt
x=range(-10,0)
y=range(0,20,2)
plt.plot(x,y)
plt.show()


#grid()
import matplotlib.pyplot as plt
x=range(1,10)
y=[20,43,12,65,87,45,76,98,45]
plt.plot(x,y)
plt.grid()
plt.show()


#len()
import matplotlib.pyplot as plt
x=range(1,10)
y=[23,43,12,65,87,45,76,98,45]
print(len(x))
print(len(y))

#subplot()
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_excel('data.xlsx')
r=df.Rollno
n=df.Name
s1=df.Sub1
s2=df.Sub2
s3=df.Sub3
plt.subplot(1,3,1)
plt.plot(r,s1,linewidth=2,marker='.')
plt.xlabel('Name')
plt.ylabel('Subject 1 marks')
plt.title('Result-1')
plt.subplot(1,3,2)
plt.plot(r,s2,linewidth=2,marker='.')
plt.xlabel('Name')
plt.ylabel('Subject 2 marks')
plt.title('Result-2')
plt.subplot(1,3,3)
plt.plot(r,s3,linewidth=2,marker='.')
plt.xlabel('Name')
plt.ylabel('Subject 3 marks')
plt.title('Result-3')

plt.show()

#scatter chart
import matplotlib.pyplot as plt
x=[12,45,52,25,66]
y=[43,56,77,98,34]
plt.scatter(x,y)
plt.show()


#multiple scatter plot on one axis
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_excel('data.xlsx')
r=df.Rollno
s1=df.Sub1
s2=df.Sub2
s3=df.Sub3

plt.scatter(r,s1,marker='*',c='red',edgecolor='black',s=50,linewidth=2)
plt.scatter(r,s2,marker='^',c='blue',edgecolor='black',s=50,linewidth=2)
plt.xlabel('Roll')
plt.ylabel('Marks')
plt.title('Scatter Chart')
plt.show()

#Histogram list()
import pandas as pd
import matplotlib.pyplot as plt

marks=[5,8,99,77,66,55,44,32,34,78,90,65,32,12,90,56,23]

plt.hist(marks,bins=20,edgecolor='blue',color='red',range=(1,100))

plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('Histogram of Marks')
plt.show()


#Histogram with specific range
import pandas as pd
import matplotlib.pyplot as plt
marks=[5,8,99,77,66,55,44,32,34,78,90,65,32,12,90,56,23]
seq=[0,10,20,30,40,50,60,70,80,90,100]
y=[1,2,3,4,5]
plt.hist(marks,edgecolor='Black',bins=seq,color='Yellow')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('Histogram of Marks')
plt.yticks(y)
plt.xticks(seq)
plt.show()


#Bar chart
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('data.xlsx')
plt.style.use('bmh')
n=df.Name
s1=df.Name
plt.bar(n,s1,label='Sub1')
plt.title('SubjectWise Student result')
plt.xlabel('Name')
plt.ylabel('Marks')
plt.legend()
plt.show()

#for see style method
print(plt.style.available)

#style  method
import pandas as ps
import matplotlib.pyplot as plt
df=ps.read_excel('data.xlsx')
plt.style.use('ggplot')
r=df.Rollno
n=df.Name
s1=df.Sub1
s2=df.Sub2
s3=df.Sub3
plt.plot(n,s1,label='Sub1')
plt.plot(n,s2,label='Sub2')
plt.title('SubjectWise Student result')
plt.xlabel('Name')
plt.ylabel('Marks')
plt.legend()
plt.show()


#for saving chart image
plt.savefig('test.png')

#plot line chart
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel('data.xlsx')
df.plot(x='Name',y=['Sub1','Sub2'],kind='line',color='r',linewidth=2,marker='o',linestyle='--')
plt.show()

#plot bar chart
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel('data.xlsx')
df.plot(x='Name',y=['Sub1','Sub2'],kind='bar',color='pink',linewidth=2,linestyle='--',edgecolor='black')
plt.show()

#plot scatter chart
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel('data.xlsx')
df.plot(x='Rollno',y='Sub1',kind='scatter',marker='o')
plt.show()

