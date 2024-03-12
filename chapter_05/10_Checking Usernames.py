current_users=["admin","Alpha5005","Beta55","Gamma99","Delta70"]
lc_current_user=[]
for user in current_users:
    lc_current_user.append(user.lower())

new_users=["PI519","Omega559","Gamma99","Delta70"]
if(new_users):
    for user in new_users:
        if user.lower() in lc_current_user:
            print(f"{user}, Not available, need to enter new username.")
        else:
            print(f"{user}, is available.")

