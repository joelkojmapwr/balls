import numpy as np

class experiment:
    n: int
    def __init__(self, n):
        self.n = n
        
    def run(self):
        box = np.zeros(self.n, dtype=int)
        count_balls = 0
        boxes_with_min_one_ball = 0
        boxes_with_min_two_balls = 0
        Bn = None
        Un = None
        Cn = None
        Dn = None
        random_generator = np.random.default_rng()
        
        while (True):
            random_ints = random_generator.integers(0, self.n, self.n)
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
                if (count_balls == self.n):
                    Un = self.n - boxes_with_min_one_ball
                
                # minimalna liczba rzutów, po której w kazdej z urn jest co najmniej jedna kula
                if (self.n - boxes_with_min_one_ball == 0 and Cn == None):
                    Cn = count_balls
                # minimalna liczba rzutów, po której w kazdej z urn s ˛a co najmniej dwie kule
                if (self.n - boxes_with_min_two_balls == 0 and Dn == None):
                    Dn = count_balls
                    return Bn, Un, Cn, Dn
        
        return None