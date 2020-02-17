class Node:
    def __init__(self, data=None, l_link=None, r_link=None):
        self.data = data
        self.l_link = l_link
        self.r_link = r_link

class DoublyLinkedList:
    def __init__(self, first=None):
        self.first = first

    def insert_front(self, data):
        n1 = Node(data)

        if self.first == None:
            self.first = n1

        else:
            n1.r_link = self.first
            self.first = n1

    def insert_rear(self, data):
        n1 = Node(data)

        if self.first == None:
            self.first = n1

        elif self.first.r_link == None:
            self.first.r_link = n1

        else:
            temp = self.first

            while temp.r_link != None:
                temp = temp.r_link

            temp.r_link = n1

    def delete_front(self):
        if self.first == None:
            return None

        elif self.first.r_link == None:
            deleted_node = self.first.data
            self.first = None

            return deleted_node

        else:
            deleted_node = self.first.data

            self.first = self.first.r_link

            return deleted_node

    def delete_rear(self):
        if self.first == None:
            return None

        elif self.first.r_link == None:
            deleted_node = self.first.data

            self.first = None

            return deleted_node

        else:
            temp = self.first

            while temp.r_link.r_link != None:
                temp = temp.r_link

            deleted_node = temp.r_link.data

            temp.r_link = None

            return deleted_node

    def display(self):
        if self.first == None:
            print("None")

        elif self.first.r_link == None:
            print(f"First <--> {self.first.data}")

        else:
            res = "First "

            temp = self.first

            while temp != None:
                res += f"<--> {temp.data} "
                temp = temp.r_link

            print(res)

if __name__ == "__main__":
    d1 = DoublyLinkedList()

    while True:
        print("*************************************************")
        print("Enter 1. to insert at front of LinkedList")
        print("Enter 2. to insert at the rear of LinkedList")
        print("Enter 3. to delete from front of the LinkedList")
        print("Enter 4. to delete from rear of the LinkedList")
        print("Enter 5. to display the LinkedList")
        print("Enter 6. to stop")

        choice = input("Enter your choice")

        if choice == "1":
            data = input("Enter the data to be inserted")
            d1.insert_front(data)

        elif choice == "2":
            data = input("Enter the data to be inserted")
            d1.insert_rear(data)

        elif choice == "3":
            print(d1.delete_front())

        elif choice == "4":
            print(d1.delete_rear())

        elif choice == "5":
            d1.display()

        else:
            break

