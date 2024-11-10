# Illustrate the correct password
correct_password = "12345"
# write the maximum number of attempts
max_attempts = 5
# Assign attempt counter
attempts = 0

# Loop until the id enters the correct password or reaches the maximum attempts
while attempts < max_attempts:
    # inquire the id to enter the password
    password = input("Please enter the password: ")
    
    # validate weather the entered password is correct 
    if password == correct_password:
        print("Access granted!")
        break
    else:
        # increase the attempt counter
        attempts += 1
        remaining_attempts = max_attempts - attempts
        # update the user of the incorrect password and remaining attempts
        print(f"Incorrect password. You have {remaining_attempts} attempts remaining.")
        
        # If maximum attempts are reached, inform the id
        if attempts == max_attempts:
            print("Maximum attempts reached. The authorities have been alerted.")
