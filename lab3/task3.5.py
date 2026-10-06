text = input()

length = len(text)
only_letters = text.isalpha()
only_digits = text.isdigit()
alphanumeric = text.isalnum()
has_dash = '-' in text

print(f"Длина: {length}")
print(f"Только буквы: {only_letters}")
print(f"Только цифры: {only_digits}")
print(f"Буквенно-цифровая: {alphanumeric}")
print(f"Содержит дефис: {has_dash}")