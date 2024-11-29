

class Critter:

    def __init__(self, container, resource_dict, init_age = 0, wild = False, is_egg = False, is_lullabied = False):
        #initialising variables and conditions
        self.resource_dict = resource_dict
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

    def check_wild_incubation(self):
        #checking if wild/tame and incubated/not values should be used
        if self.wild:
            self.egg_time = self.wild_egg_time
        else:
            self.egg_time = self.tame_egg_time

        if self.lullabied:
            self.incubation_time = self.lullabied_incubation_time
        else:
            self.incubation_time = self.std_incubation_time

    def age_one_cycle(self):
        #ages by 1 cycle
        self.age += 1

        if self.is_egg is False:
            self.produce(self.resource_dict)
            self.check_age()
        else:
            self.check_age_egg()

    def check_age(self):
        #checks if critter needs to die, or lay egg
        if self.age == self.lifespan:
            self.die(self.resource_dict)
        if self.age % self.egg_time == 0 and self.age > 0:
            self.lay_egg()

    def check_age_egg(self):
        #check if egg has matured
        if self.age == self.incubation_time:
            self.age = 0
            self.is_egg = False

    def lay_egg(self):
        pass

    def produce(self):
        pass

    def die(self, resource_dict):
        pass




class Bammoth(Critter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lifespan = 200
        self.wild_egg_time = 120
        self.tame_egg_time = 12
        self.std_incubation_time = 40
        self.lullabied_incubation_time = 8
        self.check_wild_incubation()

    def lay_egg(self):
        self.container.append(Bammoth(resource_dict = self.resource_dict,container = self.container, is_egg = True, wild = self.wild, is_lullabied = self.lullabied))
    
    def produce(self, resource_dict):
        resource_dict["phosphorite"] += 10.67

    def die(self, resource_dict):
        resource_dict["meat"] += 22400

