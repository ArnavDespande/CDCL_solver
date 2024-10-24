from utilities.file_reading import *
from solvers.preoptimizer import *
from solvers.CDCL_algorithm import *
from custom_types.Clause_table import *


cnf_file = read_file("C:/Users/arnav/Desktop/cnf.cnf")

details = get_base_details(cnf_file)
vars = details[0]

clauses = get_clauses(cnf_file)
print("Found clauses:", clauses)
print()

preoptimized_clauses = pre_optimizer(clauses, vars)
pre_CDCL_clauses = recursive_contradiction_optimizer(preoptimized_clauses)

print("Optimized clauses: ", pre_CDCL_clauses)
print()

if (pre_CDCL_clauses != "UNSATISFIABLE"):

    table_map = setup_table(pre_CDCL_clauses)
    final = solver(table_map, vars, None, None)
    if (final):
        print("SATISFIABLE")
    else:
        print("UNSATISFIABLE")
    print()