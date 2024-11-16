import copy #Fuck this thing's reason for existing
from utilities.DPLL_heuristics import *


def solver(clauses, value):

    if (solver_till_decision(copy.deepcopy(clauses), value) == False): # If solving this path leads us to false
        return False    # And consequently destroy this tree if so
    elif (solver_till_decision(copy.deepcopy(clauses), value) == True):
        return True
    else: # Sisyphus
        new_value = abs(value)+1
        return solver(solver_till_decision(copy.deepcopy(clauses), value), new_value) or solver(solver_till_decision(copy.deepcopy(clauses), value), -new_value)
        

def solver_till_decision(clauses, literal): #The thing that does stuff inbetween decisions

    remainder = use_assigned_literal(copy.deepcopy(clauses), literal)
    return recursive_non_eliminating_contradiction_optimizer(copy.deepcopy(remainder))


# Returns the clauses left over, False if we have a contradiction, True if we have TRUTH
def recursive_non_eliminating_contradiction_optimizer(clauses):
    
    singulars = singular_clause_detector(clauses)

    if (len(singulars) > 0):
        if (find_false_contradiction(clauses)):
            return False
        if (find_full_truths(clauses)):
            return True
        clauses = use_assigned_literal(copy.deepcopy(clauses), singulars[0][1])
        clauses_copy = copy.deepcopy(clauses)
        remove_true_clauses(clauses_copy)
        return recursive_non_eliminating_contradiction_optimizer(clauses_copy)
    else:
        for clause in clauses.clauses:
            if (clause.get_clause_value() == None):
                return clauses
            elif (not clause.get_clause_value()):
                return False
            else:
                continue
        return True


def use_assigned_literal(clauses, literal): #Take a literal, apply unit propogation on the clauses

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

    # Returns a list of tuples, first index of tuple is a clause, second is a single value of type Value
    return singular_clauses


def find_false_contradiction(clauses): #Returns true if we find a contradiction in here

    for clause in clauses.clauses:
        if clause.get_clause_value() == False:
            return True
    return False


def find_full_truths(clauses): #Did we win, Mr. Stark?

    for clause in clauses.clauses:
        if clause.get_clause_value() == False:
            return False
        elif clause.get_clause_value() == None:
            return False
    return True


def get_path_trace(node): #Begone

    trace = []

    while(node is not None):
        trace.insert(0, (node.value, node.dead))
        node = node.predecessor
    print(trace)
    return trace


def remove_true_clauses(clauses_main): #Eliminate anything true.

    true_clauses = []
    for clause in clauses_main.clauses:
        if (clause.get_clause_value() == True):
            true_clauses.append(clause)
    for clause in true_clauses:
        clauses_main.clauses.remove(clause)
    return clauses_main