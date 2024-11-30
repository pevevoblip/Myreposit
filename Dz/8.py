import logging

logging.basicConfig(
    filename='error_log.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error("Ділення на нуль: %s", e)
        print("Помилка: ділення на нуль неможливе.")
    except Exception as e:
        logging.error("Сталася несподівана помилка: %s", e)
        print("Сталася несподівана помилка.")

divide_numbers(10, 0)
divide_numbers(10, "a")