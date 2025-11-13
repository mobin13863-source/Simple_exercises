a=input("givee me a str ").split()
result=[]
for i in a:
    if len(i) >3 and i[0].lower()in "aeiou":
        result.append(i)
print(result)

