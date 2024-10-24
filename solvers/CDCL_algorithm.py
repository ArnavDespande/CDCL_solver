import copy
from custom_types.Trail import TrailNode
from utilities.CDCL_heuristics import *

# Each node contains details of the previous decision
def solver(original_map, clause_map, vars, previous_values, node=None):

    if len(previous_values) > 0:
        literal_selected = previous_values[0]
        previous_values.remove(literal_selected)
    else:
        literal_selected = random_value(clause_map, vars)

    new_node = TrailNode(literal_selected, "DECISION", clause_map, node)
    clause_map = solver_till_decision(clause_map, literal_selected)

    if (clause_map != False and clause_map != True):
        print(clause_map.print_table())
        print()
        return solver(original_map, clause_map, vars, previous_values, new_node)

    elif (clause_map):
        return True

    else:
        final_node = new_node
        full_stack = []
        while(final_node is not None):
            full_stack.insert(0, final_node.value)
            final_node = final_node.predecessor
        print(full_stack)
        full_stack[-1] *= -1
        return False


def solver_till_decision(clauses, literal):

    remainder = use_assigned_literal(clauses, literal)
    return recursive_non_eliminating_contradiction_optimizer(remainder)

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
        clauses.print_table()
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