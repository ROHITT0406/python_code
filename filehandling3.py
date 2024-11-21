with open("myfile3.txt","w") as f:
    f.write("hello everyone")
    f.seek(5)
    print(f.tell())
   
with open("myfile3.txt","r") as c:
    c.seek(5)
    text=c.read(5)
    print(text)   
with open("myfile3.txt","w") as f:
    f.write("hello everyone")
    f.truncate(5)