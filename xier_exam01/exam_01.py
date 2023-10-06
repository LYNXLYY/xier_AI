import json
import time
import numpy as np
import  random
#1
def decorator(func):
    def wrapper(*args, **kwargs):
        start_time =time.time()
        result = func(*args, **kwargs)
        print(result)
        end_time = time.time()
        print("start_time=",start_time)
        print("end_time",end_time)
        print("run_time",end_time-start_time)
        return wrapper
matrix=np.ones((5,10))
print(matrix)
print(matrix.T)
#2
type1 = ['♠', '♥', '♦', '♣']
type2 = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
add = [ty1+ty2 for ty1 in type1 for ty2 in type2]
add.append("joker1")
add.append("joker2")
random.shuffle(add)
#3
player1 = add[:17]
player2 = add[17:34]
player3 = add[34:51]
others = add[51:]
print(player1)
print(player2)
print(player3)
print(others)
with open('player1.json', 'w') as f:
    json.dump(player1,f)
with open('player2.json', 'w') as f:
    json.dump(player2,f)
with open('player3.json', 'w') as f:
    json.dump(player3,f)
with open('others.json', 'w') as f:
    json.dump(others,f)
#4
class MyZoo:
    def __init__(self, animals=None):
        if animals == None:
            self.animals = {}
            print("My Zoo!")
        else:
            self.animals = animals
            print("My Zoo!")

    def __eq__(self, other):
        return self.animals.keys() == other.animals.keys()

    def __len__(self):
        return sum(self.animals.values())

myzoo1 = MyZoo({"pig": 1,"dog":6})
myzoo2=MyZoo()
myzoo3 = MyZoo({"pig": 1})
myzoo4 = MyZoo({"pig": 5})


print(myzoo3 == myzoo4)
print(len(myzoo1))

