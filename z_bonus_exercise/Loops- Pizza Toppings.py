# Start an endless loop that will go on until 'quit' is entered
while True:
    # asking the id to enter a pizza topping or type 'quit' to exit
    topping = input("what would you like to have on your pizza as toppings? Or type 'quit' to finish:")
    
    # look if the id entered 'quit' (case-insensitive)
    if topping.lower() == 'quit':
        break
    else:
        # Or else, print a message telling that the topping will be added
        print(f"I'll add {topping} to your pizza!")
