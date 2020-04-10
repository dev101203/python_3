#1
my_baby_bool = "true"
my_baby_bool
print(type(my_baby_bool))


my_baby_bool_two = True 
my_baby_bool_two

print(type(my_baby_bool_two))

#2 If statement 
def dave_check(user_name):
  if user_name == "Dave":
    return "Go away Dave!"
  if user_name == "angela_catlady_87":
    return "I know it is you Dave! Go away"
user_name = "Dave"
print(dave_check(user_name))

##Relational operators
def age_check(age):
  if age >= 13:
    return True

#rel operators 2
def greater_than(x, y):
  if x > y:
    return x
  if y > x:
    return y
  if x == y:
    return "These numbers are the same"
    
def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"
  
print(graduation_reqs(120))