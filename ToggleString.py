x = input()
s=""
for l in x:
        if (l.isupper()):
            s=s+(l.lower())
         
        else: 
            s=s+(l.upper())
            
print(s)
