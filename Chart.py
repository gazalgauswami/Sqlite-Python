#Line Chart
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('data.xlsx')
n=df.Name
s1=df.Sub1
s2=df.Sub2
s3=df.Sub3
plt.plot(n,s1)
plt.plot(n,s2)
plt.plot(n,s3)
plt.title("Student's Subject Wise Marks: ")
plt.xlabel('Name')
plt.ylabel('Marks')
plt.legend(('Sub1','Sub2','Sub3'))
plt.show()

#Bar Chart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_excel('data.xlsx')
n=df.Name
Name=n
n1=n
n=np.arange(len(n))
s1=df.Sub1
s2=df.Sub2
s3=df.Sub3
plt.xticks(n,Name)
plt.bar(n+0.00,s1,width=0.25)
plt.bar(n+0.25,s2,width=0.25)
plt.bar(n+0.50,s3,width=0.25)
plt.title("Student's Subject Wise Marks: ")
plt.xlabel('Name')
plt.ylabel('Marks')
plt.legend(('Sub1','Sub2','Sub3'))
plt.show()


#Scatter Chart
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('data.xlsx')
n=df.Name
s1=df.Sub1
s2=df.Sub2
s3=df.Sub3
plt.scatter(n,s1,marker='|')
plt.scatter(n,s2,marker='^')
plt.scatter(n,s3,marker='+')
plt.title("Student's Subject Wise Marks: ")
plt.xlabel('Name')
plt.ylabel('Marks')
plt.legend(('Sub1','Sub2','Sub3'))
plt.show()

#Histogram
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('data.xlsx')
n=df.Name
s1=df.Sub1
s2=df.Sub2
s3=df.Sub3
plt.hist(s1,bins=30,range=(1,120))
plt.hist(s2,bins=30,range=(1,120))
plt.hist(s3,bins=30,range=(1,120))
plt.title("Student's Subject Wise Marks: ")
plt.xlabel('Name')
plt.ylabel('Marks')
plt.legend(('Sub1','Sub2','Sub3'))
plt.show()
