import preoptimizer


def solver(clauses, vars):
    pass


def solver_till_decision(clauses, literal):

    remainder = use_assigned_literal(clauses, literal)
    return preoptimizer.recursive_contradiction_optimizer(remainder)


def use_assigned_literal(clauses, literal):

    clauses_made_true = []

    for clause in clauses:
        if (literal in clause):
            clauses_made_true.append(clause)
        elif (-literal in clause):
            clause.remove(-literal)

    clauses = [i for i in clauses if i not in clauses_made_true]
    print("Clauses left:", clauses)
    print()
    return clauses