from experiment import Experiment
from experiment import Experiment_Aggregator

def main():
    experiment_aggregator = Experiment_Aggregator()
    for n in range (1000, 100001, 1000):
        for k in range(0, 50):
            experiment = Experiment(n)
            experiment.run()
            experiment_aggregator.add_experiment(experiment)
    
    print(f"Experiments count: {experiment_aggregator.get_experiments_count()}")
    experiment_aggregator.save_to_file("results.txt")
        
if __name__ == "__main__":
    main()