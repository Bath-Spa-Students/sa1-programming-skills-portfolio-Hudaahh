# Function that verifies if a number is even or odd
def check_even_or_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# Main function
def main():
    # Ask the id to input a number
    number = int(input("Enter a number: "))
    
    # Send the number to the function and output the result
    result = check_even_or_odd(number)
    print(result)

# Call the main function
if __name__ == "__main__":
    main()
