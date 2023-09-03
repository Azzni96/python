user = ""
password = ""
person = 0
user = input("Anna user: ")
password = input("Anna password: ")
while user != 'python' and password != 'rules':
       print("Write again.")
       if person <= 5:
        user = input("Anna user: ")
        password = input("Anna password: ")
        break
        person +=1
        print("Write again.")
print("Access denied.")
print("Welcome.")