contacts = {}

def add_contact(name, phone, email):
  contacts[name] = {"phone": phone, "email": email}

def show_contacts():
  if not contacts:
    print("Your contact book is empty.")
  else:
    print("**Contacts:**")
    for name, info in contacts.items():
      print(f" - {name}:")
      print(f"   Phone: {info['phone']}")
      if info["email"]:
        print(f"   Email: {info['email']}")

def search_contact(name):
  if name in contacts:
    info = contacts[name]
    print(f"**Found contact:**")
    print(f" - Name: {name}")
    print(f"   Phone: {info['phone']}")
    if info["email"]:
      print(f"   Email: {info['email']}")
  else:
    print(f"Contact '{name}' not found.")

while True:
  print("\n**Contact Book Menu:**")
  print("1. Add a new contact")
  print("2. Show all contacts")
  print("3. Search for a contact")
  print("4. Quit")

  choice = input("Enter your choice: ")

  if choice == "1":
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address (optional): ")
    add_contact(name, phone, email)
  elif choice == "2":
    show_contacts()
  elif choice == "3":
    name = input("Enter name to search for: ")
    search_contact(name)
  elif choice == "4":
    break
  else:
    print("Invalid choice. Please try again.")

print("Thank you for using your contact book!")