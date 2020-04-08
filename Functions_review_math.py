def tenth_power(num):
  return num ** 10
print(tenth_power(1))
print(tenth_power(0))
print(tenth_power(2))

# Square root
def square_root(num):
  return num ** 0.5
print(square_root(16))
print(square_root(100))

# WIN percentage
def average(num1, num2):
  return (num1+num2)/2
print(average(1, 100))
print(average(1, -1))

#Remainder 
def remainder(num1, num2):
  return (2*num1)%(num2/2)
print(remainder(15, 14))
print(remainder(9, 6))

# First three multiples

def first_three_multiples(num):
  print(num* 1)
  print(num*2)
  print(num*3)
  return num*3 
first_three_multiples(10)
first_three_multiples(0)

#tip 
def tip(total, percentage):
  tip_amount = (total * percentage)/100
  return tip_amount
print(tip(10, 25))
print(tip(0, 100))

# James Bond 
def introduction(first_name,last_name):
    return last_name + ", " +  first_name + " " + last_name 
print(introduction("James", "Bond"))
print(introduction("Maya", "Angelou"))

#dog years 7
def dog_years(name, age):
  return name+", you are "+str(age*7)+" years old in dog years"
print(dog_years("Lola", 16))
print(dog_years("Baby", 0))

#All opertaions
def lots_of_math(a, b, c, d):
  first = a+b
  second = c-d
  third = first*second
  fourth = third%a
  print(first)
  print(second)
  print(third)
  return fourth
print(lots_of_math(1, 2, 3, 4))
print(lots_of_math(1, 1, 1, 1))
