import matplotlib.pyplot as plt
import numpy as np

class Plot:
    def __init__(self, experiment_aggregator):
        self.experiments = experiment_aggregator.experiments
        self.n_values = [experiment.n for experiment in self.experiments]
        self.Bn_values = [experiment.Bn for experiment in self.experiments]
        self.Un_values = [experiment.Un for experiment in self.experiments]
        self.Cn_values = [experiment.Cn for experiment in self.experiments]
        self.Dn_values = [experiment.Dn for experiment in self.experiments]
        # En = Dn - Cn
        self.En_values = [experiment.En for experiment in self.experiments]
        self.max_load = [experiment.max_load for experiment in self.experiments]
        self.k = 50
        
        self.distinct_n_values = np.linspace(10000, 500000, 99)
        print(self.distinct_n_values)
        
    def get_average(self, n_values, y_values):
        average_values = []
        count = 0
        for i in self.distinct_n_values:
            sum = 0
            while(n_values[count] == i):
                sum += y_values[count]
                count += 1
                if (count == len(n_values)):
                    break
            current_average = sum / self.k
            average_values.append(current_average)
        
        return average_values
        
    def plot_results(self, y_values, label):
        average_values = self.get_average(self.n_values, y_values)
        plt.scatter(self.n_values, y_values, label=label, s=2)
        plt.plot(self.distinct_n_values, average_values, color="red", label=f"Average {label}")
        plt.legend()
        plt.show()

    def plot_Bn(self):
        self.plot_results(self.Bn_values, "Bn")

    def plot_Un(self):
        self.plot_results(self.Un_values, "Un")
    
    def plot_Cn(self):
        self.plot_results(self.Cn_values, "Cn")
    
    def plot_Dn(self):
        self.plot_results(self.Dn_values, "Dn")
        
    def plot_En(self):
        self.plot_results(self.En_values, "En")
    def plot_max_load(self):
        self.plot_results(self.max_load, "MaxLoad")
        
    def plot_results_function(self, y_values, label, function=None):
        average_values = self.get_average(self.n_values, y_values)
        average_values = np.array(average_values) / np.array(function(self.distinct_n_values))
        new_y_values = np.array(y_values) / (function(self.n_values))
        plt.scatter(self.n_values, new_y_values, label=label, s=2)
        plt.plot(self.distinct_n_values, average_values, color="red", label=rf'Average {label}')
        plt.legend(fontsize=16)
        plt.show()