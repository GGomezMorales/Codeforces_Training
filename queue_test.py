from queue_data_structure_better import Queue

my_queue = Queue()

my_queue.enqueue("Maxwell")
my_queue.enqueue("Faraday")
my_queue.enqueue("Ampere")

print(my_queue.size())
print(my_queue.peek())
print(my_queue.dequeue())
print(my_queue.peek())
print(my_queue.size())

