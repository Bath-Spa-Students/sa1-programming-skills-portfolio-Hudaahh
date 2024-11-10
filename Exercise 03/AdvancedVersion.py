# collect id input for name, hometown, and age
name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")

# operate an input for age and check weather it is a valid number
while True:
    try:
        age = int(input("Enter your age: "))  # Change input to an integer
        break  # Quit the loop if the age is a valid number
    except ValueError:
        print("Please enter a valid number for age.")

# obtain  information in a dictionary
person_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

#  publish the values on separate lines using a single print statement
print(f"\nName: {person_info['name']}")
print(f"Hometown: {person_info['hometown']}")
print(f"Age: {person_info['age']}")
