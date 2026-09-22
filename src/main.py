
def print_hi(name):
    information = []
    clauses = [[]]

    with open("ExempleFiles/uf20-01.cnf", mode="r+") as file:
        for line in file:
            if line.startswith("c"):
                pass
            elif line.startswith("p"):
                information = line.split()
            elif not line.startswith("%"):
                clauses += line.split("0\n")

    formatted_information = information
    formatted_information[2] = int(formatted_information[2])
    formatted_information[3] = int(formatted_information[3])

    formatted_clauses = clauses[1::2]
    formatted_clauses = [[int(x) for x in s.split()] for s in formatted_clauses]
    formatted_clauses.pop(len(formatted_clauses) - 1)
    formatted_clauses.pop(len(formatted_clauses) - 1)

    print(f"Number of variables: {formatted_information[2]}")
    print(f"Number of Clauses: {formatted_information[3]}")
    print(formatted_information)
    print(formatted_clauses)

if __name__ == '__main__':
    print_hi('PyCharm')
