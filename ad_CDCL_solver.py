import filereading
import preoptimizer

cnf_file = filereading.read_file("C:/Users/arnav/Desktop/cnf.cnf")

details = filereading.get_base_details(cnf_file)
vars = details[1]

clauses = filereading.get_clauses(cnf_file)

print("Found clauses: ", clauses)
print()

preoptimized_clauses = preoptimizer.pre_optimizer(clauses, vars)
print("Pre-optimized clauses: ", preoptimized_clauses)
print()

preoptimizer.initial_contradiction_check(preoptimized_clauses)