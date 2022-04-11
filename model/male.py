from model.person import Person


class Male(Person):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.wife = None
