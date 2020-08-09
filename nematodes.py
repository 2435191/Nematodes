# https://fivethirtyeight.com/features/can-you-reach-the-beach/
# (classic)

import random
import time; start = time.time()
class Nematode():
    def __init__(self, starting_amount):
        self.total = starting_amount

    def __str__(self):
        return str(self.total)

    def __add__(self, other): # to add nematodes: add; split into pairs (discarding 1 if odd); each pair has a 50% chance to add 1 to population count 
        number_of_pairs = (self.total + other.total) // 2
        self.total += other.total 

        for _ in range(number_of_pairs):
            self.total += random.choice([0, 1])
        
        return Nematode(self.total)

    def __pow__(self, int_):
        for _ in range(int_): # for each day...
            number_of_pairs = self.total // 2
            for _ in range(number_of_pairs): # ...have a 50% chance to add 1 to total nematode count
                self.total += random.choice([0, 1])
        return self.total


trials = 1000
for i in range(5):
    distribution = [0]*10000

    for _ in range(trials):
        distribution[(Nematode(1)+Nematode(1))**i] += 1

    expected_value = 0
    for j, num in enumerate(distribution):
        expected_value += j * num / trials

    

    print(f'distribution for {i} found in \n{time.time()-start}. \nExpected value: {expected_value}')




    
