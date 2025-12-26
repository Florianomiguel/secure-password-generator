import Password_generator.random_password as random_password

try:
    option = int(input('Do you want to create a new password [1] or check your current one [2]?: '))
    
    print('Reminder: Passwords with fewer than 8 characters are rarely considered strong.')
    
    if option == 1:
        length = int(input('Enter the length (number of characters) you want for your password: '))
        random_password.password(length)
    elif option == 2:
        user_password = input('Enter your password: ').strip()
        random_password.try_level(user_password)
    else:
        print('Invalid value, please enter only 1 or 2.')
        
except ValueError:
    print('ERROR! Please enter integers only.')