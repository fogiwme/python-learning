# Выполним упражнение 9.11

from admin import Admin, Privileges

victor_krylov = Admin('Виктор', "Крылов", 30, "Пушкино")
victor_krylov.print_privileges()
victor_krylov.privileges.show_privileges()