import random


class MaxSat:
    def __init__(self, info, clauses):
        self.information = info
        self.clauses = clauses
        self.variables = []
        self.current_binary_hypotheses = ""
        self.current_binary_hypotheses = "0" * self.information[2]
        self.fill_variables_with_hypotheses_values()

    def fill_variables_with_hypotheses_values(self):
        for i in range(self.information[2]):
            hypotheses_value = self.current_binary_hypotheses[i]
            if hypotheses_value == "0":
                self.variables.append(False)
            else:
                self.variables.append(True)

    def binary_plus_one(self, binario):
        numero = int(binario, 2)
        numero += 1
        return format(numero, f'0{len(binario)}b')

    def calculate_hypotheses(self):
        results = []
        hypotheses = []
        for i in range(pow(2, self.information[2])):
            hypotheses.append(self.current_binary_hypotheses)
            self.fill_variables_with_hypotheses_values()
            results.append(self.calculate_clauses())
            self.current_binary_hypotheses = self.binary_plus_one(self.current_binary_hypotheses)
            self.variables.clear()
        return results, hypotheses

    def calculate_clauses(self):
        results = []
        for clause in self.clauses:
            results.append(self.calculate_result(clause))
        return results


    def calculate_result(self, clause):
        boolean_value = []
        for value in clause:
            if value-1 >= 0:
                boolean_value.append(self.variables[value-1])
            else:
                boolean_value.append(not self.variables[abs(value) - 1])
        return boolean_value.__contains__(True)

    def fill_variables_with_random_values(self):
        for i in range(self.information[2]):
            random_value = random.randint(0,1)
            if random_value == 0:
                self.variables.append(False)
            else:
                self.variables.append(True)