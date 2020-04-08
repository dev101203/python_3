# Write your dog_years function here:
def dog_years(name, age):
  return name + "," +  "you are" + age + "years old in dog years"

print(dog_years("Lola", str(16)))

# should print "Lola, you are 112 years old in dog years"

print(dog_years("Baby", str(0)))

# should print "Baby, you are 0 years old in dog years"