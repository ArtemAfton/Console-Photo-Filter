from PIL import Image


def red_filter(image):
    # Получение размеров изображения
    width, height = image.size
    # Создание нового изображения с тем же размером
    new_image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            new_image.putpixel((x, y), (r, 0, 0))
    return new_image


def green_filter(image):
    # Получение размеров изображения
    width, height = image.size
    # Создание нового изображения с тем же размером
    new_image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            new_image.putpixel((x, y), (0, g, 0))
    return new_image


def blue_filter(image):
    # Получение размеров изображения
    width, height = image.size
    # Создание нового изображения с тем же размером
    new_image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            new_image.putpixel((x, y), (0, 0, b))
    return new_image


def inversion_filter(image):
    # Получение размеров изображения
    width, height = image.size
    # Создание нового изображения с тем же размером
    new_image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            new_image.putpixel((x, y), (255 - r, 255 - g, 255 - b))
    return new_image


filters = ("Красный фильтр", "Зелёный фильтр", "Синий фильтр", "Инверсия")

# Приветствие
print("Добро пожаловать в консольный фоторедактор.")

# Запрос  пути к файлу
file_path = input("Введите путь к файлу: ")

# Открытие файла и конвертация в формат RGB
image = Image.open(file_path).convert("RGB")

failed = False
while not False:
    print("Меню фотофильтров: ")
    for ell in range(len(filters)):
        print(ell + 1, "-", filters[ell])
    choice = input("Выберите фотофильтр (или 0 для выхода): ")
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "0":
        print("Вы что-то не то вводите, введите цифру выбранного вами фильтра (или 0 для выхода).")
        print("Меню фотофильтров: ")
        for ell in range(len(filters)):
            print(ell + 1, "-", filters[ell])
        choice = input()
    if choice == "1":
        print(f"Вы выбрали Красный фотофильтр (оставляет только красные оттенки изображения).")
        print("Применить фильтр? (Да/Нет)")
        decision = input()
        while decision != "да" and decision != "нет":
            print("Вы что-то не то вводите, введите Да или Нет.")
            decision = input()
        if decision.lower() == "да":
            new_image = red_filter(image)
        elif decision.lower() == "нет":
            continue
    elif choice == "2":
        print("Вы выбрали Зелёный фотофильтр (оставляет только зелёные оттенки изображения).")
        print("Применить фильтр? (Да/Нет)")
        decision = input()
        while decision != "да" and decision != "нет":
            print("Вы что-то не то вводите, введите Да или Нет.")
            decision = input()
        if decision.lower() == "да":
            new_image = green_filter(image)
        elif decision.lower() == "нет":
            continue
    elif choice == "3":
        print("Вы выбрали Синий фотофильтр (оставляет только синие оттенки изображения).")
        print("Применить фильтр? (Да/Нет)")
        decision = input()
        while decision != "да" and decision != "нет":
            print("Вы что-то не то вводите, введите Да или Нет.")
            decision = input()
        if decision.lower() == "да":
            new_image = blue_filter(image)
        elif decision.lower() == "нет":
            continue
    elif choice == "4":
        print("Вы выбрали фильтр Инверсия (инвертирует все оттенки изображения).")
        print("Применить фильтр? (Да/Нет)")
        decision = input()
        while decision != "да" and decision != "нет":
            print("Вы что-то не то вводите, введите Да или Нет.")
            decision = input()
        if decision.lower() == "да":
            new_image = inversion_filter(image)
        elif decision.lower() == "нет":
            continue
    elif choice == "0":
        print("До свидания!")
        break
    else:
        print("Вы что-то не то вводите, введите номер выбранного вами фильтра.")
        continue
    # Предложение пользователю сохранить новое изображение
    print("Хотите сохранить картинку? (Да/Нет)")
    decision2 = input()
    while decision2 != "да" and decision2 != "нет":
        print("Вы что-то не то вводите, введите Да или Нет.")
        decision2 = input()
    if decision2.lower() == "да":
        save_path = input("Куда сохранить: ")
        new_image.save(save_path)
    elif decision2.lower() == "нет":
        continue
    # Предложение пользователю ещё раз использовать фоторедактор
    print("Ещё раз? (Да/Нет)")
    answer = input()
    while answer != "да" and answer != "нет":
        print("Вы что-то не то вводите, введите Да или Нет.")
        answer = input()
    if answer.lower() == "да":
        continue
    elif answer.lower() == "нет":
        print("До свидания!")
        break



















