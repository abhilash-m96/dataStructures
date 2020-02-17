# Follows 'FIFO', First In First Out

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def insert(self, item):
        self.queue.append(item)

    def remove(self):
        if self.queue == []:
            return None
        else:
            return self.queue.pop(0)

    def display(self):
        return self.queue

if __name__ == "__main__":
    q = Queue()

    while(True):
        print("Enter 1 to insert into the queue \n")
        print("Enter 2 to remove item from queue \n")
        print("Enter 3 to display all the queue elements \n")
        print("Enter 4 to stop \n")

        choice = input("Enter your choice \n")

        if choice == "1":
            item = input("Enter the item to be inserted into the queue \n")
            q.insert(item)

        elif choice == "2":
            print(q.remove())

        elif choice == "3":
            print(q.display())
        else:
            break





