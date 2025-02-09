import turtle


def koch_snowflake(t, order, size):
    """
    Малює одну сторону сніжинки Коха
    t: об'єкт turtle
    order: рівень рекурсії
    size: довжина відрізка
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def draw_snowflake(order, size=300):
    """
    Малює повну сніжинку Коха
    order: рівень рекурсії
    size: розмір сніжинки
    """
    # Налаштування вікна відображення результату
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Сніжинка Коха")

    # Налаштування turtle
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість
    t.color("white")
    t.penup()

    # Початкова позиція
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Малюємо три сторони сніжинки
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    # Ховаємо turtle після завершення
    t.hideturtle()
    window.mainloop()


def main():
    while True:
        try:
            order = int(input("Введіть рівень рекурсії (0-6): "))
            if 0 <= order <= 6:
                break
            else:
                print("Будь ласка, введіть число від 0 до 6")
        except ValueError:
            print("Будь ласка, введіть ціле число")

    draw_snowflake(order)


if __name__ == "__main__":
    main()
