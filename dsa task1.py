def comp(n):
    l=list(n.strip(" "))
    l.append("z")
    c=1
    a=[]
    i=0
    while i<(len(l)-1):
        if l[i]==l[i+1]:
            c+=1
        else:
            a.append(l[i])
            a.append(str(c))
            c=1
        i+=1
    for i in a:
        if i=="1":
            a.remove("1")
    return a
def ltos(q):
    s=""
    for j in q:
        s+=j
    print(s)
l=str(input("Enter string to be compressed : "))
ltos(comp(l))
