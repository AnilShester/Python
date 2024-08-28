usernames = ["anilshester","anilshester1", "anilshester2","anilshester3","anilshester4", "anilshester5", "admin"]

for username in usernames:
    if username.lower() == "admin":
        print("Hello " + username + ", would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again")

current_users = ["anilshester","anilshester1", "anilshester2","anilshester3","anilshester4", "anilshester5", "admin"]
new_users =["anilshester6","anilshester7","anilsheter8","anilshester3", "anilShester2"]

for new_user in new_users:
    if new_user.lower() not in current_users.lower():
        print("Username " + new_user + " is avaliable.")
    else:
        print("Username " + new_user + " is already taken.")

