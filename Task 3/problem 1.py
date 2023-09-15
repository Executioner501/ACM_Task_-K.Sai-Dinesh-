s=input("")
l=s.split()
ol=[int(item)for item in l]
if len(ol)<=100:
  o=[num for num in ol if -100<= num<=100 and num%2!=0 ] 
  os=sum(o)
  print("the sum of odd numbers is",os)
else:
  print("enter in limit")

