# odd_indexes
def odd_indices(lst):
  x =[]
  for index in range(1, len(lst), 2):
    x.append(lst[index])
  return x
print(odd_indices([4, 3, 7, 10, 11, -2]))

#exponents 
def exponents(bases, power):
  x = []
  for base in bases:
    for base in bases:
      x.append(bases**power)
  return x
print(exponents([2,3,4], [1,2,3]))

## larger numbers
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2
print(larger_sum([1, 9, 5], [2, 3, 7]))

### over 9000
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum
## largest number find
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum
print(max_num([50, -10, 0, 75, 20]))


### same values

def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst