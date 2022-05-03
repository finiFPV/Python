def save(
    user_name,
    password1,
    email,
    hardwareid,
    membership,
    admin,
    owner,
    time,
    level,
    special_key,
):
    save_dict = {
        "user": user_name,
        "password": password1,
        "email": email,
        "hardwareid": hardwareid,
        "membership": membership,
        "admin": admin,
        "owner": owner,
        "time": time,
        "level": level,
    }
    with open("util\\database.txt", "a+") as save:
        save.write(f"{special_key}{save_dict}")
        save.write("\n")
    save.close()