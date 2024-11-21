'''with open("myfile2.txt","r") as f:
    i=0
    while True:
        i=i+1
        line=f.readline()
        if not line :
            break
        m1=int(line.split(",")[0])
        m2=int(line.split(",")[1])
        m3=int(line.split(',')[2])
        print(f"student {i} maths marks {m1} ")
        print(f"student {i} science marks {m2} ")
        print(f"student {i} social science marks {m3} ")'''
f=open("myfile3.txt","w")
line=["hello","everyone","how are you","i hope you are doing well"]
for lines in line:
    f.write(lines+"\n")
f.close