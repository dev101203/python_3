def ground_shipping(weight):
  if weight <= 2:
    price = 1.50
  elif weight <=6:
    price =3.00
  elif weight <= 10:
    price = 4.0 
  else:
    price = 4.75
  return 20 + (price * weight)
  
print(ground_shipping(8.4))


premium_ground_shipping = 125.00
  
 
def drone_shipping(weight):
 if weight <=2:
   price = 4.50
 elif weight <=6:
   price = 9.00
 elif weight <=10:
   price = 12.00
 else:
   price = 14.25
 return weight * price
print(drone_shipping(1.5))

def ground_premium_drone_shipping(weight):
 
  ground = ground_shipping(weight)
  premium = premium_ground_shipping
  drone = drone_shipping(weight)
 
  if ground < premium and ground < drone:
    method = "standard"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium"
    cost = premium
  else:
    method = "drone"
    cost = drone
  print(
"The cheapest option available is $%.2f with %s shipping"
  % (cost, method)
)
 
ground_premium_drone_shipping(4.8)
ground_premium_drone_shipping(41.5)


  

