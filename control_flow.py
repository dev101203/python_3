#1age_check function for our movie 
# streaming platform. Previously, 
# all it did was check if the user’s age was over 13 and 
# if so return True. We can use an else statement to return 
# a message in the event the user is too young to watch the movie.
def age_check(age):
  if age >= 13:
    return True
  else:
    return "Sorry, you must be 13 or older to watch this movie."

## Try and except control flow 
def divides(a,b):
  try:
    result = a / b
    print (result)
  except ZeroDivisionError:
    print ("Can't divide by zero!")
