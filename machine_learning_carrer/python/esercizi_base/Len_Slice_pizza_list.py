# Your code below:
toppings=["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"];
prices=[2,6,1,3,2,7,2];
num_two_dollar_slices=prices.count(2)
num_pizzas=len(toppings)
print("We sell "+str(num_pizzas)+" different kinds of pizza!, where")
pizza_and_prices=list(zip(toppings,prices))
print(pizza_and_prices)
pizza_and_prices.sort(key=lambda x: x[1])
print(pizza_and_prices)
cheapest_pizza=pizza_and_prices[0]
priciest_pizza=pizza_and_prices[-1]
pizza_and_prices.pop(-1)
pizza_and_prices.insert(3,[2.5, "peppers"])
print(pizza_and_prices[:3])