# 1. Сначала берем шаблон из Упражнения 14.1
def replace_lines(pattern: str, replacement: str, input_file: str, output_file: str):
    try:  #защита от сбоев
        with open(input_file, 'r', encoding='utf-8') as f_in: # Чтение файла в память
            content = f_in.read()  # считывает абсолютно весь текст из файла и сохраняет его в переменную 
 
 #Замена слов в тексте       
        modified_content = content.replace(pattern, replacement)
        
        with open(output_file, 'w', encoding='utf-8') as f_out:  # как только Python прочитает файл, он сразу же закроет его
            f_out.write(modified_content)
        print(f"[УСПЕХ] Файл успешно обработан и сохранен в '{output_file}'")
    except IOError as ex:
        print(f"[ОШИБКА] Не удалось обработать файл: {ex}")

# 2. ЗАПУСК ТЕСТА
if __name__ == '__main__': # запуск программы
    # Тестовый текст проверки регистров и окончаний
    test_data = (       # записываем текст в переменную
        "Привет, верблюд!\n"
        "Вчера я видел, как один верблюд шёл по пустыне. \n"
        "Этот верблюд был очень пушистым.\n"
        "В конце строки тоже стоит верблюд\n\n"
        "Интересно, заменит ли программа слово верблюд, если оно написано с большой буквы: Верблюд?\n"
        "Или если оно слилось со знаком препинания: верблюда?\n"
    )
    
    # Автоматически создаем входной файл на диске
    with open('input.txt', 'w', encoding='utf-8') as f: # Создание файла input.txt на компьютере
        f.write(test_data)
        
    print("--- Исходный файл 'input.txt' успешно создан ---")
  
# Программа сама создает на твоем компьютере реальный текстовый файл input.txt
# и записывает туда наш проверочный текст
# не нужно создавать его вручную через Блокнот

    # Вызываем функцию: меняем "верблюд" на "робот"
    replace_lines(
        pattern="верблюд", 
        replacement="робот", 
        input_file="input.txt", 
        output_file="output.txt"
    )
    
    # Читаем и показываем результат работы программы
    print("\n--- Содержимое созданного файла 'output.txt': ---")
    try:
        with open('output.txt', 'r', encoding='utf-8') as f: # Проверка результата
            print(f.read())
    except FileNotFoundError:
        print("[ОШИБКА] Файл output.txt не был создан!")
