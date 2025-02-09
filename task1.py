import os
import shutil
import argparse
from pathlib import Path


def create_parser():
    """Створення парсера аргументів командного рядка"""
    parser = argparse.ArgumentParser(
        description="Рекурсивне копіювання та сортування файлів"
    )
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument(
        "--dest",
        default="dist",
        help="Шлях до директорії призначення (за замовчуванням: dist)",
    )
    return parser


def create_directory(path):
    """Створення директорії, якщо вона не існує"""
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        print(f"Помилка при створенні директорії {path}: {e}")
        return False
    return True


def copy_file(source, dest):
    """Копіювання файлу з обробкою помилок"""
    try:
        shutil.copy2(source, dest)
        print(f"Скопійовано: {source} -> {dest}")
        return True
    except (shutil.Error, OSError) as e:
        print(f"Помилка при копіюванні {source}: {e}")
        return False


def process_directory(source_path, dest_path):
    """Рекурсивна обробка директорії"""
    try:
        # Перебір всіх елементів у директорії
        for item in os.scandir(source_path):
            if item.is_dir():
                # Рекурсивний виклик для піддиректорій
                process_directory(item.path, dest_path)
            elif item.is_file():
                # Отримання розширення файлу
                file_extension = Path(item.name).suffix.lower()
                if not file_extension:
                    file_extension = ".no_extension"

                # Створення піддиректорії для цього типу файлів
                extension_dir = os.path.join(
                    dest_path,
                    (
                        file_extension[1:]
                        if file_extension != ".no_extension"
                        else "no_extension"
                    ),
                )
                if create_directory(extension_dir):
                    # Копіювання файлу
                    dest_file = os.path.join(extension_dir, item.name)
                    copy_file(item.path, dest_file)

    except OSError as e:
        print(f"Помилка при доступі до директорії {source_path}: {e}")


def main():
    # Парсинг аргументів командного рядка
    parser = create_parser()
    args = parser.parse_args()

    # Перевірка існування вихідної директорії
    if not os.path.exists(args.source):
        print(f"Помилка: Вихідна директорія '{args.source}' не існує")
        return

    # Створення директорії призначення
    if not create_directory(args.dest):
        return

    # Запуск рекурсивної обробки
    print(f"Початок копіювання з {args.source} в {args.dest}")
    process_directory(args.source, args.dest)
    print("Копіювання завершено")


if __name__ == "__main__":
    main()
