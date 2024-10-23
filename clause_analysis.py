def get_pure_literals(unresolved_clauses, vars):

    pure_literals = []

    for i in range(1, vars+1):

        found_positive_flag = False
        found_negative_flag = False

        for clause in unresolved_clauses:
            if (i in clause):
                found_positive_flag = True
            if (-i in clause):
                found_negative_flag = True
            if (found_negative_flag and found_positive_flag):
                break

        if (found_positive_flag and not found_negative_flag):
            pure_literals.append(i)
        elif (found_negative_flag and not found_positive_flag):
            pure_literals.append(-i)

    return pure_literals


def get_tautological_clauses(unresolved_clauses):

    tautologies = []

    for clause in unresolved_clauses:
        tautology_found = False
        for variable in clause:
            if (-variable in clause):
                tautology_found = True
                break
        if (tautology_found):
            tautologies.append(clause)

    return tautologies


def get_Horn_clauses(unresolved_clauses):

    Horn_clauses = []

    for clause in unresolved_clauses:
        first_positive = False
        second_positive = False

        for variable in clause:
            if (variable > 0):
                if (first_positive):
                    second_positive = True
                first_positive = True
            if (first_positive and second_positive):
                break

        if (not second_positive):
            Horn_clauses.append(clause)

    return Horn_clauses


def get_singular_clauses(unresolved_clauses):

    singulars = []

    for clause in unresolved_clauses:
        if (len(clause) == 1):
            singulars.append(clause)

    return singulars


def locate_contradiction(unresolved_clauses):

    singulars = get_singular_clauses(unresolved_clauses)
    print("Comparing singulars:", singulars)

    for singular in singulars:
        if ([-int(singular[0])] in singulars):
            print("Contradicting singular:", singular)
            print()
            return (True, singular)
    return False