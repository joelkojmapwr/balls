from experiment import Experiment
from experiment import Experiment_Aggregator

def main():
    
    experiment_aggregator = Experiment_Aggregator(1)
    for n in range (10000, 500001, 5000):
        print(f"Experiment run for n={n}")
        for k in range(0, 50):
            experiment = Experiment(n, 1)
            experiment.run()
            experiment_aggregator.add_experiment(experiment)
    experiment_aggregator.save_to_file("results.txt")
    
    experiment_aggregator2 = Experiment_Aggregator(2)
    for n in range (10000, 500001, 5000):
        print(f"Experiment run for n={n}")
        for k in range(0, 50):
            experiment = Experiment(n, 2)
            experiment.run()
            experiment_aggregator2.add_experiment(experiment)
    experiment_aggregator2.save_to_file("results2.txt")
        
if __name__ == "__main__":
    main()