import re
Password = input("Enter password")
i = 0
if re.search('\W+',Password) != None:
  #for special characters  
    i+=1
if re.search('[A-Z]+',Password) != None:
    #for uppercase
    i+=1
if re.search('[0-9]+',Password) != None:
    #for digits
    i+=1
if i == 0:
    print('poor')
if i == 1 or i == 2:
    print("medium")
if i == 3:
    print("strong")