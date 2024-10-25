def read_file(path):

    cnf_file = open(path, "r")

    return cnf_file;


def get_base_details(lines):

    for line in lines:
        if line.startswith("p"):
            cleaning = line.split()
            # Cleaning[2] = Number of variables
            # Cleaning[3] = Number of clauses
            return int(cleaning[2]), int(cleaning[3])


def get_clauses(lines):

    clauses = []

    for line in lines:
        if line.strip().endswith("0"):
            cleaning = line.split()
            cleaning = [int(item) for item in cleaning]
            clauses.append(cleaning[:-1])

    return clauses