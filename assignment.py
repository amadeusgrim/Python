l1 = input("Please input values of the same length: ")
l2 = input("Please input values of the same length: ")


def hamming(l1,l2):
 number  = 0
 if len(l1) != len(l2):
  print("Strings are not equal length")
 else:
  for x,(a,b) in enumerate(zip(l1,l2)):
    if a != b:
      print(f'character not matching {a,b} in {x}')
      number += 1
 return number


print(hamming(l1,l2))

def string(s):
  return  "".join(x*2 for x in s)
print(string("public"))


# hamming distance second example 

def hamming(a,b):
  count = 0 
  for x in range(len(a)):
    if a[x] != b[x]:
      count += 1
  return count
 
a = "aabbb" 
b = "ababa"
print(hamming(a,b))


#  in this challenge establiish if a given num is a curzon number. if 1 plus 2^ num is exacyly divisible by 1+2 * num then num is a curzon number 
#given a non -ve integar num implemeny a function that returns true if num is a curzon num else flase 