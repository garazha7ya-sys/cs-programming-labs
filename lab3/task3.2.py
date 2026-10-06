s = input()

parts = s.split()

surname = parts[0].capitalize()
name_initial = parts[1][0].upper() + "."
patronymic_initial = parts[2][0].upper() + "."

print(surname, name_initial, patronymic_initial)