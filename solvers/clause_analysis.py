def get_blocked_clauses(unresolved_clauses): #Returns a tuple pair of blocked clauses; largest first

    # https://users.aalto.fi/~tjunttil/2021-DP-AUT/notes-sat/preprocessing.html#blocked-clause-elimination

    not_blocked = False

    for clause in unresolved_clauses:
        for secondary_clause in unresolved_clauses:

            for value in clause:
                if -value in secondary_clause:
                    for contra_value in secondary_clause:
                        if -contra_value in clause:

                            for other_clause in unresolved_clauses:
                                if unresolved_clauses.index(other_clause) != unresolved_clauses.index(clause) and unresolved_clauses.index(other_clause) != unresolved_clauses.index(secondary_clause):
                                    if value in other_clause:
                                        not_blocked = True
                                    if -value in other_clause:
                                        if not (contra_value in other_clause):
                                            not_blocked = True

                            if not not_blocked:
                                return (clause, secondary_clause)

    return None

def get_pure_literals(unresolved_clauses, vars): #Returns a list of pure literals to eliminate

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


def get_tautological_clauses(unresolved_clauses): #Returns a list of tautological clauses to eliminate

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


def get_singular_clauses(unresolved_clauses): #Returns a list of singular clauses to eliminate

    singulars = []

    for clause in unresolved_clauses:
        if (len(clause) == 1):
            singulars.append(clause)

    return singulars


def locate_contradiction(unresolved_clauses): #See if we have a contradiction

    singulars = get_singular_clauses(unresolved_clauses)

    for singular in singulars:
        if ([-int(singular[0])] in singulars): #If a negative version of a singular is in our list of singulars, return the value
            return (True, singular)
    return False #All good :)