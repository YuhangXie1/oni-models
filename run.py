import numpy as np
import matplotlib.pyplot as plt

from model.critters import Bammoth


resource_dict = {
    "phosphorite":0.0,
    "meat":0.0
}

critters_list = []

b = Bammoth(resource_dict = resource_dict, container = critters_list)
critters_list.append(b)

print(critters_list)

time = np.arange(1,201)
population = []

for t in time:
    for critter in critters_list:
        critter.age_one_cycle()
    population.append(len(critters_list))

def count(container):
    critters = 0
    eggs = 0


plt.plot(time, population)
plt.savefig("output.png")
