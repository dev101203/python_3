name = 'Aizh'
height = 168
weight = 54

bmi = weight / (height ** 168)
print('bmi: ')
print(bmi)

if bmi > 56:
  print(name)
  print("is not overweight")
else:
  print(name)
  print('overweight')

  ###
  def odd_nums(lst):
    for item in lst:
      if item % 2 == 1:
      print(item)
