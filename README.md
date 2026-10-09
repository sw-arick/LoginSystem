# 🔐 Login System

A simple command-line login system written in Python. The program asks for an email and password, checks them against stored user data, and tells you whether the login succeeded.

> **Note:** This is a learning project. Credentials are hard-coded and stored in plain text, so it is not secure and should not be used in a real application.

## Features

- Email and password prompts
- Credentials matched as a pair, so one user's password can't log in another account
- Empty input check
- Clear messages for success, invalid credentials, and missing input

## How it works

1. User data is stored in a dictionary, mapping each email to its password.
2. The program asks for an email and password.
3. If either is empty, it asks the user to fill both in.
4. If the pair matches a stored user, `login()` runs. Otherwise it shows an error.

## Example

```
Enter your Email: user@example.com
Enter your Password: ********
Logged in!
```

```
Enter your Email: user@example.com
Enter your Password: wrongpass
Invalid email or password
```

## Run it locally

```bash
git clone https://github.com/sw-arick/login-system.git
cd login-system
python main.py
```

Requires Python 3. No external libraries needed.

## Concepts used

- Dictionaries for storing key-value data
- Functions to separate login and validation logic
- `input()` and string handling
- `if` / `elif` / `else` conditions

## Ideas for improvement

- Hide the password while typing with the `getpass` module
- Hash passwords instead of storing them in plain text (`hashlib` or `bcrypt`)
- Add a sign-up option to create new users
- Limit the number of failed attempts
- Save users to a file or database instead of the code

## Author

[sw-arick](https://github.com/sw-arick)
