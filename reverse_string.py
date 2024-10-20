s=input("Enter the string :")
reverse=""
for i in range(-1,-len(s)-1,-1):
    reverse=reverse+s[i]
print(reverse)