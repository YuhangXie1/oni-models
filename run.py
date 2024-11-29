import numpy as np

from model.critters import Bammoth


resource_dict = {
    "phosphorite":0,
    "meat":0
}

critters_list = []

b = Bammoth(critters_list)
critters_list.append(b)

print(critters_list)

time = range(1,400)
print(time)