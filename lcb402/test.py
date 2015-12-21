### Laura Buchanan
### lcb402

import unitest
from investment_instrument import *

class test_investment_instrument(unittest.Testcase):
	
	def test_invest(self):
		self.assertEqual(investment_instrument[1,10,100,1000],['1','10','100','1000'])

if __name__ == '__main__':
    unittest.main()
