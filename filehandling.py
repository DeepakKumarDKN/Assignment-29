# 1. Write a Python script to print the following status of a file:
# a. Whether a file is read only
# b. Whether a file is closed or not
# c. Which file opening mode is used
# d. Name of the file

"""
with open('questionOne.txt','r') as f:
  print('is the file read Only',f.readable())
  print('is the file closed:', f.close())
  print('Mode used is:',f.mode)
  print('Name of the file:',f.name)
  f.close()
  print('is the file closed:', f.close())
  
"""


# 2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text.

"""
with open('myfile.txt','w') as f:
  f.write('Deepak Kumar Nayak')
  f.close()
  
"""

# 3. Write a Python script to read the above created file ‘myfile.txt’ and display content on
# the console.

"""
def reading(filename,mode):
  with open(filename,mode) as f:
    data = f.read()
    print(data)
    f.close()
reading('myfile.txt','r')

"""


# 4. Write a Python script to store a list of city names in a file ‘cities.txt’

f = open('cities.txt','w')
list=['Kolkata\n','Mumbai\n','Kanpur\n','Lucknow\n','Bhopal\n','Delhi\n']
f.writelines(list)
f.close()

# for city in list:
#   f.write(city+"\n")

#5. Write a Python script to append list of city names in a file ‘cities.txt’

"""
with open('cities.txt','a')as f:
  f.writelines(['Chennai\n','Hyderabaad\n','Gurugram\n'])
  f.close()
"""

# 6. Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or not
"""
def searchCity(filename,citySearch):
  cityName = []
  with open(filename,"r") as f:
    for lines in f.readlines():
      line=lines.replace("\n","")  
      cityName.append(line)
    if citySearch in cityName:
      return 'Yes it is Present'
  return None

   
a=searchCity('cities.txt','Odisha')
print(a)

"""
# 9. Write a Python script to store book data in a file. Book data is in the form of a
# dictionary in which book name is the key and price is its value. Use pickle to store
# data into a file (say bookfile)

import pickle
books = {'bookOne':230, 'bookTwo':300, 'bookThree':300, 'bookFour':320}
f = open('bookfile.txt','ab')
pickle.dump(books,f)
f.close()

# 10. Write a Python script to extract book data from a bookfile using pickle. Also print
# extracted book data.
import pickle
f= open('bookfile.txt','rb')
s = pickle.load(f)
for key in s:
  print(key, s[key])
