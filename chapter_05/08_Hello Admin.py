usernames=["admin","Alpha5005","Beta55","Gamma99","Delta70"]
for user in usernames:
    if(user == "admin"):
        print("Hello admin, would you like to see status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
