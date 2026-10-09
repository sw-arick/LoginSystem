users = {
    "elon@gmail.com": "ElonMusk",
    "mark@gmail.com": "MarkZuck",
}

def login():
    print("logged in!")

def validateData():
    email = input("Enter your Email: ").strip()
    password = input("Enter your Password: ")

    if email == "" or password == "":
        print("Please enter your email and password")
    elif users.get(email) == password:
        login()
    else:
        print("Invalid email or password")