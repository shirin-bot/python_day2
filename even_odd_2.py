l=[8,33,20,5,7,12]
even=[]
odd=[]

for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
        
print(f"even is {even} \nand odd is {odd}")