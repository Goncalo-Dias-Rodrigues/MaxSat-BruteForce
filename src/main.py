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

    inicio = time.perf_counter()
    file_manager = FileManager()

    information, clauses = file_manager.get_info("files/uf20-02.cnf")

    max_sat = MaxSat(information, clauses)

    results, hypothesis = max_sat.calculate_hypotheses()


    best_result = 0
    best_hypothesis = ""
    for index in range(len(results)):
        current_result = results[index].count(True)
        if current_result > best_result:
            best_result = current_result
            best_hypothesis = hypothesis[index]

    fim = time.perf_counter()

    tempo = fim - inicio
    print(f"Tempo de execução: {tempo:.6f} segundos")
    print(f"Best Result: {best_result}")
    print(f"Best Hypothesis: {best_hypothesis}")

    print(f"Number of variables: {information[2]}")
    print(f"Number of Clauses: {information[3]}")
    # print(information)
    # print(clauses)

