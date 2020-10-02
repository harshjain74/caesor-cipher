msg = input("Enter your message : ")
txt =''
key = int(input("Enter key : "))
for index,i in enumerate(msg):
    if isinstance(i,str):
        n = key + ord(i)
        if i.islower() and n > 122:
            n = n - 26 
        elif i.isupper() and n>90: 
            n = n - 26
        txt = txt + chr(n)

print(txt)
        

