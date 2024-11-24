def read_file(path): #Self explanatory

    cnf_file = open(path, "r")
    return cnf_file;


def get_base_details(lines): #This is way too badly formatted for a vital function lol

    for line in lines:
        if line.startswith("p"):
            cleaning = line.split()
            #Cleaning[2] = Number of variables
            #Cleaning[3] = Number of clauses
            return int(cleaning[2]), int(cleaning[3])


def get_clauses(lines): #Get all clauses [this is a list of list of ints]

    clauses = []

    for line in lines:
        if line.strip().endswith(" 0") and not line.strip().startswith("c"):
            cleaning = line.split()
            cleaning = [int(item) for item in cleaning]
            clauses.append(cleaning[:-1])

    return clauses
