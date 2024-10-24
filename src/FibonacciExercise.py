# Calcula la secuencia fibonacci, guarda los numeros en una lista y la regresa
def calculate_fibonacci() -> list[int]:
    fibonacci_numbers_list: list[int] = []
    fibonacci_number: int = 0
    x: int = 1

    for i in range(13):
        fibonacci_numbers_list.append(fibonacci_number)
        y = x
        x = fibonacci_number + x
        fibonacci_number = y

    return fibonacci_numbers_list


if __name__ == "__main__":
    print(calculate_fibonacci())

