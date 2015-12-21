### Laura Buchanan
### lcb402

import numpy as np
import matplotlib.pyplot as plt

# Class for functions used in investment modeling
class investment_instrument(object):
	def __init__(self,positions,num_trials):
		self.positions = positions
		self.num_trials = num_trials 
		self.position_value = 1000 / self.positions 
                valid_outcomes = [-1,1]
                self.daily_ret = np.random.choice(valid_outcomes, p =[0.51,0.49],size=self.num_trials)
                self.cumu_ret = [2*self.position_value*self.positions if x==1 else 0 for x in self.daily_ret]

	# Function to calulate and save mean and std of daily_ret
	def mean_n_std(self):
                daily_mean = np.mean(self.daily_ret)
                daily_std = np.std(self.daily_ret)

                results_file = open("results.txt", "a")
                results_file.write("Daily Mean " + str(self.positions) + " shares at $" + str(self.position_value) + ": " + str(daily_mean) + "\n")
                results_file.write("Daily STD " + str(self.positions) + " shares at $" + str(self.position_value) + ": " + str(daily_std) + "\n\n")
                results_file.close()

	# Function to plot and save hist for daily_ret
	def plot_hist(self):
                plt.hist(self.daily_ret,100,range=[-1,1])
                plt.xlabel('Daily Return Value')
                plt.ylabel('Daily Return Count')
                plt.title('Daily Return Histogram')
                plt.savefig('histogram_' + str(self.positions) + '_pos.pdf')

