class Array:
    def __init__(self):
        self.arr = []

    # Insert a value at a specific index
    def insert(self, index, value):
        if index < 0 or index > len(self.arr):
            print("Index out of bounds!")
            return
        self.arr.insert(index, value)

    # Delete a specific value and return its index
    def delete_by_value(self, value):
        if value in self.arr:
            index = self.arr.index(value)
            self.arr.remove(value)
            return index
        else:
            print("Value not found!")
            return -1

    # Delete a value at a specific index
    def delete_by_index(self, index):
        if index < 0 or index >= len(self.arr):
            print("Index out of bounds!")
            return
        self.arr.pop(index)

    # Display the array
    def display(self):
        print(self.arr)

    # Append a value to the end of the array
    def append(self, value):
        self.arr.append(value)

    # Reverse the array
    def reverse(self):
        self.arr = self.arr[::-1]

    # Search for a value and return its index
    def search_by_value(self, value):
        if value in self.arr:
            return self.arr.index(value)
        else:
            print("Value not found!")
            return -1


def main():
    my_array = Array()

    while True:
        print("\nMenu:")
        print("1. Insert a value at a specific index")
        print("2. Delete a specific value and return its index")
        print("3. Delete a value at a specific index")
        print("4. Display the array")
        print("5. Append a value to the array")
        print("6. Reverse the array")
        print("7. Search for a value and return its index")
        print("8. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            index = int(input("Enter the index: "))
            value = int(input("Enter the value: "))
            my_array.insert(index, value)
        elif choice == 2:
            value = int(input("Enter the value to delete: "))
            print("Deleted at index:", my_array.delete_by_value(value))
        elif choice == 3:
            index = int(input("Enter the index to delete: "))
            my_array.delete_by_index(index)
        elif choice == 4:
            my_array.display()
        elif choice == 5:
            value = int(input("Enter the value to append: "))
            my_array.append(value)
        elif choice == 6:
            my_array.reverse()
            print("Array reversed.")
        elif choice == 7:
            value = int(input("Enter the value to search: "))
            print("Found at index:", my_array.search_by_value(value))
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()