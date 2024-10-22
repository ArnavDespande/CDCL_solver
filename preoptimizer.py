import clause_analysis

def recursive_contradiction_optimizer(clauses):

    singulars = clause_analysis.get_singular_clauses(clauses)
    print("Singulars found:", singulars)
    print()

    if (len(singulars) > 0):
        if (contradiction_check(clauses, singulars) == "UNSATISFIABLE"):
            return "UNSATISFIABLE"
        clauses = singularity_eliminator(clauses, int(singulars[0][0]))
        return recursive_contradiction_optimizer(clauses)
    else:
        return clauses

def pre_optimizer(clauses, vars):
    
    clauses = singularity_compressor(clauses)
    clauses = tautological_eliminator(clauses)
    clauses = pure_literal_eliminator(clauses, vars)

    return clauses

def singularity_eliminator(clauses, singular):

    removables = []
    removable_singlevalues = []

    for clause in clauses:
        if (singular in clause):
            removables.append(clause)
        if (-singular in clause):
            clause.remove(-singular)

    clauses = [i for i in clauses if i not in removables]
    print("With singularity literals addressed:", clauses)
    print()

    return clauses

def contradiction_check(clauses, singulars):

    singulars = [int(item[0]) for item in singulars]

    for singular in singulars:
        if (-singular in singulars):
            return "UNSATISFIABLE"

    return "UNKNOWN"

def pure_literal_eliminator(clauses, vars):

    pure_clauses = []

    pures = clause_analysis.get_pure_literals(clauses, vars)
    print("Pure literals: ", pures)
    print()

    for pure in pures:
        for clause in clauses:
            if pure in clause:
                pure_clauses.append(clause)

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

def singularity_compressor(clauses):

    clauses1 = []

    for clause in clauses:
        subclause = []
        for literal in clause:
            if (not (literal in subclause)):
                subclause.append(literal)
        clauses1.append(subclause)

    return clauses1