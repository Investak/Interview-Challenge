#Software Engineer – Backend / Frontend challenge 
##Welcome
Welcome to the AKJ technical challenge! If you are someone who is looking to be a part of the next big company, you are here at the right place. You will be a part of a sharp, motivated and world class team working on the most ground breaking technology. 

##Basics 
The rules of this challenge are simple –

•	What you make should satisfy the challenge statement.	

•	Your code should be human readable and beautiful.

•	We at AKJ, take code organization and application architecture quite seriously.

•	Please complete the code in your own github repository and submit a pull request or submit the link to info.theakjgroup@gmail.com

##The Challenge
###What You’ll need to build:
You will need to build a sandbox for our users which lets them play around with sample stocks they might use to construct the portfolio. What they choose is not reflected in their actual choice on our production system, but you should still let them get a good sense of what would have happened had they actually chosen the stocks.

Requirements:

•	Portal login functionality – user should be able to login / logout of the interface.

•	Once logged in he should be able to select from a stocks list (provided in file [stocks list file](https://github.com/Investak/Interview-Challenge/blob/master/Stock%20List.xlsx))

•	In the ideal scenario, backend algorithm will return some weights (use some dummy weights for now) for this portfolio. You are encouraged to build your own heuristics for weights. In the simplest case, you can even assume an equal distribution.

•	Historical performance charts of the chosen portfolio vs individual stocks will be displayed in a time series (user selected time range) which will change depending upon the portfolio user selects.
An example of a historical performance graph is provided below - charts should be highly intuitive and interactive making the user experience a smooth one. 

![Imgur](http://i.imgur.com/r6PcUCP.png?1)

•	Store user history. The user should be able to see his previous selections and also visualize the previously generating graphs/charts for those selections. You can further enhance this feature by comparing the different stocks you looked at.

•	You can get historical data of stocks from Yahoo Finance or other sources on the web. Or you can use a Python module like this one here - https://pypi.python.org/pypi/yahoo-finance

##What you are encouraged to use
1.	Django
2.	ReactJS
3.	PostgreSQL

##Judging Criteria
•	What you have produced will determine your final outcome. If you like using the app, we will probably love it too, and vice versa. Please do note that the requirements above are not set in stone. If there is a feature you hate or want, please feel free to take a decision on your own. But we are looking for a kick-ass mini product. Please don't send us something even you can't use. 

•	Creativity. the challenge is intentionally left open ended. These are the kinds of open ended challenges you will face on the job too :)

•	Code readability and organization. We can't stress this enough.


##FAQs

1. What is a portfolio?

A portfolio is a collection of stocks. So for example if we have a portfolio 1 it may comprise of different stocks such as ['NIFTY', 'GOOGLE', 'APPL', etc.. ].

2. How many portfolios can a customer have?

A customer can have multiple number of portfolios depending upon how many has he locally saved in his account.

