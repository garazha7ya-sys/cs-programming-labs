def is_valid_command(command):
    return command in ("0", "1", "2", "exit")


def can_burn(power, fuel):
    return fuel >= power


def simulate_step(height, speed, fuel, power, gravity, thrust_step):
    fuel = fuel - power
    speed = speed + gravity - thrust_step * power
    if speed < 0:
        speed = 0
    height = height - speed
    if height < 0:
        height = 0
    return height, speed, fuel


def get_status(height, speed, safe_speed=2):
    if height > 0:
        return "В полете"
    if speed <= safe_speed:
        return "Посадка успешна"
    return "Авария"


def format_state(height, speed, fuel):
    return f"Высота: {height} | Скорость: {speed} | Топливо: {fuel}"


def main():
    # Вариант 4
    height = 28
    speed = 4
    fuel = 10
    gravity = 3
    thrust_step = 3

    print(format_state(height, speed, fuel))

    while True:
        command = input()
        if not is_valid_command(command):
            print("Ошибка команды")
            continue
        if command == "exit":
            print("Полет прерван")
            break
        power = int(command)
        if not can_burn(power, fuel):
            print("Недостаточно топлива")
            continue
        height, speed, fuel = simulate_step(
            height, speed, fuel, power, gravity, thrust_step
        )
        print(format_state(height, speed, fuel))
        status = get_status(height, speed)
        if status != "В полете":
            print(status)
            break


if __name__ == "__main__":
    main()