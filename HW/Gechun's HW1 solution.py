# Gechun's HW1 solution

import random


# create a class Portfolio
class Portfolio():   
    def __init__(self):
    	self.cash = 0  ## initial amount of cash is 0
    	self.stock = {}  ## dictionary of all stock purchased or sold
    	self.buyprice = {}  ## dictionary to store the prices of all stock purchased
    	self.mutualfunds = {}  ## dictionary of all mutual funds purchased or sold
    	self.history = []  ## list of history of all transactions

    # add a method to add cash to the total amount of cash  	
    def addCash(self, amount):
		self.cash = self.cash + amount  ## update the cash amount
		thishistory = "Add cash $" + str(amount)  
		self.history.append(thishistory)  ## record the adding of cash

	# add a method to buy stock
	def buyStock(self, shares, stock):
		if type(shares) != int:  ## check if the amount of shares is an integer
			return "Stocks can only be purchased as whole units."
		else:
			stockamount = shares * stock.price
		    if  stockamount <= self.cash:  ## check if the account have enough money to buy stock
		    	thishistory = "Buy " + str(shares) + " share(s) of " + str(stock.name)
		        self.history.append(thishistory) ## record the buying of stock
                self.cash = self.cash - stockamount ## update the cash amount
                self.buyprice[stock.name] = stock.price ## store the buying price of this stock which will be used later in selling
                if stock.name in self.stock:  ## check if one has purchased the same stock before:  
                	originalshares = self.stock[stock.name]  
                    self.stock[stock.name] = originalshares + shares  ## if so, add the new purchased amount to the existing amount
                else:
                	self.stock[stock.name] = shares ## if not, add a new item with the stock name and amount purchased
			else: 
			    return "Not enough cash to buy."
		
	# add a method to buy mutual fund
	def buyMutualFund(self, shares, fund):
		fundamount = shares * 1
		if  fundamount <= self.cash:  ## check if the account have enough money to buy stock
			thishistory = "Buy " + str(shares) + " share(s) of " + str(fund.name)
		    self.history.append(thishistory)  ## record the buying of mutual funds		
			self.cash = self.cash - fundamount  ## update the cash amount
			if fund.name in self.mutualfunds:  ## check if one has purchased the same mutual fund before:  
                originalshares = self.mutualfunds[fund.name]
                self.mutualfunds[fund.name] = originalshares + shares  ## if so, add the new purchased amount to the existing amount
            else:
                self.mutualfunds[fund.name] = shares ## if not, add a new item with the mutual fund name and amount purchased
		else: 
			return "Not enough cash to buy."

    # add a method to sell mutual fund
    def sellMutualFund(self, name, shares):
    	if name in self.mutualfunds:  ## check if one has purchased this mutual fund before
    		if shares > self.mutualfunds[name]:  ## check if one sell more than the existing amount
    			return "Your shares of this mutual fund are less than the amount you want to sell."
    		else:
    	        sellprice = random.uniform(0.9, 1.2)  ## randomly choose a sell price from a uniform distribution
    	        self.cash = self.cash + sellprice*shares  ## add the amount of selling mutual fund back to cash
    	        thishistory = "Sell " + str(shares) + " share(s) of " + name  
		        self.history.append(thishistory)   ## record the selling of mutual fund
		        originalshares = self.mutualfunds[name]
		        self.mutualfunds[name] = originalshares - shares ## update the amount of shares left
		else:
			return "You do not have any amount of shares left in this mutual fund."


    # add a method to sell stock
    def sellStock(self, name, shares):
    	if type(shares) != int:
			return "Stocks can only be sold as whole units."
		else:
			if name in self.stock:
    		    if shares > self.stock[name]:  ## check if one sell more than the existing amount
    			   return "Your shares of this stock are less than the amount you want to sell."
    		    else:
    	            sellprice = random.uniform(0.5*self.buyprice[name], 1.5*self.buyprice[name]) ## randomly choose a sell price from a uniform distribution
    	            self.cash = self.cash + sellprice*shares  ## add the amount of selling stock back to cash
    	            thishistory = "Sell " + str(shares) + " share(s) of " + name  
		            self.history.append(thishistory)   ## record the selling of stock
		            originalshares = self.stock[name]
		            self.stock[name] = originalshares - shares  ## update the amount of shares left
		    else:
			    return "You do not have any amount of shares left in this stock."

    	    
    # add a method to withdraw cash
    def withdrawCash(self, amount):
    	if amount <= self.cash:  ## check if one withdraw more than the existing amount
    	   self.cash = self.cash - amount  ## update the cash amount
    	   thishistory = "Withdraw cash $" + str(amount)  
		   self.history.append(thishistory)  ## record the withdrawing of cash
		else:
			return "Not enough cash to withdraw."



    # add a print method to return all types of assets in one's portfolio
	def __str__(self):
		return 'cash: $' + str(self.cash) + '\nstock: ' + str(self.stock) + '\nmutualfunds: ' + str(self.mutualfunds)


    # add a method to print all history
    def history(self):
        return '\n'.join(self.history) 

# create a new class Stock
class Stock():
    def __init__(self, price, name):
    	self.price = price
    	self.name = name

    	 
# create a new class MutualFund
class MutualFund():
    def __init__(self, name):
    	 self.name = name


# test 
portfolio = Portfolio() # creat a new account
portfolio.addCash(300.50)
s = Stock(20, "HFH") 
portfolio.buyStock(5, s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT") 
portfolio.buyMutualFund(10.3, mf1) 
portfolio.buyMutualFund(2, mf2)
print(portfolio) # print all assets before selling

portfolio.sellMutualFund("BRT", 3) 
portfolio.sellStock("HFH", 1) 
portfolio.withdrawCash(50) 
print(portfolio) # print all assets after selling

portfolio.history # print the history of all transaction





