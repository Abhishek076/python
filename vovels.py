s=list(input("Enter the string:"))
v=['a','e','i','o','u']
c=0
for i in s:
    if i in v:
        c=c+1
print(c)