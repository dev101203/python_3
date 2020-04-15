#max number
def max_number(num1,num2,num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num2 and num3 > num2:
    return num3
  else: 
    return "Its a tie"
print(max_number(1,2,3))

#in range 
def in_range(num,lower,upper):
  if num >= lower and num <= upper:
    return True
  else:
    return False 
print(in_range(10,10,10))
print(in_range(5,10,20))

#always false
def always_false(num):
  if(num >0 and num < 0):
    return True
  else: 
    return False 
print(always_false(0))
print(always_false(-1))
print(always_false(1))


