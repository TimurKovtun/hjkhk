class samalet:
    model = "Aerobus a 380"
    speed = 3000

class pasanger:
    def __init__(self, name, *args, **kwards):
        super().__init__(*args, **kwards)
        self.name = name
        self.ves = 5000

class airport(samalet):
    distance = 30000

    def ran(self):
        self.time = self.distance/self.speed
        print(f" Время пути{self.time} ")



class ticket(pasanger, airport):
    def print_ticket(self):
        print(f"Самолет:{self.model}")
        print(f"Пассажир:{self.name}")
        super().ran()
        print(f"Вес багажа:{self.ves}")

a=ticket(name= "Тимур")
a.print_ticket()