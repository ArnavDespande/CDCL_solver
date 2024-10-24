class Value:
    def __init__ (self, tag, value=None, assigned_status=False):
        self.tag = tag
        self.value = value
        self.assigned_status = assigned_status

class Clause:
    def __init__ (self, vars):
        self.variables = vars

    def get_clause_value(self):
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
    def __init__ (self, clauses):
        self.clauses = []

    def add_clause(self, clause):
        self.clauses.append(clause)

    def print_table(self):
        for clause in self.clauses:
            for var in clause.variables:
                print(var.tag , " ", var.value, " ", end="")
            print()

def setup_table(clauses):
    setup = Clause_Table([])

    for clause in clauses:
        valued_clause = []
        for var in clause:
            value = Value(var)
            valued_clause.append(value)
        adding_clause = Clause(valued_clause)
        setup.add_clause(adding_clause)

    return setup