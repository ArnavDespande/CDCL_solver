import filereading

cnf_file = filereading.read_file("C:/Users/arnav/Desktop/prop_rnd_6136_v_6_c_25_vic_1_4.cnf")

details = filereading.get_clauses(cnf_file)
for detail in details:
    print(detail)