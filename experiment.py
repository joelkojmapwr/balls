import numpy as np
from numba import njit


@njit
def experiment_run(n):
    box = np.zeros(n, dtype=np.int32)
    count_balls = 0
    boxes_with_min_one_ball = 0
    boxes_with_min_two_balls = 0
    Bn = -1
    Un = -1
    Cn = -1
    Dn = -1
    random_generator = np.random
    
    while (True):
        random_ints = random_generator.randint(0, n, n * 16)
        for i in random_ints:
            count_balls += 1
            if (box[i] == 0):
                boxes_with_min_one_ball += 1
            elif (box[i] == 1):
                if (boxes_with_min_two_balls == 0):
                    Bn = count_balls
                boxes_with_min_two_balls += 1
            
            box[i] += 1
            # liczba pustych urn po wrzuceniu n kul
            if (count_balls == n):
                Un = n - boxes_with_min_one_ball
            
            # minimalna liczba rzutów, po której w kazdej z urn jest co najmniej jedna kula
            if (n - boxes_with_min_one_ball == 0 and Cn == -1):
                Cn = count_balls
            # minimalna liczba rzutów, po której w kazdej z urn s ˛a co najmniej dwie kule
            if (n - boxes_with_min_two_balls == 0 and Dn == -1):
                Dn = count_balls
                return Bn, Un, Cn, Dn
    
    return None

class Experiment:
    def __init__(self, n):
        self.n = n
    
    def run(self):
        self.Bn, self.Un, self.Cn, self.Dn = experiment_run(self.n)
        self.En = self.Dn - self.Cn
        
class Experiment_Aggregator:
    def __init__(self):
        self.experiments = []
        
    def add_experiment(self, experiment):
        self.experiments.append(experiment)
        
    def get_experiments_count(self):
        return len(self.experiments)
    
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            for experiment in self.experiments:
                f.write(f"{experiment.n} {experiment.Bn} {experiment.Un} {experiment.Cn} {experiment.Dn} {experiment.En}\n")
                
    def load_from_file(self, filename):
        self.experiments = []
        with open(filename, "r") as f:
            for line in f:
                n, Bn, Un, Cn, Dn, En = map(int, line.split())
                experiment = Experiment(n)
                experiment.Bn = Bn
                experiment.Un = Un
                experiment.Cn = Cn
                experiment.Dn = Dn
                experiment.En = En
                self.experiments.append(experiment)
    