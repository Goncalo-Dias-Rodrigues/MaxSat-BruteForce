
def print_hi(name):
    information = []
    clauses = [[]]

    with open("ExempleFiles/uf20-01.cnf", mode="r+") as file:
        for line in file:
            if line.startswith("c"):
                pass
            elif line.startswith("p"):
                information = line.split()
                print(f"Number of variables: {information[2]}")
                print(f"Number of Clauses: {information[3]}")
            elif not line.startswith("%"):
                clauses += line.split("0\n")
    # clauses.remove("")
    print(information[1])
    print(clauses[0])
    print(clauses[1])
    print(clauses[2])
    print(clauses[3])

    formated_clauses = [len(clauses)]

    for i in range(len(clauses)):
        if not i % 2 == 0:
            formated_clauses += clauses[i]

    for index in range(len(clauses)):
        if not index % 2 == 0:
            print(clauses)




if __name__ == '__main__':
    print_hi('PyCharm')
