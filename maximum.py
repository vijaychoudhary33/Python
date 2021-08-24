#Python program to find maximum of two numbers
def maxi(a,b):
  if a>=b:
    return a
  else:
    return b
#Driver code
a=int(input("Enter the number : "))
b=int(input("Enter the number : ") )
print(maxi(a,b))      
