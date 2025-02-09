def print_state(towers, state_type=""):
    """Виводить поточний стан веж"""
    if state_type:
        print(f"{state_type}:")
    print(f"{'Поточний стан:':<15} {towers}")


def move_disk(towers, source, target, disk_num):
    """Переміщує диск між стрижнями"""
    disk = towers[source].pop()
    towers[target].append(disk)
    print(f"Перемістити диск з {source} на {target}: {disk}")
    print_state(towers)


def hanoi(n, towers, source="A", auxiliary="B", target="C"):
    """Рекурсивно розв'язує головоломку Ханойських веж"""
    if n == 1:
        move_disk(towers, source, target, 1)
        return

    hanoi(n - 1, towers, source, target, auxiliary)
    move_disk(towers, source, target, n)
    hanoi(n - 1, towers, auxiliary, source, target)


def main():
    # Отримуємо кількість дисків від користувача
    try:
        n = int(input("Введіть кількість дисків: "))
        if n < 1:
            raise ValueError("Кількість дисків має бути додатним числом")
    except ValueError as e:
        print(f"Помилка: {e}")
        return

    # Ініціалізуємо стрижні
    towers = {
        "A": list(range(n, 0, -1)),  # Заповнюємо перший стрижень дисками
        "B": [],  # Допоміжний стрижень
        "C": [],  # Цільовий стрижень
    }

    print_state(towers, "Початковий стан")

    # Розв'язуємо головоломку
    hanoi(n, towers)

    print(f"{'Кінцевий стан:':<15} {towers}")


if __name__ == "__main__":
    main()
