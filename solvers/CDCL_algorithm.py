import copy
from custom_types.Trail import *
from utilities.CDCL_heuristics import *


# Each node contains details of the previous decision
def solver(clause_map, vars, node=None, passover=None, ids=None):

    if (ids == None):
        ids = []
    literal_selected = random_value(clause_map, vars)
    if (passover is not None):
        print("Found passover from previous decision at", passover)
        literal_selected = passover
    Id = ((int(node.id) if node is not None else 2) * literal_selected)
    if (Id in ids):
        print("You've been here before")
        return False
    else:
        ids.append(Id)

    print("Decided on:", literal_selected)
    new_node = TrailNode(literal_selected, "DECISION", copy.deepcopy(clause_map), copy.deepcopy(node))
    clause_map1 = solver_till_decision(copy.deepcopy(clause_map), literal_selected)

    if (clause_map1 != False and clause_map1 != True):
        clause_map1.print_table()
        return solver(copy.deepcopy(clause_map1), vars, copy.deepcopy(new_node), None, ids)

    elif (clause_map1):
        return True

    else:
        if (passover is None):
            print("Contradiction found, switching polarity")
            return solver(copy.deepcopy(clause_map), vars, copy.deepcopy(node), -(new_node.value), ids)
        else:
            print("Contradiction found, going up tree")
            if (node is not None):
                print("Upper decision being used:", -(node.value))
                return solver(copy.deepcopy(node.map_snapshot), vars, node.predecessor, -(node.value), ids)
            else:
                print("Can't go any higher")
                return False


def solver_till_decision(clauses, literal):

    remainder = use_assigned_literal(copy.deepcopy(clauses), literal)
    return recursive_non_eliminating_contradiction_optimizer(copy.deepcopy(remainder))

# Returns the clauses and the representative node
def recursive_non_eliminating_contradiction_optimizer(clauses):
    
    singulars = singular_clause_detector(clauses)

    if (len(singulars) > 0):
        if (find_false_contradiction(clauses)):
            return False
        if (find_full_truths(clauses)):
            return True
        clauses = use_assigned_literal(copy.deepcopy(clauses), singulars[0][1])
        print(singulars[0][1], ":Singular")
        print()
        return recursive_non_eliminating_contradiction_optimizer(clauses)
    else:
        for clause in clauses.clauses:
            if (clause.get_clause_value() == None):
                return clauses
            elif (not clause.get_clause_value()):
                clause.print_clause()
                print()
                return False
            else:
                continue
        return True


def use_assigned_literal(clauses, literal):

    clauses_copy = clauses

    for clause in clauses_copy.clauses:
        for variable in clause.variables:
            if (abs(variable.tag) == abs(literal) and not variable.assigned_status):
                variable.assigned_status = True
                if (variable.tag > 0 and literal > 0 or variable.tag < 0 and literal < 0):
                    variable.value = True
                else:
                    variable.value = False

    return clauses_copy


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


def find_full_truths(clauses):

    for clause in clauses.clauses:
        if clause.get_clause_value() == False:
            return False
        elif clause.get_clause_value() == None:
            return False
    return True