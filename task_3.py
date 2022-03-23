class Worker:
    name = None
    surname = None
    position = None
    _income = {"wage": 100.0, "bonus": 1.5}


    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income["wage"] * self._income["bonus"]


position = Position("Ivan", "Ivanov", "Teacher", {"wage": 1000.0, "bonus": 1.5})
position.position += " School"
print(position.get_full_name.__name__, position.get_full_name())
print(position.position)
print(position.get_total_income.__name__, position.get_total_income())
