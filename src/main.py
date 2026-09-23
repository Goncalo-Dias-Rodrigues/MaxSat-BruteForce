from file_manager import FileManager
from maxsat import MaxSat

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
    file_manager = FileManager()

    information, clauses = file_manager.get_info("files/uf20-03.cnf")

    max_sat = MaxSat(information, clauses)
    max_sat.calculate_clauses()




    print(f"Number of variables: {information[2]}")
    print(f"Number of Clauses: {information[3]}")
    print(information)
    print(clauses)

