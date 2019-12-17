## Write Python Code To Implement The Following Problem Statement

Assume that you and your friend want to test your investment strategies. While you feel that the stocks that gave HIGHEST returns on the previous day will give the highest return on the current day also, your friend feels that stocks that gave the LOWEST returns on the previous day will give the highest returns on the current day. 

What is the best way to resolve this argument? Go and simulate your respective strategies over a period of 5 years by starting with an investment of $100 each for the whole duration. Keep buying and selling every day and see who ends up with the most amount of money

We have provided the historical closing prices of 10 US stocks. Write python code to simulate the above strategies for a period of 5 years starting from Jan 1st, 2015. 

On the first day, for the first strategy, you invest $100 in the top 3 stocks that gave the HIGHEST returns on the previous day, in the second strategy you invest $100 in 3 stocks that gave the LEAST returns on the previous day. 

The Second day, you SELL whatever you have in hand and BUY NEW stocks based on the above rules respectively. 

Keep repeating these steps until the end of time

Get back to us with the CSV files containing stock selection, investment & returns for each day for 2 strategies starting from Jan 1’ 2015 and visualizations for how the initial $100 investment progressed over the period in each case. 

## Inputs Files Folder link:
	https://drive.google.com/drive/folders/1CFsTnXW1OUuFdjXkH03z3bf5vKHVU2JB?usp=sharing


Note: 
You must invest equal amounts in all the stocks you pick for a strategy in a day 
It’s ok if you can only buy a fraction of stocks with the money you have (That is it' perfectly ok if you can buy 0.35 stocks of a certain company)




==========

## Example:

Let’s say A, B, C, D… J are the 10 companies in the superset.
On Jan 1st, 2015 stocks A, C, D gave the highest returns  while the stocks E, F, J gave the lowest returns 
On 2nd Jan 2015, Since its the first day and you are supposed to invest $100 into each portfolio, that is $100 in portfolio of stocks which gave highest returns(Let’s call this “Port-X”) and $100 on portfolio of stocks which gave the lowest returns(Let’s call this “Port-Y”)
Split $100 of Port-X and invest $33.33 into A, $33.33 into C and $33.33 into D
Split $100 of Port-Y and invest $33.33 into E, $33.33 into F and $33.33 into J
On 3rd Jan 2015, see which stocks gave the highest returns on 2nd Jan. Let’s say stocks H, I, J gave the highest returns.
Sell A, C, D which were bought on 2nd Jan. Let’s say you got $102.5 by selling these stocks. Split the money equally and invest $34.2 into H, $34.2 into I and $34.2 into J
Similarly if on 2nd Jan lets say D, E, F gave the lowest returns
Sell E, F, J on 3rd Jan and invest the money in D, E, F
Repeat this till the end of time
