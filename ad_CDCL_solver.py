import filereading
import clause_analysis

cnf_file = filereading.read_file("C:/Users/arnav/Desktop/prop_rnd_6136_v_6_c_25_vic_1_4.cnf")

details = filereading.get_base_details(cnf_file)
print(details)
clauses = filereading.get_clauses(cnf_file)
print(clauses)
pure_literals = clause_analysis.get_pure_literals(clauses, details[1])
print(pure_literals)