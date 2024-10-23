import file_reading
import preoptimizer
import CDCL_algorithm


cnf_file = file_reading.read_file("C:/Users/arnav/Desktop/cnf.cnf")

details = file_reading.get_base_details(cnf_file)
vars = details[0]

clauses = file_reading.get_clauses(cnf_file)
print("Found clauses:", clauses)
print()

preoptimized_clauses = preoptimizer.pre_optimizer(clauses, vars)
pre_CDCL_clauses = preoptimizer.recursive_contradiction_optimizer(preoptimized_clauses)

print("Optimized clauses: ", pre_CDCL_clauses)
print()

if (pre_CDCL_clauses != 'UNSATISFIABLE' and pre_CDCL_clauses != 'SATISFIABLE'):
    robotic_result = CDCL_algorithm.solver(pre_CDCL_clauses, vars)
    print("Result:", robotic_result)