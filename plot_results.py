from experiment import Experiment_Aggregator
from plot import Plot
import numpy as np



def main():
    experiment_aggregator = Experiment_Aggregator(1)
    experiment_aggregator.load_from_file("results.txt")
    plot = Plot(experiment_aggregator)
    
    plot.plot_max_load()
    """
    # a)
    plot.plot_results_function(plot.Bn_values, "Bn/n", lambda n: n)
    plot.plot_results_function(plot.Bn_values, "Bn/sqrt(n)", lambda n: np.sqrt(n))
    
    # b)
    plot.plot_results_function(plot.Un_values, "Un/n", lambda n: n)
    
    # c) 
    plot.plot_results_function(plot.Cn_values, "Cn/n", lambda n: n)
    plot.plot_results_function(plot.Cn_values, "Cn/(n*ln(n))", lambda n: n * np.log(n))
    plot.plot_results_function(plot.Cn_values, "Cn/n^2", lambda n: np.power(n, 2))
    
    # d)
    plot.plot_results_function(plot.Dn_values, "Dn/n", lambda n: n)
    plot.plot_results_function(plot.Dn_values, "Dn/(n*ln(n))", lambda n: n * np.log(n))
    plot.plot_results_function(plot.Dn_values, "Dn/n^2", lambda n: np.power(n, 2))
    
    # e)
    plot.plot_results_function(plot.En_values, "En/n", lambda n: n)
    plot.plot_results_function(plot.En_values, "En/(n*ln(n))", lambda n: n * np.log(n))
    plot.plot_results_function(plot.En_values, "En/(n*ln(ln(n)))", lambda n: n* np.log(np.log(n)))
    """
    
if __name__ == "__main__":
    main()