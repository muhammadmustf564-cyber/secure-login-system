users = {
    "ali":"1234",
    "ahmad":"9815",
    "adil":"7890"
}

for attempt in range(3):
    username = input("Enter username:")
    password = input("Enter password:")
    
    try:
       if username in users and users[username] == password:
           print("login successful")
           with open("log.txt","a") as f:
               f.write(f"{username} - success\n")
           break
       else:
           print("wrong credentials")
           with open("log.txt","a") as f:
               f.write(f"{username} - fail\n")
    except:
        print("Invalid input")
else:
    print("Account Locked")

           
               