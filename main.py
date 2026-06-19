from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Nom", "Âge", "Ville"]
table.add_row(["Alice", 25, "Paris"])
table.add_row(["Bob", 30, "Lyon"])
table.add_row(["Charlie", 35, "Marseille"])
table.add_row(["bob", 963,"67ha"])
print(table)
