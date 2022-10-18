from Pack1.insert import *
from Pack2.Pack3.delete import *
from Pack3.update import *
from Pack3.display import *
from Pack4.serch import *

print('1.insert 2.delete 3.update 4.display 5.serch ')
ch=int(input('Enter Your Choice: '))

if ch==1:
    insert_data()
elif ch==2:
    delete_data()
elif ch==3:
    update_data()
elif ch==4:
    display_data()
elif ch==5:
    serch_data()
else:
    print('You Have Wrong Choise')
