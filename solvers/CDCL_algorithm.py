def solver(clauses, vars):
    pass


def solver_till_decision(clauses, literal):

    remainder = use_assigned_literal(clauses, literal)
    return recursive_non_eliminating_contradiction_optimizer(remainder)

def recursive_non_eliminating_contradiction_optimizer(clauses):
    
    singulars = singular_clause_detector(clauses)

    if (len(singulars) > 0):
        if (find_false_contradiction(clauses)):
            return False
        clauses = use_assigned_literal(clauses, singulars[0][1])
        print(singulars[0][1], ":Singular")
        clauses.print_table()
        print()
        return recursive_non_eliminating_contradiction_optimizer(clauses)
    else:
        for clause in clauses.clauses:
            if (clause.get_clause_value() == None):
                return clauses
            elif (not clause.get_clause_value()):
                clause.print_clause()
                return False
            else:
                continue
        return True

def use_assigned_literal(clauses, literal):

    for clause in clauses.clauses:
        for variable in clause.variables:
            if abs(variable.tag) == abs(literal):
                variable.assigned_status = True
                if (variable.tag > 0 and literal > 0 or variable.tag < 0 and literal < 0):
                    variable.value = True
                else:
                    variable.value = False

    return clauses

def singular_clause_detector(clauses):

    singular_clauses = []

    for clause in clauses.clauses:

        first_non_assigned = False
        found_variable = 0
        second_non_assigned = False

        for variable in clause.variables:
            if first_non_assigned and not variable.assigned_status:
                second_non_assigned = True
            if not variable.assigned_status:
                first_non_assigned = True
                found_variable = variable.tag
        
        if (first_non_assigned and not second_non_assigned):
            singular_clauses.append((clause, found_variable))

    # Returns a list of tuples, first tuple is a clause, second tuple is a single value of type Value
    return singular_clauses

def find_false_contradiction(clauses):

    for clause in clauses.clauses:
        if clause.get_clause_value() == False:
            clause.print_clause()
            return True
    return False