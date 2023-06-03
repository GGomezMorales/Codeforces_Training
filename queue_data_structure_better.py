class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        """
        Evaluates is the queue is empty
        """
        return self.front is None

    def enqueue(self, item):
        """
        This operation is used to store the elements in the queue (rear)
        """
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """
        This operation is used to remove the elements in the queue (front)
        """
        if self.is_empty():
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return f'Acabo de eliminar: {item}'

    def peek(self):
        """
        Get the element from the front of the queue without removing it
        """
        if self.is_empty():
            return None
        return self.front.data

    def size(self):
        """
        Mejorar
        """
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def show_queue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self.front
            queue_list = []
            while current:
                queue_list.append(current.data)
                current = current.next
            print(queue_list)
