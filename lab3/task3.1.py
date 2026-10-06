doc_code = input("Введите код документа (AAA-NNNN-NNNN): ")

if len(doc_code) == 13 and doc_code[3] == '-' and doc_code[8] == '-':
    category = doc_code[0:3]
    year = doc_code[4:8]
    number = doc_code[9:13]
    reversed_number = number[::-1]

    print(f"Категория: {category}")
    print(f"Год: {year}")
    print(f"Номер: {number}")
    print(f"Обратный номер: {reversed_number}")
else:
    print("Ошибка: неверный формат кода документа.")
    print("Категория: 000")
    print("Год: 0000")
    print("Номер: 0000")
    print("Обратный номер: 0000")