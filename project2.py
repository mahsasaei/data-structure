class Queue:
    def __init__(self, size):
        """Initialize the queue with a fixed size"""
        self.size = size
        self.queue = [None] * size
        self.front = -1  # Pointer to the front of the queue
        self.rear = -1   # Pointer to the rear of the queue

    def is_empty(self):
        """Check if the queue is empty"""
        return self.front == -1

    def is_full(self):
        """Check if the queue is full"""
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, obj):
        """Add an element to the rear of the queue"""
        if self.is_full():
            print("Queue is full! Cannot add new elements.")
            return
        if self.front == -1:  # If the queue is empty
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = obj
        print(f"Element {obj} added to the queue.")

    def dequeue(self):
        """Remove an element from the front of the queue"""
        if self.is_empty():
            print("Queue is empty! Cannot remove elements.")
            return None
        removed_obj = self.queue[self.front]
        if self.front == self.rear:  # If there is only one element left
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Element {removed_obj} removed from the queue.")
        return removed_obj

    def peek(self):
        """View the front element without removing it"""
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[self.front]

    def reverse_queue(self):
        """Reverse the queue and return a new queue"""
        if self.is_empty():
            print("Queue is empty! Cannot reverse.")
            return None
        reversed_queue = []
        if self.rear >= self.front:
            reversed_queue = self.queue[self.front:self.rear + 1][::-1]
        else:
            reversed_queue = (
                self.queue[self.front:] + self.queue[:self.rear + 1]
            )[::-1]
        print(f"Reversed queue: {reversed_queue}")
        return reversed_queue

    def display(self):
        """Display all elements in the queue"""
        if self.is_empty():
            print("Queue is empty!")
            return
        if self.rear >= self.front:
            print("Queue elements:", self.queue[self.front:self.rear + 1])
        else:
            print(
                "Queue elements:",
                self.queue[self.front:] + self.queue[:self.rear + 1],
            )


# Testing the Queue class
if __name__ == "__main__":
    q = Queue(5)  # Create a queue with capacity of 5
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    q.dequeue()
    q.display()
    print(f"Front element: {q.peek()}")
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)  # This operation should fail as the queue is full
    q.display()
    q.reverse_queue()  # Reverse the queue
    print("queue is empty?",q.is_empty())
    print("queue is full?",q.is_full())