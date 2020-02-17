class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack == []:
            return None
        else:
            return self.stack.pop()

    def display(self):
        if self.stack == []:
            return None
        else:
            return self.stack

    def is_empty(self):
        return self.stack == []

if __name__ == "__main__":
    s = Stack()

    while True:
        print("Enter 1 to insert elements into the stack \n")
        print("Enter 2 to pop an element from a stack \n")
        print("Enter 3 to display the elements \n")
        print("Enter 4 to stop \n")
        choice = input("Enter your choice \n")

        if choice == "1":
            item = input("Enter the item to be inserted into the stack")
            s.push(item)

        elif choice == "2":
            print(s.pop())

        elif choice == "3":
            print(s.display())

        else:
            break

