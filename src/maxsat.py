
class MaxSat:
    """
        Solves the maxsat problem with brute-force
    """

    def __init__(self, info, clauses):
        """
        Initializes the MaxSat instance with the problem information and clauses;
        Creates the variables array with all variables initialized to False.
        :param info: Information from the header of the file
        :param clauses: Every clause from the formula with the respective index and polarity of each variable
        """
        self.information = info
        self.clauses = clauses
        self.variables = [False] * self.information[2]

    def next_hypothesis(self):
        """
        Calculates the next hypothesis by adding 1 to the variables array, like a binary counter;
        Changes the array in place, so nothing needs to be rebuilt.
        The first variable is the most significant one, so the order is the same as the binary String.
        """
        index = len(self.variables) - 1
        while index >= 0 and self.variables[index]:
            self.variables[index] = False
            index -= 1
        if index >= 0:
            self.variables[index] = True

    def current_hypothesis_to_string(self):
        """
        Converts the current values of the variables to a binary String (False -> 0, True -> 1).
        Only used when a hypothesis is good enough to be stored.
        :return: Current hypothesis as a String
        """
        hypothesis = ""
        for value in self.variables:
            if value:
                hypothesis += "1"
            else:
                hypothesis += "0"
        return hypothesis

    def evaluate(self):
        """
        Evaluates all possible hypotheses and stores the ones that satisfy the maximum number of clauses;
        Stops keeping previous hypotheses when a better result is found.
        :return: Best number of clauses that form a True and all the best hypotheses that achieve that number
        """
        best_result = -1
        best_hypotheses = []
        for _ in range(1 << self.information[2]):
            current_result = self.calculate_clauses(best_result)
            if current_result == self.information[3]:
                if not best_result == self.information[3]:
                    best_hypotheses.clear()
                best_result = current_result
                best_hypotheses.append(self.current_hypothesis_to_string())
            elif current_result >= best_result:
                if not current_result == best_result:
                    best_hypotheses.clear()
                best_result = current_result
                best_hypotheses.append(self.current_hypothesis_to_string())
            self.next_hypothesis()
        return best_result, best_hypotheses

    def calculate_clauses(self, best_result):
        """
        Counts how many clauses are True for the current hypothesis;
        Stops as soon as the false clauses make it impossible to reach the best result so far.
        :param best_result: Best number of True clauses found until now
        :return: Number of True clauses, or -1 if this hypothesis cannot reach best_result
        """
        allowed_failures = self.information[3] - best_result
        failures = 0
        for clause in self.clauses:
            if not self.calculate_result(clause):
                failures += 1
                if failures > allowed_failures:
                    return -1
        return self.information[3] - failures

    def calculate_result(self, clause):
        """
        Calculates the result of a specific clause by evaluating each variable according to its polarity;
        Since all variables inside a clause are connected by "or" operators, the clause is True as soon as at least one
        literal evaluates to True.
        :param clause: Clause that will be analysed
        :return: True if at least 1 True exists, false otherwise
        """
        for value in clause:
            if value - 1 >= 0:
                if self.variables[value-1]:
                    return True
            else:
                if not self.variables[abs(value) - 1]:
                    return True
        return False
