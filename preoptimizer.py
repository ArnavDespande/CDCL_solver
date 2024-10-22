import clause_analysis

def full_optimizer(clauses, vars):
    
    clauses = tautological_eliminator(clauses)
    clauses = pure_literal_eliminator(clauses, vars)

    return clauses

def pure_literal_eliminator(clauses, vars):

    pures = clause_analysis.get_pure_literals(clauses, vars)
    print(pures)
    print()

    for pure in pures:
        for clause in clauses:
            if pure in clause:
                clauses.remove(clause)

    return clauses

def tautological_eliminator(clauses):

    tautologies = clause_analysis.get_tautological_clauses(clauses)
    clauses = [i for i in clauses if i not in tautologies]
    print(clauses)
    print()
    
    return clauses