# Розробити клас Human.
# Human за замовчуванням  має: 
#     Енергію (energy) = 100

  
class Human():
    energy = 100
    def __init__(self, name = "", second_name = "", gender = "") -> None:
        self.name = name
        self.second_name = second_name
        self.gender = gender
    def __repr__(self) -> str:
        return f'{self.name} {self.second_name}, {self.gender};'

    def eat(self):
        self.energy = +5

    def sleep(self):
        self.energy = +10

    def talk(self):
        self.energy = -5

    def walk(self):
        self.energy = -10

    def do_homework(self):
        self.energy = -90
Mariya = Human("Mariya", "May", "female")
Maya = Human("Maya", "April", "female")
Stanislav = Human("Stanislav", "March", "male")
Oleksandr = Human("Oleksandr", "October", "male")
Oleksiy = Human("Oleksiy ", "December", "male")

Mariya.eat()
Mariya.talk()
Mariya.sleep()

Maya.walk()
Maya.do_homework()

Stanislav.do_homework()
Stanislav.sleep()
Stanislav.talk()

Oleksandr.walk()
Oleksandr.eat()

Oleksiy.do_homework()
Oleksiy.talk()
Oleksiy.sleep()

humans = [Mariya, Maya, Stanislav, Oleksandr, Oleksiy]
max_energy = 0
max_human = None
for human in humans:
    if human.energy > max_energy:
        max_energy = human.energy
        max_human = human
print(max_human.name)
