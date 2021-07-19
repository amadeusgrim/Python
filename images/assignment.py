positive = 0
Negative = 0
while 1:
  x = int(input("Please input Number (0 ends Loop): "))
  if x == 0:
     break
  elif x > 0:
     positive += 1
  else: 
       Negative += 1 
   
print("Number of positive numbers :",  positive)
print("Number of negative numbers :" , Negative)  


