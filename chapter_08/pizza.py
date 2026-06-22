def make_pizza(size, *toppings):
    if len(toppings) == 1:
        print(f"Making {size}-inch pizza wiht following topping:")
    else:
        print(f"Making {size}-inch pizza wiht following toppings:")

    for topping in toppings:
        print(f" --- {topping}")
    # print(type(toppings))


# make_pizza(12, "pepperoni")
# make_pizza(16, "extra cheese", "green onions", "chili")
