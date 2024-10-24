l=[1,3,4,6,10,12,14,17,18,20,22,28,30,32,34,35,37,45,54,69,72]
print(len(l))
target=72
left=0
right=len(l)-1
while left<=right:
    mid=(left+right)//2
    if target==l[mid]:
        print("index =",mid)
        break
    elif target>=l[mid]:
        left=mid+1
    else:
        right=mid-1
else:
    print("Number not found")

