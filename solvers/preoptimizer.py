from utilities.clause_analysis import * 


def recursive_blockage_remover(clauses):

    blockages = get_blocked_clauses(clauses)

    if (blockages != None):
        clauses.remove(blockages[0])
        return recursive_blockage_remover(clauses)
    return clauses


def recursive_contradiction_optimizer(clauses):

    singulars = get_singular_clauses(clauses)

    if (len(singulars) > 0):
        if (locate_contradiction(clauses) != False):
            return "UNSATISFIABLE"
        clauses = singularity_eliminator(clauses, int(singulars[0][0]))
        return recursive_contradiction_optimizer(clauses)
    else:
        if (clauses == []):
            return "SATISFIABLE"
        return clauses


def pre_optimizer(clauses, vars):
    
    clauses = singularity_compressor(clauses)
    clauses = tautological_eliminator(clauses)
    clauses = pure_literal_eliminator(clauses, vars)

    return clauses


def singularity_eliminator(clauses, singular):

    removables = []

    for clause in clauses:
        if (singular in clause):
            removables.append(clause)
        if (-singular in clause):
            clause.remove(-singular)

    clauses = [i for i in clauses if i not in removables]

    return clauses


def pure_literal_eliminator(clauses, vars):

    pure_clauses = []

    pures = get_pure_literals(clauses, vars)

    for pure in pures:
        for clause in clauses:
            if pure in clause:
                pure_clauses.append(clause)

    clauses = [i for i in clauses if i not in pure_clauses]

    return clauses


def tautological_eliminator(clauses):

    tautologies = get_tautological_clauses(clauses)
    clauses = [i for i in clauses if i not in tautologies]
    
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