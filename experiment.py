import numpy as np
from numba import njit

"""
d - number of boxes to choose the lowest from them
"""
@njit
def experiment_run(n, d):
    #print(f"Experiment run for d={d}")
    box = np.zeros(n, dtype=np.int32)
    count_balls = 0
    boxes_with_min_one_ball = 0
    boxes_with_min_two_balls = 0
    Bn = -1
    Un = -1
    Cn = -1
    Dn = -1
    max_load: int
    random_generator = np.random
    
    while (True):
        random_ints = random_generator.randint(0, n, n * 16 * d)
        
            
        for itr in range (0, len(random_ints), d):
            min_box: int # index of the box with the smallest amount of balls
            min_box = random_ints[itr]
            for k in range (itr+1, itr+d, 1):
                if (box[random_ints[k]] < box[min_box]):
                    min_box = random_ints[k]
            
            count_balls += 1
            if (box[min_box] == 0):
                boxes_with_min_one_ball += 1
            elif (box[min_box] == 1):
                if (boxes_with_min_two_balls == 0):
                    Bn = count_balls
                boxes_with_min_two_balls += 1
            
            box[min_box] += 1
            # liczba pustych urn po wrzuceniu n kul
            if (count_balls == n):
                Un = n - boxes_with_min_one_ball
                max_load = max(box)
            
            # minimalna liczba rzutów, po której w kazdej z urn jest co najmniej jedna kula
            if (n - boxes_with_min_one_ball == 0 and Cn == -1):
                Cn = count_balls
            # minimalna liczba rzutów, po której w kazdej z urn s ˛a co najmniej dwie kule
            if (n - boxes_with_min_two_balls == 0 and Dn == -1):
                Dn = count_balls
                return Bn, Un, Cn, Dn, max_load
    
    return None

class Experiment:
    def __init__(self, n, d):
        self.d = d
        self.n = n
    
    def run(self):
        self.Bn, self.Un, self.Cn, self.Dn, self.max_load = experiment_run(self.n, self.d)
        self.En = self.Dn - self.Cn
        
class Experiment_Aggregator:
    def __init__(self, d):
        self.d = d
        self.experiments = []
        
    def add_experiment(self, experiment):
        self.experiments.append(experiment)
        
    def get_experiments_count(self):
        return len(self.experiments)
    
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            for experiment in self.experiments:
                f.write(f"{experiment.n} {experiment.Bn} {experiment.Un} {experiment.Cn} {experiment.Dn} {experiment.En} {experiment.max_load}\n")
                
    def load_from_file(self, filename):
        self.experiments = []
        with open(filename, "r") as f:
            for line in f:
                n, Bn, Un, Cn, Dn, En, max_load = map(int, line.split())
                experiment = Experiment(n, self.d)
                experiment.Bn = Bn
                experiment.Un = Un
                experiment.Cn = Cn
                experiment.Dn = Dn
                experiment.En = En
                experiment.max_load = max_load
                self.experiments.append(experiment)
    