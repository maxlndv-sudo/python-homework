from pathlib import Path

def find_duplicate_files(directory_path: str, suffix: str = ".txt") -> dict:
    """
    Рекурсивно сканирует каталог, находит все файлы с заданным суффиксом
    и группирует их по имени для выявления дубликатов.
    
    :param directory_path: Путь к исходной папке для сканирования.
    :param suffix: Расширение файлов (например, '.txt').
    :return: Словарь, где ключ - имя файла, а значение - список полных путей к нему.
    """
    # Превращаем строку пути в умный объект Path
    base_dir = Path(directory_path)
    
    # Защитная проверка: если папки не существует или это файл, выходим
    if not base_dir.exists() or not base_dir.is_dir(): #Программа не начнет сканирование, если пользователь опечатался в названии папки.
        print(f"[Ошибка]: Путь {directory_path} не существует или не является папкой.")
        return {}

    # Создаем пустой словарь (картотеку). 
    # Структура будет такой: { 'song.mp3': [Путь1, Путь2, Путь3] }
    files_by_name = {}

    # Используем rglob() для глубокого (рекурсивного) поиска по всем подпапкам.
    # Конструкция f"*{suffix}" превратится, например, в "*.txt" (искать всё, что кончается на .txt)
    for child in base_dir.rglob(f"*{suffix}"):
        
        # Нам нужны только файлы (пропускаем папки, если они вдруг так названы)
        if child.is_file():
            
            # Извлекаем чистое имя файла с помощью свойства .name (например, 'text.txt')
            file_name = child.name
            
            # Если мы видим такое имя файла ВПЕРВЫЕ, создаем для него пустой список в словаре
            if file_name not in files_by_name:
                files_by_name[file_name] = []
                
            # С помощью .resolve() получаем полный (абсолютный) путь к файлу
            absolute_path = child.resolve()
            
            # Добавляем этот путь в список к текущему имени файла
            files_by_name[file_name].append(absolute_path)
            
    return files_by_name


def print_duplicates(all_files: dict):
    """Красиво выводит в консоль только те файлы, у которых есть дубликаты."""
    has_duplicates = False
    
    print("\n=== РЕЗУЛЬТАТЫ ПОИСКА ДУБЛИКАТОВ ===")
    
    # Перебираем имена файлов и списки их путей в нашей картотеке
    for name, paths in all_files.items():
        
        # Если путей больше 1 — значит, перед нами дубликат!
        if len(paths) > 1:
            has_duplicates = True
            print(f"\nНайден дубликат песни: '{name}' (Встречается {len(paths)} раз)")
            
            # Выводим каждый полный путь с новой строки
            for path in paths:
                print(f"  -> Полный путь: {path}")
                
    if not has_duplicates:
        print("Отлично! Дубликаты файлов с таким расширением не найдены.")


# =====================================================================
# АВТОМАТИЧЕСКИЙ ТЕСТ (Эта часть создаст папки на диске для проверки)
# =====================================================================
if __name__ == "__main__":
    # 1. Задаем имя тестовой папки
    test_folder = Path("./music_collection")
    
    print("1. Подготовка тестовой среды...")
    # Создаем структуру папок: music_collection/, а внутри неё папки rock/ и pop/
    (test_folder / "rock").mkdir(parents=True, exist_ok=True)
    (test_folder / "pop").mkdir(parents=True, exist_ok=True)
    
    # Создаем фейковые txt-файлы (некоторые имена специально повторяются в разных папках)
    # Файл 'yesterday.txt' будет лежать и в корне, и в папке 'pop' - это дубликат.
    (test_folder / "yesterday.txt").touch()
    (test_folder / "pop" / "yesterday.txt").touch() 
    
    # Файл 'bohemian_rhapsody.txt' будет лежать в rock/ и в pop/ - это тоже дубликат.
    (test_folder / "rock" / "bohemian_rhapsody.txt").touch()
    (test_folder / "pop" / "bohemian_rhapsody.txt").touch()
    
    # Уникальный файл (дубликатов не будет)
    (test_folder / "rock" / "stairway_to_heaven.txt").touch()
    
    print("2. Тестовые файлы и папки успешно созданы на диске.")
    print("3. Запуск сканирования функции из Упражнения 14.2...")
    
    # Ищем дубликаты MP3 файлов в созданной тестовой папке
    scan_results = find_duplicate_files(directory_path="./music_collection", suffix=".txt")
    
    # Выводим результат на экран
    print_duplicates(scan_results)
