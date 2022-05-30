#Programe to create a new file 
f = open('my_file.txt','w')
f.write("Hello Sudheer!\n I Like your python coding. \n I like Kick buttwoski")
f.close()
#Program to read the contents in the new file   
f = open('my_file.txt' ,'r')
for line in f.readlines():
  print(line)
f.close()
#Program to append the contents to an existing file
f = open('my_file.txt','a')
f.write("\n Rollno :VU21EECE0100011")
f.close()
#Program to copy the contents from one file to another file
f1=open('my_file.txt','r')
f2=open('my_duplicate_file.txt','w')
for line in f1.readlines():
  f2.write(line)
f1.close()
f2.close()
#Program to delet a file
import os
os.remove('my_duplicate_file.txt')
#Programe to count the number of words in text file
file = open("my_file.txt", "r")
data = file.read()
words = data.split()
print('Number of words in text file :', len(words))
#Program to counnt the number of lines in file 
def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("my_file.txt"))