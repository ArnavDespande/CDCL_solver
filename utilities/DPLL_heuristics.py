import random


def commonality_searcher(clauses, values): #Get the number of positive and negative instances, values is the max number of variables

    number_frequency = [[0, 0] for _ in range(values)] #[Negative][Positive] (((is this accurate???)))

    for clause in clauses:
        for var in clause:
            if (var.tag < 0):
                number_frequency[-var-1][1] += 1 #If we find a "-5", set value [4][1] += 1
            else:
                number_frequency[var-1][0] += 1 #If we find a "5", set value [4][0] += 1

    return number_frequency #Returns a bunch of tuples


def most_common_value(clauses, vars): #This function calls commonality_searcher() within itself.

    max_value = 1
    is_negative = False

    values = commonality_searcher(clauses, vars)

    for value_pair in values: #For tuple in list of tuples
        for value in value_pair: #For count in tuple
            if (value >= max_value): #If this count is greater than current
                is_negative = False #Set a flag to false (as a default)
                max_value = values.index(value_pair)+1 #Update maximal value to be this new value
                if (value_pair.index(value) == 0): #If this maximal value was found at the [0]th index of the tuple
                    is_negative = True #It was a negative value
    if (is_negative):
        max_value *= -1 #Make sure that the negative value is noted as final result

    return max_value


def random_value(clauses, vars): #Returns a random value which exists in the current set of clauses, regardless of + or -

    value_pair = random.randint(1, vars)
    value = random.choice([-1, 1])
    if (value == -1):
        output = -value_pair
    else:
        output = value_pair
    for clause in clauses.clauses:
        for val in clause.variables:
            if abs(output) == abs(val.tag):
                return output
    return random_value(clauses, vars)


#Use this function to check if you can further iterate; it returns a zero if you can't
def next_value(clauses, vars, previous_value=None): #This returns the highest value in the clause table

    if (previous_value == None):
        return 1

    for clause in clauses.clauses:
        for value in clause.variables:
            if (abs(previous_value)+1) == abs(value.tag):
                return abs(previous_value)+1

    return next_value(clauses, vars, abs(previous_value)+1)