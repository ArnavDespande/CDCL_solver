import random


def commonality_searcher(clauses, values):

    number_frequency = [[0, 0] for _ in range(values)] #[Negative][Positive]

    for clause in clauses:
        for var in clause:
            if (var < 0):
                number_frequency[-var-1][1] += 1
            else:
                number_frequency[var-1][0] += 1

    return number_frequency


def most_common_value(clauses, vars):

    max_value = 0
    is_negative = False

    values = commonality_searcher(clauses, vars)

    for value_pair in values:
        for value in value_pair:
            if (value > max_value):
                is_negative = False
                max_value = values.index(value_pair)+1
                if (value_pair.index(value) == 0):
                    is_negative = True
    if (is_negative):
        max_value *= -1

    return max_value

'''
def random_value(clauses, vars):

    values = commonality_searcher(clauses, vars)

    value_pair = random.choice(values)
    value = random.choice(value_pair)
    if (value != 0):
        return -(values.index(value_pair)+1) if (value_pair.index(value) == 0) else (values.index(value_pair)+1)
    else:
        return random_value(values, vars)
'''