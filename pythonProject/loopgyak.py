"""for i in range(5):
    b=""
    for d in range(3):
        b+="*"
    print(b)
for i in range(11):
    print(i)
i=1
while i<11:
    print(i)
    i=i+1
a=5
for i in range(1, 6):
    for j in range(1, i+1):
        print(j , end=" ")
    print("")
a=int(input("Kérek egy egész számot: "))
b=0
for i in range(1, a+1):
    b+=i
print(b)

a=int(input("Kérek egy egész számot: "))

for i in range(1):
    for h in range(1,11,1):
        print(a*h)


a = [12, 75, 150, 180, 145, 525, 50]
for i in a:
    if i%5==0:
        if i>500:
            break
        elif i>150:
            continue
        print(i)"""
a=input("Adj meg egy számot: ")
b = 0
i=0
while i<len(a):
    i=i+1
    b+=1
print(b)



