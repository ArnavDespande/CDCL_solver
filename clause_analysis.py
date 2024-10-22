def get_pure_literals(unresolved_clauses, vars):

    pure_literals = []

    for i in range(1, vars+1):

        found_positive_flag = False
        found_negative_flag = False

        for clause in unresolved_clauses:
            if (i in clause):
                found_positive_flag = True
            if (i*-1 in clause):
                found_negative_flag = True
            if (found_negative_flag and found_positive_flag):
                break

        if (found_positive_flag and not found_negative_flag):
            pure_literals.append(i)
        elif (found_negative_flag and not found_positive_flag):
            pure_literals.append(-i)

    return pure_literals