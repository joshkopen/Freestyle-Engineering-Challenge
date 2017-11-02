# Freestyle Engineering Challenge

Test cases in test cases folder, with test case #1 already stored in the base folder. The text and settings file must be in the same folder as the main.py in order to run properly.

Link to github of project:


## Algorithm Explanation:

This algorithm aims to give the user the best possible number of items to buy based on the information provided. Firstly, the budget must be supplied in the settings.py file as an integer. Also inside settings.py is a number called food ratio which must be a number between 0 and 1 that states how much food should be bought versus the amount of drinks. This allows for the algorithm to be flexible as the user may want more food than drinks at their party. The algorithm then uses the list of preferences in order to create a percentage of how much each food/drink takes up of the total preferences. It then spends that percentage of the budget on that item. It does this separately for food and drink on their individual budgets. The algorithm assumes however that you can only buy whole numbers of the objects; for example, it does not allow buying 2.56 burgers, but would instead round this down to 2. This then leaves leftover budget, which the algorithm then tackles by trying to spend all the remaining money. It compiles a list of the most popular food and drink items together and tries to buy as many of the items as possible starting with the most popular and working down to the least popular. This final portion chooses to handle food and drink together based purely on their popularity, as it is the best way not to skew the given food ratio in settings.py. This will leave the user with less money remaining than the cheapest food item.

This algorithm was chosen because of my opinion that it gives the best representation of how preferences work. Alternatively, the algorithm could have tried to have the percentage of preferences match the amount of items bought, rather than a percentage representation of the money spent on items. Even further, a different algorithm could have tried to make sure every person had at least one of their preferences purchased. Ultimately, I think that my algorithm would work best with a really large group of people that does not necessarily care about outlier individuals, but instead tries to cater to the masses. My algorithm may work better for planning a 200 person wedding than it would planning a small dinner party where it'll be really obvious if one of your 4 guests does not get a food they prefer. My algorithm also tends to favor cheap items and buy more food total than the other algorithms would and uses the budget more completely, which I thought was the best result for an algorithm of this kind.


## Assumptions:

This solution does rely on several key assumptions.
1. It assumes the user will properly format the input files. If they are not formatted correctly, the program will throw an error and not return an answer. 
2. It assumes normal ideas about cost such as the idea that the cost will not be negative, as this would completely destroy the numbers in the algorithm.
3. It assumes that the currency is not necessarily in dollars or any other specific currency. This solution allows for money to go down to many decimal places. Although it would be possible to have the amounts round to two decimal places, with the rise of kryptocurrency which allows for much smaller denominations of money, this solution chooses to remain more general in its allowance of decimal places.
4. It assumes that each user is of completely equal value in the people.txt document. It does not give any weight to any singular person's choices any more than the rest. It would be possible in a different situation to have a weighting number in people.txt which would allow a person's opinon to mean more if they were perhaps some important political figure or celebrity. The algorithm would then have to be changed in the section which counts percentages by multiplying the preferences of these individuals. 
5. It assumes that all items which appear in people.txt also appear in food.txt and drinks.txt respectively.
6. It assumes that the host wants to spend as much of the budget as possible. The algorithm would be completely different if it were assumed that the host wanted to spend as little as possible to just get one satisfactory item for each of his guests.

## Intended Test Case Results

### Test Case 1

The algorithm has determined that you should buy the amounts of the following drinks: 
coke: 3
pepsi: 3
fanta: 0
water: 12
The algorithm has determined that you should buy the amounts of the following foods: 
burger: 2
hotdog: 7
cheeseburger: 1
salad: 2
You would have 0.41666666666666696 amount of currency remaining from your budget

### Test Case 2

The algorithm has determined that you should buy the amounts of the following drinks: 
cider: 0
juice: 0
tomato juice: 0
The algorithm has determined that you should buy the amounts of the following foods: 
pizza: 1
lasagna: 4
bread: 1
penne: 4
You would have 0.03921568627450989 amount of currency remaining from your budget

### Test Case 3

The algorithm has determined that you should buy the amounts of the following drinks: 
cider: 0
juice: 0
tomato juice: 0
The algorithm has determined that you should buy the amounts of the following foods: 
pizza: 0
lasagna: 0
bread: 0
penne: 0
You would have 0.0 amount of currency remaining from your budget