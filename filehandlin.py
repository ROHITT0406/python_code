'''in read mode
f=open("myfile2.txt",'r')
text=f.read()
print(text)
f.close
in write mode
f=open("myfile2.txt",'w')
f.write("i will work hard till i get the job ")
f.close
opening a file with open method

f=open("myfile2.txt",'a')
f.write("so that i can help my family")
f.close'''
#using with method
with open("myfile.txt","a") as f:
    f.write("i have to show everyone that  i am not behind")