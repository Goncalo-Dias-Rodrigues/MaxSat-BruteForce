from file_manager import FileManager
from maxsat import MaxSat
import time

# | Elemento   | Convenção          | Exemplo             |
# | ---------- | ------------------ | ------------------- |
# | Variáveis  | `snake_case`       | `user_name`         |
# | Funções    | `snake_case`       | `calculate_total()` |
# | Classes    | `PascalCase`       | `UserAccount`       |
# | Constantes | `UPPER_SNAKE_CASE` | `MAX_CONNECTIONS`   |
# | Métodos    | `snake_case`       | `get_user()`        |
# | Módulos    | `snake_case`       | `user_service.py`   |
# | Pacotes    | `lowercase`        | `utils`             |

if __name__ == '__main__':

    start = time.perf_counter()
    file_manager = FileManager()

    information, clauses = file_manager.get_info("files/20variables/uf20-01.cnf")

    max_sat = MaxSat(information, clauses)

    best_result, best_hypotheses = max_sat.evaluate()

    end = time.perf_counter()

    time = end - start
    print(f"Tempo de execução: {time:.6f} segundos")
    print(f"Best Result: {best_result}")
    print(f"Best Hypothesis: {best_hypotheses}")

    print(f"Number of variables: {information[2]}")
    print(f"Number of Clauses: {information[3]}")
    # print(information)
    # print(clauses)

