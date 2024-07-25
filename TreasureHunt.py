class Node:
    def __init__(self, clue, question, answer):
        self.clue = clue
        self.question = question
        self.answer = answer
        self.prev = None
        self.next = None

class TreasureHunt:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_clue(self, clue, question, answer):
        new_node = Node(clue, question, answer)
        if self.head is None:
            self.head = self.tail = self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def move_next(self):
        if self.current.next is not None:
            self.current = self.current.next
        else:
            print("You have reached the end of the treasure hunt!")

    def move_prev(self):
        if self.current.prev is not None:
            self.current = self.current.prev
        else:
            print("You are at the beginning of the treasure hunt")

    def ask_question(self):
        if self.current is not None:
            print(f"Clue: {self.current.clue}")
            answer = input(f"Question: {self.current.question}\n Your answer: ")
            if answer.lower() == self.current.answer.lower():
                print("Correct!")
                if self.current.next is not None:
                    print("Moving to the next clue.\n")
                    self.move_next()
                    return True
                else:
                    print("You have reached the end of the treasure hunt!")
                    return False
            else:
                print("Incorrect! Moving to the previous clue.\n")
                self.move_prev()
                return True
        else:
            print("No more clues available.")
            return False


def MainCode():
    treasure_hunt = TreasureHunt()
    treasure_hunt.add_clue("Clue 1", "What is 2+2?", "4")
    treasure_hunt.add_clue("Clue 2", "What is the capital of France?", "Paris")
    treasure_hunt.add_clue("Clue 3", "What is the largest ocean?", "Pacific")
    treasure_hunt.add_clue("Clue 4", "What planet is known as the Red Planet?", "Mars")

    while True:
        if not treasure_hunt.ask_question():
            break

MainCode()

