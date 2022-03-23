class Stationery:
    title = None

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self):
        super().__init__()
        self.title = "ручка"

    def draw(self):
        print("Пишем текст")
        return None


class Pencil(Stationery):
    def __init__(self):
        super().__init__()
        self.title = "карандаш"

    def draw(self):
        print("Чертим чертеж")
        return None


class Handle(Stationery):
    def __init__(self):
        super().__init__()
        self.title = "маркер"

    def draw(self):
        print("Выделяем заголовки")
        return None


pen = Pen()
pencil = Pencil()
handle = Handle()

for some in [pen, pencil, handle]:
    print(f"{some.__class__}:title = {some.title}")
    print(f"{some.__class__}.draw() =>\t", end="")
    some.draw()
