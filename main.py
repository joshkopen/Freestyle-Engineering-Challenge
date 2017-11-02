import settings
import operator


def file_reader(file_name):
    '''Reads a file line by line, separating at the colon
    and assigning the value of price to the drink in a
    dictionary. Returns that dictionary'''
    return_dic = {}
    with open(file_name, 'r') as file:
        for line in file:
            return_dic[line.split(':')[0]] = float(line.split(':')[1])
    return return_dic


def dic_editor(dic, add_prefs):
    '''Takes a single line and updates
    the dictionary by adding 1 to its previous value
    or giving it a value of 1 if it doesn't exist.
    Returns that dictionary'''
    for each in add_prefs.split(','):
        stripped = each.strip()
        if stripped in dic:
            dic[stripped] += 1
        else:
            dic[stripped] = 1
    return dic


def preference_reader(file_name):
    '''Reads person.txt and returns two dictionaries
    of drink and food preferences respectively'''
    with open(file_name, 'r') as file:
        prefs = file.readlines()

    counter = 0
    drink_dic = {}
    food_dic = {}

    while counter < len(prefs):
        drink_prefs = prefs[counter+1]
        drink_dic = dic_editor(drink_dic, drink_prefs)
        food_prefs = prefs[counter+2]
        food_dic = dic_editor(food_dic, food_prefs)
        counter += 3

    return drink_dic, food_dic

def assign_percentage(prefs):
    '''Figures out based on preferences what percentage
    of the total preferences an item is'''
    total = 0
    percent_dic = {}

    for each in prefs:
        total += prefs[each]
    for each in prefs:
        percent_dic[each] = prefs[each] / total
    return percent_dic

def buy_items(budget, prefs, costs):
    '''Buys items based on the preferences and costs.
    Returns the amount of items bought, the remaining budget,
    and the percentage of preferences calculated'''
    remaining = 0
    percentages = assign_percentage(prefs)
    print(percentages)
    amounts = {}

    for item in costs:
        if item in percentages:
            to_spend = percentages[item] * budget
            amount = to_spend / costs[item]
            amounts[item] = int(amount)
            remaining += amount - amounts[item]
        else:
            percentages[item] = 0
            amounts[item] = 0
    return amounts, remaining, percentages

def buy_remaining(budget, percentages, costs, drink_amounts, fodd_amounts):
    '''Uses the remaining budget to buy as much as possible of the most
    popular items and tries to maximize the amount of budget used.
    Returns the new amounts for drinks, food, and the amount of budget
    that was not possible to be spent'''
    sorted_percentages = sorted(percentages.items(), key=operator.itemgetter(1))
    sorted_percentages = sorted_percentages[::-1]
    for item in sorted_percentages:
        while costs[item[0]] < budget:
            budget -= costs[item[0]]
            if item[0] in drink_amounts:
                drink_amounts[item[0]] += 1
            else:
                food_amounts[item[0]] += 1
    return drink_amounts, food_amounts, budget


drink_costs = file_reader("drinks.txt")
food_costs = file_reader("food.txt")
drink_prefs, food_prefs = preference_reader("people.txt")

drink_amounts, d_remaining, drink_percentages = buy_items(settings.budget * (1 - settings.food_ratio), 
    drink_prefs, drink_costs)
food_amounts, f_remaining, food_percentages = buy_items(settings.budget * settings.food_ratio, 
    food_prefs, food_costs)
remaining = d_remaining + f_remaining

print(drink_amounts)
print(food_amounts)
print(remaining)

percentages = dict(list(drink_percentages.items()) + list(food_percentages.items()))
costs = dict(list(drink_costs.items()) + list(food_costs.items()))
print(percentages)
print(costs)

drink_amounts, food_amounts, remaining = buy_remaining(remaining, percentages,
    costs, drink_amounts, food_amounts)


print("The algorithm has determined that you should buy the amounts of the following drinks: ")
for drink in drink_amounts:
    print("{0}: {1}".format(drink, drink_amounts[drink]))
print("The algorithm has determined that you should buy the amounts of the following foods: ")
for food in food_amounts:
    print("{0}: {1}".format(food, food_amounts[food]))
print("You would have {} amount of currency remaining from your budget".format(remaining))


