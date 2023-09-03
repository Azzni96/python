user = ""
password = ""
person = 0
while user != 'python' and password != 'rules':
     if person < 5:
      user = input("Anna user: ")
      password = input("Anna password: ")
      print("Write again.")
      person += 1

print("Access denied.")
print("Welcome.")
