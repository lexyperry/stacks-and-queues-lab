import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # TODO: Add an item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # TODO: Remove and return the item from the front of the queue
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"Dequeued {removed} | Queue: {self.items}")
            return removed
        else:
            return None 

    def peek(self):
        # TODO: Return the item at the front of the queue without removing it
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        # TODO: Return True if the queue is empty
        return len(self.items) == 0

    def select_and_announce_winner(self):
        if not self.items:
            return None

        winner = random.choice(self.items)
        print(f"The winner is {winner}!")
        dequeued = []
        while self.items:
            current = self.dequeue()
            dequeued.append(current)
            if current == winner:
                break
        return winner
