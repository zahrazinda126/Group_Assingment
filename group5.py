class StudentQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, student):
        self.queue.append(student)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage:
queue = StudentQueue()

# Students joining the queue
students = ["Zahara", "Ssendi", "Arapta", "Pouch"]
for student in students:
    queue.enqueue(student)
    print(f"{student} joined the queue.")

# Current queue size
print("\nQueue size:", queue.size())

# Dequeue students being served
print("\nStudents being served:")
for _ in range (len(students)):
    # print dequeue value
    print(queue.dequeue())
    print(queue.size())

# Current queue size after serving
print("\nQueue size after serving:", queue.size())

# Check if the queue is empty
print("\nIs the queue empty?", queue.is_empty())
