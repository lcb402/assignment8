### Laura Buchanan
### lcb402

# This main function takes positions and num_trials from user, plots histogram, and saves mean and std of daily return
import sys
from investment_instrument import *

if __name__ == "__main__":
	try:
		positions_check = 0
		while positions_check == 0:
			positions = raw_input("How many shares would you like to buy at a time?")
			valid_positions = ['1','10','100','1000']
			if positions in valid_positions:
				positions = int(positions)
				positions_check = 1
			else:
				print "Sorry, I didn't understand.  Please type 1, 10, 100, or 1000 as you input."

		num_trials_check = 0
		while num_trials_check == 0:
        		num_trials = raw_input("How many times would you like to repeat the test?")
        		valid_num_trials = range(10001)
			del valid_num_trials[0]
			valid_num_trials = map(str,valid_num_trials)
        		if num_trials in valid_num_trials:
                		num_trials = int(num_trials)
                		num_trials_check = 1
        		else:
                		print "Sorry, I didn't understand.  Please type a number between 1 and 10,000 as you input."

		invest = investment_instrument(positions,num_trials)
		invest.mean_n_std()
		invest.plot_hist()

	except KeyboardInterrupt:
		print "\nProgram ended by user."
		sys.exit(1)

	except ValueError:
		print "\nError with input format."

