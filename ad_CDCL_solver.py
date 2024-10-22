import filereading
import preoptimizer

cnf_file = filereading.read_file("C:/Users/arnav/Desktop/cnf.cnf")

details = filereading.get_base_details(cnf_file)
vars = details[1]

clauses = filereading.get_clauses(cnf_file)

print(clauses)
print()

preoptimized_clauses = preoptimizer.full_optimizer(clauses, vars)
print(preoptimized_clauses)