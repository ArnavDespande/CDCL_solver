import copy
from custom_types.Trail import *
from utilities.CDCL_heuristics import *


# Each node contains details of the previous decision
def solver(clause_map, vars, node=None, passover=None):

    if (passover is not None):
        #print("Found passover:", passover)
        literal_selected = passover
    else:
        if node is None:
            literal_selected = iterative_value(clause_map, vars, None)
        else:
            literal_selected = iterative_value(clause_map, vars, node.value)
        #print("Decided on:", literal_selected)


    new_node = TrailNode(literal_selected, "DECISION", copy.deepcopy(clause_map), node, False)
    if (node != None):
        if new_node.value > 0:
            node.son = new_node
        else:
            node.daughter = new_node

    clause_map1 = solver_till_decision(copy.deepcopy(clause_map), literal_selected)


    if (clause_map1 != False and clause_map1 != True):
        return solver(copy.deepcopy(clause_map1), vars, new_node, None)
    elif (clause_map1):
        return True
    else:
        new_node.dead = True

        if (passover is None):
            #print("Contradiction found, switching polarity")
            new_node.dead = True
            return solver(copy.deepcopy(clause_map), vars, node, -(new_node.value))
        else:
            # Screw it
            return False
            '''
            print("Contradiction found, need to backtrack")
            node_to_use = backtrack_to_appropriate_node(node)
            if (node_to_use is not None):
                print("Upper decision being used:", -(node_to_use.value))
                return solver(copy.deepcopy(node_to_use.map_snapshot), vars, node_to_use.predecessor, -(node_to_use.value))
            else:
                print("Can't go any higher")
                return False'''


def backtrack_to_appropriate_node(node):
    if (node is None):
        return None

    if (node.dead):
        return backtrack_to_appropriate_node(node.predecessor)

    if (node.daughter != None):
        if (node.son.dead and node.daughter.dead):
            if (node.value < 0):
                node.dead = True
                return (backtrack_to_appropriate_node(node.predecessor))
            return (node)
    '''else:
        return ("debug needed")'''


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
        '''print(singulars[0][1], ":Singular")
        print()'''
        clauses_copy = copy.deepcopy(clauses)
        remove_true_clauses(clauses_copy)
        return recursive_non_eliminating_contradiction_optimizer(clauses_copy)
    else:
        for clause in clauses.clauses:
            if (clause.get_clause_value() == None):
                return clauses
            elif (not clause.get_clause_value()):
                # clause.print_clause()
                print()
                return False
            else:
                continue
        return True


def use_assigned_literal(clauses, literal):

    for clause in clauses.clauses:
        for variable in clause.variables:
            if (abs(variable.tag) == abs(literal) and not variable.assigned_status):
                variable.assigned_status = True
                if (variable.tag > 0 and literal > 0 or variable.tag < 0 and literal < 0):
                    variable.value = True
                else:
                    variable.value = False

    clauses_unfinished = remove_true_clauses(copy.deepcopy(clauses))

    return clauses_unfinished


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
            return True
    return False


def find_full_truths(clauses):

    for clause in clauses.clauses:
        if clause.get_clause_value() == False:
            return False
        elif clause.get_clause_value() == None:
            return False
    return True


def get_path_trace(node):

    trace = []

    while(node is not None):
        trace.insert(0, (node.value, node.dead))
        node = node.predecessor
    print(trace)
    return trace


def remove_true_clauses(clauses_main):

    true_clauses = []
    for clause in clauses_main.clauses:
        if (clause.get_clause_value() == True):
            true_clauses.append(clause)
    for clause in true_clauses:
        clauses_main.clauses.remove(clause)
    return clauses_main