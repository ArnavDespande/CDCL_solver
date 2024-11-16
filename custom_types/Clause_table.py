class Value: 
    def __init__ (self, tag, value=None, assigned_status=False):
        self.tag = tag #Tag is a number
        self.value = value #Value is a boolean-value
        self.assigned_status = assigned_status #Also a boolean, but for a different reason

class Clause:
    def __init__ (self, vars):
        self.variables = vars #A clause is a list of variables (of type Value)

    def get_clause_value(self): #Check if this clause has been made satisfiable
        unassigned_located = False
        for variable in self.variables:
            if (variable.assigned_status):
                if (variable.value):
                    return True
            else:
                unassigned_located = True
        if (unassigned_located):
            return None
        return False

    def print_clause(self):
        for var in self.variables:
            print(var.tag, " ", var.value, " ", end="")
        print()

class Clause_Table:
    def __init__ (self):
        self.clauses = []

    def add_clause(self, clause): #Add a clause to this table
        self.clauses.append(clause)

    def print_table(self):
        for clause in self.clauses:
            for var in clause.variables:
                print(var.tag , " ", var.value, " ", end="")
            print()

def setup_table(clauses): #Initialize a giant table of clauses, default values = None, all unassigned
    setup = Clause_Table()

    for clause in clauses:
        valued_clause = []
        for var in clause:
            value = Value(var)
            valued_clause.append(value)
        adding_clause = Clause(valued_clause)
        setup.add_clause(adding_clause)

    return setup