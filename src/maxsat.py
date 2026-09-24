import random


class MaxSat:
    """
        Solves the maxsat problem with brute-force
    """

    def __init__(self, info, clauses):
        """
            Stores the information and clauses in the class;
            Creates an array space for the variables;
            Creates a String to store the current solution hypothesis(starting with all zeros);
            Fills the variable array with the correspondent boolean values.
        :param info: Information from the header of the file
        :param clauses: Every clause from the formula with the respective index and polarity of each variable
        """
        self.information = info
        self.clauses = clauses
        self.variables = []
        self.current_binary_hypotheses = ""
        self.current_binary_hypotheses = "0" * self.information[2]
        self.fill_variables_with_hypotheses_values()

    def fill_variables_with_hypotheses_values(self):
        """
        Fills the variable array with the values from the current hypothesis (0 -> False, 1 -> True).
        """
        for i in range(self.information[2]):
            hypotheses_value = self.current_binary_hypotheses[i]
            if hypotheses_value == "0":
                self.variables.append(False)
            else:
                self.variables.append(True)

    def binary_plus_one(self, binary):
        """
        Calculates the next hypothesis by adding 1 value to the binary String.
        :param binary: Current hypothesis
        :return: Next hypothesis based on the last one
        """
        number = int(binary, 2)
        number += 1
        return format(number, f'0{len(binary)}b')

    def evaluate(self):
        """
        Evaluates all the results and hypotheses
        :return: Best number of clauses that form a True and all the best hypotheses that achieve that number
        """
        results, hypothesis = self.calculate_hypotheses()
        best_result = -1
        best_hypotheses = []
        for index in range(len(results)):
            current_result = results[index].count(True)
            if current_result > best_result:
                best_result = current_result
                if not current_result == self.information[3]:
                    best_hypotheses.append(hypothesis[index])
                else:
                    best_hypotheses.clear()
            if current_result == self.information[3]:
                best_hypotheses.append(hypothesis[index])
        return best_result, best_hypotheses

    def calculate_hypotheses(self):
        """
        Tests all the hypothesis for all variables;
        Calls for results of all clauses for the specific variable boolean values from the current hypothesis.
        :return: the results and the respective hypothesis
        """
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
        """
        Calculates the result boolean value of all clauses.
        :return: An array of boolean values resulting of all the given clauses
        """
        results = []
        for clause in self.clauses:
            results.append(self.calculate_result(clause))
        return results

    def calculate_result(self, clause):
        """
        Calculates the result of a specific clause; While doing this it applies the inversion operator with indexes
        that are negative in the clause; Knowing that inside the clause are only "or" operators we only need to
        know that at least 1 True exists.
        :param clause: Clause that will be analysed
        :return: True if at least 1 True exists, false otherwise
        """
        boolean_value = []
        for value in clause:
            if value - 1 >= 0:
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
