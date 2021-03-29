from typing import List, Any


class naan_factory:


    def make_dough(self, item1, item2):
        if item1 == "water" and item2 == "flour":
            return "dough"
        elif item1 == "flour" and item2 == "water":
            return "dough"

    def bake_dough(self, item1):

        if item1 == "dough":
            return "bread"
        return "Please  try again"

    def run_factory(self, item1, item2):
        if item1 == "water" and item2 == "flour":
            return "naan"




if __name__ == "__main__":
    while True:
        user_option = input("Do you want to make naan? (exit to stop) ")
        if user_option.lower() == "exit":
            break

        item1 = input("Enter your first ingredient: ")
        item2 = input("Enter your second ingredient: ")

        naan_fact = naan_factory()
        result = naan_fact().run_factory(item1, item2)
        print(f"You have made {result}.")