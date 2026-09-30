books = ["Python", "Java", "Machine Learning"]

print("Library Management System")
print("Available Books:")

for book in books:
    print(book)

username = input("Enter username: ")

if username:
    print("Login successful")
else:
    print("Login failed")