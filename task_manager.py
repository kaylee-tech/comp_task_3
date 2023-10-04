# Validity Check for username existing, asks user to enter existing username
def check_username(username: str, username_list: list):
    """
    Keeps asking the user to enter a username until they enter an existing one

    :param username: str, The input from the user 
    :param username_list: list, the list of stored usernames
    
    :return: str, an existing username
    """
    username_exists = False
    while username_exists == False:
        if username in username_list:
            username_exists = True
        else:
            print("Please enter an existing username")
            username = input("Please enter your username: ")
    return username


# Validity check for password existing, asks user to enter existing password
def check_password(password: str, password_list: list):
    """
    Keeps asking the user to enter a password until they enter an existing one

    :param password: str, The input from the user 
    :param password_list: list, the list of stored passwords
    
    :return: str, an existing password
    """
    password_exists = False
    while password_exists == False:
        if password in password_list:
            password_exists = True 
        else:
            print("Please enter an existing password")
            password = input("please enter your password: ")
    return password


# Checks if the username exists and asks the user for new username if so
def username_exists(username: str, username_list: list):
    """
    Keeps asking the user to enter a username, until they enter a new one

    :param username: str, The input from the user 
    :param username_list: list, the list of stored usernames
        default?? 
    
    :return: str, an new username
    """
    username_exists = True
    while username_exists == True:
        if username in username_list:
            print("This username is taken - please choose another one")
            username = input("Please enter their username: ")
        else:
            username_exists = False    
    return username


# Checks that the password and the entered confirmation match
# Asks user to re-enter password if the do not match
def password_confirmation(password: str, password_con: str):
    """
    Keeps asking the user to enter password confirmation, until password
    and password confirmation match

    :param password: str, The input from the user 
    :param password_con: str, the second input from the user
        default?? 
    
    :return: str, a password that the user entered correctly twice
    """
    password_matches = False
    while password_matches == False:
        if password == password_con:
            password_matches = True
        else: 
            print("Passwords entered do not match")
            password = input("Please enter their password: ")
            password_con = input("Please re-enter their password: ")
    return password


# Checks that the user entered exists, if not asks for new existing user
def task_user_exists(username: str, username_list: list):
    """
    Keeps asking the user to enter a username, until they enter an existing one

    :param username: str, The input from the user 
    :param username_list: list, the list of stored usernames
        default?? 
    
    :return: str, an existing username
    """
    username_exists = False
    while username_exists == False:
        if username in username_list:
            username_exists = True
        else:
            print("Please assign this take to an existing user")
            username = input("Please enter the user's name for this task: ")  
    return username


# Reads in values from text file and puts them in 2 lists
def read_values_lists():
    # Opening the textfile and reading, the usernames and passwords into a list
    user_file = open("user.txt", "r")
    lines = user_file.readlines()
    for line in lines:
        temp = line.strip().split(", ")
        user_usernames.append(temp[0])
        user_passwords.append(temp[1])
    user_file.close()
    return user_usernames, user_passwords


#====Login Section====
user_usernames = []
user_passwords = []
username_with_password = False
user_usernames, user_passwords = read_values_lists()

current_username = input("Please enter your username: ")
current_username = check_username(current_username, user_usernames)
current_password = input("please enter your password: ")
current_password = check_password(current_password, user_passwords)

# Password and username correspond with each other
while username_with_password == False:
    username_index = user_usernames.index(current_username)
    password_index = user_passwords.index(current_password)
    if username_index == password_index:
        username_with_password = True
        print(f"\nWelcome {current_username}")
    else:
        print("\nplease enter the correct login details")
        current_username = input("Please enter your username: ")
        current_username = check_username(current_username, user_usernames)
        current_password = input("please enter your password: ")
        current_password = check_password(current_password, user_passwords)

# Will continuously loop through the users menu until the user chooses to exit
while True:
    # Presents the menu to the user 
    if current_username == "admin":
        menu = input('''Select one of the following options:
                    r - register a user
                    a - add task
                    va - view all tasks
                    vm - view my tasks
                    s - statistics
                    e - exit
                    : ''').lower()
        
    else:
         menu = input('''Select one of the following options:
                    a - add task
                    va - view all tasks
                    vm - view my tasks
                    e - exit
                    : ''').lower()
    
    # Registers a new user to the user text file
    if menu == 'r' and current_username == "admin":
        print("\nRegistering a new user")
        new_username = input("Please enter their username: ")
        new_username = username_exists(new_username, user_usernames)
        new_password = input("Please enter their password: ")
        new_password_check = input("Please re-enter their password: ")
        new_password = password_confirmation(new_password, new_password_check)
        
        # Writing new user to text file
        user_file = open("user.txt", "a")
        user_file.write(f"{new_username}, {new_password}\n")
        user_file.close()
        print("The user has been added to the text file\n")

    # Adding a task to the task text file
    elif menu == 'a':
        print("\nAdding a new task")
        # Checking that the user assigned to that task exists
        task_username = input("Which user will work on this task: ")
        task_username = task_user_exists(task_username, user_usernames)
        task_name = input("Please enter the task's name: ")
        task_description = input("Please give a short overview of the task: ")
        task_start_date = input("Please enter today's date (DD MM YYYY): ")
        task_due_date = input("Please enter the due date (DD MM YYYY): ")
        task_status = "NO"
        print("")

        # Writing new information the the task textfile
        task_sen = ("\n{}, {}, {}, {}, {}, {}")
        task_sen = task_sen.format(task_username, task_name, task_description,
                                   task_start_date, task_due_date, task_status)
        task_file = open("tasks.txt", "a")
        task_file.write(task_sen)
        task_file.close()

    # Displaying all the tasks that the users need to do collectively
    elif menu == 'va':
        # Creating lists to hold task variables
        task_user_list = []
        task_name_list = []
        task_descrip_list = []
        task_sd_list = []
        task_dd_list = []
        task_stat_list = []

        # Opening tasks text file
        task_file = open("tasks.txt", "r")
        lines = task_file.readlines()
        for line in lines:
            temp = line.strip().split(", ")
            task_user_list.append(temp[0])
            task_name_list.append(temp[1])
            task_descrip_list.append(temp[2])
            task_sd_list.append(temp[3])
            task_dd_list.append(temp[4])
            task_stat_list.append(temp[5])
        task_file.close()

        # Display the tasks from the text file
        print("\nDisplaying all the tasks")
        num_counter = 1
        while(num_counter <= len(task_user_list)):
            # Format to output the results
            print("TASK " + str(num_counter))
            print("Task:\t\t" + task_name_list[num_counter-1])
            print("Assigned to:\t" + task_user_list[num_counter-1])
            print("Date assigned:\t" + task_sd_list[num_counter-1])
            print("Due date:\t" + task_dd_list[num_counter-1])
            print("Task Complete?\t" + task_stat_list[num_counter-1])
            print("Task description:\n " + task_descrip_list[num_counter-1])
            print("")
            num_counter += 1
        
    # Displaying the users Tasks
    elif menu == 'vm':
        # Creating lists to hold task variables
        task_user_list = []
        task_name_list = []
        task_descrip_list = []
        task_sd_list = []
        task_dd_list = []
        task_stat_list = []

        # Opening tasks text file
        task_file = open("tasks.txt", "r")
        lines = task_file.readlines()
        for line in lines:
            temp = line.strip().split(", ")
            task_user_list.append(temp[0])
            task_name_list.append(temp[1])
            task_descrip_list.append(temp[2])
            task_sd_list.append(temp[3])
            task_dd_list.append(temp[4])
            task_stat_list.append(temp[5])
        task_file.close()

        # Display the user's tasks from the text file
        print("\nDisplaying your tasks")
        num_counter = 1
        num_counter_user = 0
        while(num_counter <= len(task_user_list)):

            # Checking if the task belongs to the longed in user
            if(current_username == task_user_list[num_counter-1]):
                num_counter_user += 1
                # Format to output the results
                print("TASK " + str(num_counter_user))
                print("Task:\t\t" + task_name_list[num_counter-1])
                print("Assigned to:\t" + task_user_list[num_counter-1])
                print("Date assigned:\t" + task_sd_list[num_counter-1])
                print("Due date:\t" + task_dd_list[num_counter-1])
                print("Task Complete?\t" + task_stat_list[num_counter-1])
                print("Task description:\n " + task_descrip_list[num_counter-1])
                print("")
            num_counter += 1
        
        # If num_counter_user equals zero let the user know the have no tasks
        if(num_counter_user == 0):
            print("You currently have no tasks assigned to you\n")

    # Statistics for admin user
    elif menu == 's' and current_username == "admin":
        print("\nstatistics")

        # counting number of tasks
        file = open("tasks.txt", "r")
        count_task = []
        task_lines = file.readlines()
        for lines in task_lines:
            temp = lines.strip().split(", ")
            count_task.append(temp[0])
        file.close()

        # counting number of users
        file = open("user.txt", "r")
        count_user = []
        user_lines = file.readlines()
        for lines in user_lines:
            temp = lines.strip().split(", ")
            count_user.append(temp[0])
        file.close()

        # The statistic output
        print("The number of users registered is " + str(len(count_user)))
        print("The number of existing tasks are " + str(len(count_task)))
        print()

    # This will cause the loop to stop running
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # Lets the user know they entered an invalid option
    else:
        print("You have made entered an invalid input. Please try again\n")