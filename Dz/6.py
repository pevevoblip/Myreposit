def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Вміст файлу:")
            print(content)
    except FileNotFoundError:
        print(f"Файл за шляхом '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

if __name__ == "__main__":
    file_path = input("Введіть шлях до файлу: ")
    read_file(file_path)
