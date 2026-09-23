import random


class MaxSat:
    def __init__(self, info, clauses):
        self.information = info
        self.clauses = clauses

        self.variables = []
        self.fill_variables()

    def fill_variables(self):
        for i in range(self.information[2]):
            random_value = random.randint(0,1)
            if random_value == 0:
                self.variables.append(False)
            else:
                self.variables.append(True)

    def calculate_clauses(self):
        results = []
        for clause in self.clauses:
            results.append(self.calculate_result(clause))
        print(results)
        print(results.count(True))

    def calculate_result(self, clause):
        boolean_value = []
        for value in clause:
            if value-1 >= 0:
                boolean_value.append(self.variables[value-1])
            else:
                boolean_value.append(not self.variables[abs(value) - 1])
        return boolean_value.__contains__(True)
