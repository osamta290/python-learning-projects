# User Registration System

users = []


def show_users(users):
    for user in users:
        print(f"User: {user[0]} | Age: {user[1]}")


while True:
    name = input("Enter your name: ")

    while True:
        try:
            age = int(input("Enter your age: "))

            if age > 0:
                break
            else:
                print("Age must be greater than zero.")

        except ValueError:
            print("Please enter numbers only!")

    users.append([name, age])

    out = input("Do you want to register another user? ").lower()

    if out == "yes":
        continue
    else:
        break

print("Registration complete!")
show_users(users)
