toppings = ['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']

prices = [2,6,1,3,2,7,2]

#lenght 
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) +" different kinds of pizza!")

#zip
pizzas = list(zip(prices,toppings))
print(pizzas)

#sort
pizzas.sort()
print(pizzas)

#the 1st element
cheapest_pizza = pizzas[0]
print(cheapest_pizza)

# the last
priciest_pizza = pizzas[-1]
print(priciest_pizza)

#the 3 lowest cost pizzas
three_cheapest = pizzas[:3]
print(three_cheapest)

#Count the number of occurrences of 2
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
