l=[12,34,5,2,1,3,6,641,33,13,23,35,34]
i=len(l)
while i>1:
    for j in range(i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
    i=i-1
print(l)

