#Write a program to create a list and perform various operations on list using menu.

my_list = []

while True:
    print("\n--- List Operations Menu ---")
    print("1. Create List")
    print("2. Display List")
    print("3. Add Element")
    print("4. Remove Element")
    print("5. Search Element")
    print("6. Sort List")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of elements: "))
        my_list = []
        for i in range(n):
            val = int(input(f"Enter element {i+1}: "))
            my_list.append(val)
        print("List created successfully!")

    elif choice == 2:
        print("Current List:", my_list)

    elif choice == 3:
        val = int(input("Enter element to add: "))
        my_list.append(val)
        print("Element added!")

    elif choice == 4:
        val = int(input("Enter element to remove: "))
        if val in my_list:
            my_list.remove(val)
            print("Element removed!")
        else:
            print("Element not found!")

    elif choice == 5:
        val = int(input("Enter element to search: "))
        if val in my_list:
            print("Element found in list!")
        else:
            print("Element not found!")

    elif choice == 6:
        my_list.sort()
        print("List sorted!")

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
