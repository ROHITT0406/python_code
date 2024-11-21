a=input("enter a string").split()
t=[]
for i in a:
    t.append(i[::-1])
print(" ".join(t))









#t=" ".join(a[::-1])
#print(t)
#for i in a[:len(a)-1]:
#    t.append(i[0])
#t.append(a[-1])
#print(" ".join(t))
#p=[]
#for i in a:
#    if len(i) % 2 == 0:
#        p.append(i)
#print(p)
        