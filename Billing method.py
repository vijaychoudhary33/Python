ar=input()
if ar=="addition":
  sum=0
  number=input()
  number=number.split()
  for numbers in number:
    sum+=int(number)
  print(sum) 