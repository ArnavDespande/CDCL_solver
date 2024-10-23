import clause_analysis
import CDCL_heuristics
import preoptimizer
import file_reading


def solver(clauses, vars):

    while (clauses != "SATISFIABLE" and clauses != "UNSATISFIABLE"):
        value_to_use = CDCL_heuristics.most_common_value(clauses, vars)
        print("Greedy value:", value_to_use)
        print()
        clauses = use_assigned_literal(clauses, value_to_use)
        print("After using value:", clauses)
        print()
        clauses = solver_till_decision(clauses, value_to_use)
    return clauses


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
    return clauses