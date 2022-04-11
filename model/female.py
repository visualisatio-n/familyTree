from model.person import Person


class Female(Person):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.husband = None
        self.children = list()

    def add_child(self, child: Person):
        self.children.append(child)
