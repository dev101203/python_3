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

#And operators
def graduation_reqs(credits,gpa):
 credits >= 120 and gpa >= 2.0
    return "You meet the requirements to graduate!"

print(credits)
  
  # Or operator 
  def graduation_mailer(gpa, credits):
  if (gpa >= 2.0) or (credits >= 120):
    return True
###
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if not (gpa >= 2.0) and not (credits >= 120):
    return "You do not meet either requirement to graduate!"

print(graduation_reqs(2.0,120))
