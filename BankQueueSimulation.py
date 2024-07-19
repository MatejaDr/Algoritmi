class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def enqueue(self, value):
        self.items.append(value)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.items)
    
class Bank:
    def __init__(self, num_tellers, max_customers):
        self.num_tellers = num_tellers
        self.max_customers = max_customers
        self.queue = Queue()
        self.tellers = [None] * num_tellers

    def add_customer(self, customer):
        if self.queue.size() < self.max_customers:
            self.queue.enqueue(customer)
        else:
            print("Sorry, the bank is full. Please come back later.")
    
    def assign_teller(self):
        if not self.queue.is_empty():
            for i in range(self.num_tellers):
                if self.tellers[i] is None:
                    self.tellers[i] = self.queue.dequeue()
                    break
    
    def remove_teller(self, teller):
        if 0 <= teller < self.num_tellers and self.tellers[teller] is not None:
            self.tellers[teller] = None

    def serve_customers(self):
        while not self.queue.is_empty():
            for i in range(self.num_tellers):
                if self.tellers[i] is None:
                    self.tellers[i] = self.queue.dequeue()
                    break
            else:
                break
        
    def print_queue(self):
        print("Customers in queue:")
        for i in self.queue.items:
            print(i)

    def print_tellers(self):
        print("Tellers:")
        for i, teller in enumerate(self.tellers):
            if teller is not None:
                print(f"Teller {i}: {teller}")
            else:
                print(f"Teller {i}: None")

bank = Bank(3,5)
bank.add_customer("Milan")
bank.add_customer("Zoran")
bank.add_customer("Stojan")
bank.add_customer("Bojan")
bank.add_customer("Goran")
bank.print_queue()
bank.serve_customers()
bank.print_queue()
bank.print_tellers()
bank.remove_teller(0)
bank.print_tellers()