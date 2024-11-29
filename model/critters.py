

class Critter:

    def __init__(self, container, init_age = 0, wild = False, is_egg = False, is_lullabied = False):
        #initialising variables and conditions
        self.container = container
        self.age = init_age
        self.wild = wild
        self.is_egg = is_egg
        self.lullabied = is_lullabied

        #initialising containers. Values populated by child class
        self.lifespan = None
        self.wild_egg_time = None
        self.tame_egg_time = None
        self.std_incubation_time = None
        self.lullabied_incubation_time = None
        self.egg_time = self.tame_egg_time
        self.incubation_time = self.std_incubation_time

        #checking if wild/tame and incubated/not values should be used
        if self.wild:
            self.egg_time = self.wild_egg_time
        if self.lullabied:
            self.incubation_time = self.lullabied_incubation_time

        def age_one_cycle(self):
            #ages by 1 cycle
            self.age += self.age

            if self.is_egg is False:
                produce()
                check_age()
            else:
                check_age_egg()

        def check_age(self):
            #checks if critter needs to die, or lay egg
            if self.age == self.lifespan:
                die()
            if self.age % self.egg_time == 0:
                lay_egg()

        def check_age_egg(self):
            #check if egg has matured
            if self.age == self.incubation_time:
                self.age = 0
                self.is_egg = False

        def lay_egg(self):
            pass

        def produce(self):
            pass

        def die(self):
            pass




class Bammoth(Critter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lifespan = 200
        self.wild_egg_time = 120
        self.tame_egg_time = 12
        self.std_incubation_time = 40
        self.lullabied_incubation_time = 8

        def lay_egg(self):
            self.container.append(Bammoth(container = self.container, is_egg = True, wild = self.wild, is_lullabied = self.is_lullabied))
        
        def produce(self, resource_dict):
            resource_dict["phosphorite"] += 10.67

        def die(self, resource_dict):
            resource_dict["meat"] += 22400

