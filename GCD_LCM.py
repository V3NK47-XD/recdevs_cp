n1=36
n2=12
def gcd(a,b):
    gcd=0
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd

def lcm(a,b):
    lcm=a*b
    for i in range(max(a,b),(a*b)+1):
        if i%a==0 and i%b==0:
            lcm = i
            return lcm
    return lcm

gcd=gcd(n1,n2)
lcm=lcm(n1,n2)
print("GCD =",gcd)
print("LCM =",lcm)