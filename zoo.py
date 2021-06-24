class Animal:
    
    def __init__(self, name, age, health, happiness):
        
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):

        print(f'{self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}')
        return self

    def feed(self):

        self.health += 10
        self.happiness += 10
        return self

class Felines(Animal):
    def __init__(self, name, age, health = 50, happiness = 40, feeding = 'carnivore'):
        super().__init__(name, age, health, happiness)
    
    def fillet(self):
        self.health += 5
        self.happiness += 3
        return self
    
    def spruce_up(self):
        self.happiness += 1
        return self
        
class Primates(Animal):
    def __init__(self, name, age, health = 60, happiness = 70, feeding = 'omnivore'):
        super().__init__(name, age, health, happiness)
    
    def banana(self):
        self.health += 1
        self.happiness += 5
        return self

    def play(self):
        self.happiness += 10
        return self


class Birds(Animal):
    def __init__(self, name, age, health = 70, happiness = 30, feeding = 'insectivorous'):
        super().__init__(name, age, health, happiness)
    
    def bugs(self):
        self.health += 3
        self.happiness += 5
        return self
    
    def deworm(self):
        self.health += 15
        return self


Bear = Animal('Yogui', 20, 40, 45)

Tiger = Felines('Tonny', 15)

Lion = Felines('Simba', 3)

Chimpanzee = Primates('Bongo', 7)

Gorilla = Primates('Kong', 10)

Woodpecker = Birds('Woody', 2)

RoadRunner = Birds('Beepbeep', 3)
#Felines.fillet()
#Primates.banana()

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        
    def add_felines(self, name, age):
            self.animals.append(Felines(name, age))
            
    def add_primates(self, name, age):
        self.animals.append(Primates(name, age))
        
    def add_birds(self,name, age):
        self.animals.append(Birds(name, age))
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
            
zoo1 = Zoo("John's Zoo")

zoo1.add_felines("Tony", 15)
zoo1.add_felines('Simba',3)

zoo1.add_primates("Bongo", 7)
zoo1.add_primates("Kong", 10)

zoo1.add_birds("Woody", 2)
zoo1.add_birds("Beepbeep", 3)

zoo1.print_all_info()



while True:
    resultado = input('¿Que desea hacer? \n1: Crear un felino \n2: Crear un primate \n3: Crear un ave \n4: Alimentar \n5: Mostar info de zoo \n6: Salir \n')
    
    if resultado == '1':
        print('Crear felino:\n')
        print('Nombre y edad del felino: (nombre, edad)\n')
        name = input('Nombre: ')
        age = input('Edad: ')
        zoo1.add_felines(name, age)
    
    elif resultado == '2':
        print('Crear primate:\n')
        print('Nombre y edad del primate: (nombre, edad)\n')
        name = input('Nombre: ')
        age = input('Edad: ')
        zoo1.add_primates(name, age)
    
    elif resultado == '3':
        print('Crear ave:\n')
        print('Nombre y edad del ave: (nombre, edad)\n')
        name = input('Nombre: ')
        age = input('Edad: ')
        zoo1.add_birds(name, age)
    
    elif resultado == '4':
        feed = int(input('¿Cual animal quieres alimentar? (Elije una opción) \n1. Tony \n2. Simba \n3. Bongo \n4. Kong \n5. Woody \n6. Beepbeep \n'))
        zoo1.animals[feed-1].feed()
    
    elif resultado == '5':
        zoo1.print_all_info()
        
    elif resultado == '6':
        break
    
    else:
        print('Opción no válida')
