# GPU purchase optimizer
A short script to calculate gpu optimal gpu to purchase for cost and performance over gpu lifetime.

At this point, if you want to calculate which GPU you should buy to optimize performance for it's lifetime:
1. Check the CSV has correct data for cheapest prices. You'll have to input these manually for now.
2. Edit the relative computing power depreciation constant if you want. It measures how much theoretically relative GPU power decreases each month as GPU's get more powerful. The default value should be more or less accurate maybe I don't know, I kinda guessed power goes up ~17% a year.
3. Change the relative computing power limit to the performance metric of what you think is the least powerful GPU you'd be happy to have RIGHT NOW. It's best to check which GPU in the csv file has the least performance you'd be happy with right now and then edit the r variable to that value.
4. Run the script, it outputs a list of GPU's sorted by their performance over lifetime for money.
