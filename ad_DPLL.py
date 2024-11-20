from utilities.file_reading import *
from solvers.preoptimizer import *
from solvers.DPLL_algorithm import *
from custom_types.Clause_table import *
'''
cnf_file = read_file(path)

details = get_base_details(cnf_file)
vars = details[0]

clauses = get_clauses(cnf_file)

preoptimized_clauses = pre_optimizer(clauses, vars)
pre_DPLL_clauses = recursive_contradiction_optimizer(preoptimized_clauses)

if (pre_DPLL_clauses != "UNSATISFIABLE" and pre_DPLL_clauses != "SATISFIABLE"):

    table_map = setup_table(pre_DPLL_clauses)
    final = solver(table_map, 1)
    if (final):
        print("SATISFIABLE")
    else:
        print("UNSATISFIABLE")
'''
import sys

def main():
    lines = sys.stdin.readlines()
    vars = get_base_details(lines)[0]
    clauses = get_clauses(lines)
    preoptimized_clauses = pre_optimizer(clauses, vars)
    pre_blocked_clauses = recursive_contradiction_optimizer(preoptimized_clauses)
    pre_DPLL_clauses = recursive_blockage_remover(pre_blocked_clauses)

    if (pre_DPLL_clauses != "UNSATISFIABLE" and pre_DPLL_clauses != "SATISFIABLE"):
        table_map = setup_table(pre_DPLL_clauses)
        final = solver(table_map, 1)
        if (final):
            print("SATISFIABLE")
        else:
            print("UNSATISFIABLE")
    else:
        print(pre_DPLL_clauses)

if (__name__ == "__main__"):
    main()