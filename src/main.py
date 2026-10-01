from file_manager import FileManager
from maxsat import MaxSat
import time

if __name__ == '__main__':

    start = time.perf_counter()
    file_manager = FileManager()

    # information, clauses = file_manager.get_info("files/20variables/uf20-01.cnf")
    information, clauses = file_manager.get_info("files/hoos.cnf")
    end = time.perf_counter()

    file_time = end - start

    start = time.perf_counter()
    max_sat = MaxSat(information, clauses)

    best_result, best_hypotheses = max_sat.evaluate()

    end = time.perf_counter()

    time = end - start
    print(f"File reading execution time: {file_time:.6f} segundos")
    print(f"Algorithm execution time: {time:.6f} segundos")
    print(f"Number of variables: {information[2]}")
    print(f"Number of Clauses: {information[3]}")
    print(f"Best Result: {best_result}")
    print(f"Number of solutions: {len(best_hypotheses)}")
    print(f"Best Hypothesis: {best_hypotheses}")


    # print(information)
    # print(clauses)

