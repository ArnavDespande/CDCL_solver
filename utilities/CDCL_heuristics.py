import random


def commonality_searcher(clauses, values):

    number_frequency = [[0, 0] for _ in range(values)] #[Negative][Positive]

    for clause in clauses:
        for var in clause:
            if (var.tag < 0):
                number_frequency[-var-1][1] += 1
            else:
                number_frequency[var-1][0] += 1

    return number_frequency


def most_common_value(clauses, vars):

    max_value = 1
    is_negative = False

    values = commonality_searcher(clauses, vars)

    for value_pair in values:
        for value in value_pair:
            if (value >= max_value):
                is_negative = False
                max_value = values.index(value_pair)+1
                if (value_pair.index(value) == 0):
                    is_negative = True
    if (is_negative):
        max_value *= -1

    return max_value


def random_value(clauses, vars):

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


'''Use this function to check if you can further iterate; it returns a zero if you can't
def iterative_value(clauses, vars, previous_value=None):

    if (previous_value == None):
        return 1

    if abs(previous_value)+1 > vars:
        return 0

    for clause in clauses:
        if (abs(previous_value)+1) in clause:
            return abs(previous_value)+1
        elif -(abs(previous_value)+1) in clause:
            return -(abs(previous_value)+1)

    return iterative_value(clauses, vars, abs(previous_value)+1)'''