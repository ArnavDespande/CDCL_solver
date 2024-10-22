import clause_analysis

def initial_contradiction_check(clauses):

    singulars = clause_analysis.get_singular_clauses(clauses)
    print("Singular clauses found:", singulars)
    print()
    singulars = [int(item[0]) for item in singulars]

    for singular in singulars:
        if (-singular in singulars):
            print("UNSATISFIABLE")
            return "UNSATISFIABLE"

    print("UNKNOWN")
    return "UNKNOWN"

def pre_optimizer(clauses, vars):
    
    clauses = tautological_eliminator(clauses)
    clauses = pure_literal_eliminator(clauses, vars)

    return clauses

def pure_literal_eliminator(clauses, vars):

    pure_clauses = []

    pures = clause_analysis.get_pure_literals(clauses, vars)
    print("Pure literals: ", pures)
    print()

    for pure in pures:
        for clause in clauses:
            if pure in clause:
                pure_clauses.append(clause)
                break

    clauses = [i for i in clauses if i not in pure_clauses]
    return clauses

def tautological_eliminator(clauses):

    tautologies = clause_analysis.get_tautological_clauses(clauses)
    print("Tautologies found: ", tautologies)
    print()
    clauses = [i for i in clauses if i not in tautologies]
    print("With tautologies removed: ", clauses)
    print()
    
    return clauses