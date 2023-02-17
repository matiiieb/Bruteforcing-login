import random

def generate_combination():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random_numbers = []

    for i in range(6):
        random_index = random.randint(0, len(numbers) - 1)
        selected_number = numbers[random_index]
        random_numbers.append(selected_number)
        numbers.pop(random_index)

        if i > 0 and abs(selected_number - random_numbers[i - 1]) == 1:
            numbers.append(selected_number)
            random_numbers.pop()
            random_index = random.randint(0, len(numbers) - 1)
            selected_number = numbers[random_index]
            random_numbers.append(selected_number)
            numbers.pop(random_index)

    return random_numbers

combinations = []

random.seed()  # Inicializa una semilla aleatoria

# Genera todas las combinaciones posibles
for i in range(30240):  # 30240 es el número total de combinaciones posibles
    combinations.append(generate_combination())

# Guarda las combinaciones en un archivo de texto
with open("combinaciones.txt", "w") as f:
    for combination in combinations:
        f.write(str(combination) + "\n")
