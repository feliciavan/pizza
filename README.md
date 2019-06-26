# Online shop for pizza

This is a shopping website for pizza. It provides the menu of all kinds of food. Customers can choose whatever they want into their shopping cart. The owner of this website can check the order list of all customers and process the orders.

This website is based on Django and a database.

In templates/orders folder:

base.html is the layout

boss.html shows all the orders to the boss/site administrator

cart.html shows the order of customer

dinner.html for dinner platters

login and signup html for user's login and register

other htmls are for each type in menu

In models.py:

PizzaPrice is the price of Pizza

DinnerPlattersPrice is the price of DinnerPlatters

PizzaTopping just shows the toppings

Salads and Pasta contain the product and the price

SubsPrice is the price of Subs including the pure steak

SubsSteakPrice is the price of SubsSteak

Order is for customer and boss to see the products in the cart
