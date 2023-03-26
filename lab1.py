"""@package docstring
"""

import random
import pandas as pd
from time import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(1000000)

class Car:
    """Класс Машина, в котором хранятся имя владельца, модель, год выпуска, государственный номер и цвет
    """
    def __init__(self, raw): #конструктор
        """конструктор"""
        self.name = raw[0]
        self.model = raw[1]
        self.year = raw[2]
        self.number = raw[3]
        self.color = raw[4]
        
    def __eq__(self, other): #x = y
        """перегрузка оператора равенства"""
        if self.number == other.number:
            if self.year == other.year:
                if self.model == other.model:
                    if self.color == other.color:
                        if self.name == other.name:
                            return True
        return False
    
    def __ne__(self, other): #x != y
        """перегрузка оператора неравенства"""
        if self == other:
            return False
        else:
            return True
        
    def __lt__(self, other): #x < y
        """перегрузка оператора меньше"""
        if self.number < other.number:
            return True
        elif self.number == other.number:
            if self.year < other.year:
                return True
            elif self.year == other.year:
                if self.model < other.model:
                    return True
                elif self.model == other.model:
                    if self.color < other.color:
                        return True
                    elif self.color == other.color:
                        if self.name < other.name:
                            return True
        return False
    
    def __gt__(self, other): #x > y
        """перегрузка оператора больше"""
        if self.number > other.number:
            return True
        elif self.number == other.number:
            if self.year > other.year:
                return True
            elif self.year == other.year:
                if self.model > other.model:
                    return True
                elif self.model == other.model:
                    if self.color > other.color:
                        return True
                    elif self.color == other.color:
                        if self.name > other.name:
                            return True
        return False
    
    def __le__(self, other): #x <= y
        """перегрузка оператора меньше или равно"""
        if (self < other) or (self == other):
            return True
        else:
            return False
        
    def __ge__(self, other): #x >= y
        """перегрузка оператора больше или равно"""
        if (self > other) or (self == other):
            return True
        else:
            return False

##сортировка выбором
def choice_sort(lst_f):
    """сортировка выбором"""
    lst = lst_f
    for i in range(len(lst) - 1):
        min_pos = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_pos]:
                min_pos = j
        lst[i], lst[min_pos] = lst[min_pos], lst[i]
    return lst

##вспомогательная функция сортировки слиянием
def merge_two(lst_f, lst_s):
    """вспомогательная функция сортировки слиянием
    """
    lst1 = lst_f
    lst2 = lst_s
    res = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    if i < len(lst1):
        res += lst1[i:]
    if j < len(lst2):
        res += lst2[j:]
    return res

##сортировка слиянием
def merge_sort(lst_f):
    """сортировка слиянием
    """
    lst = lst_f
    if len(lst) == 1:
        return lst
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge_two(left, right)

##быстрая сортировка
def quick_sort(lst_f):
    """быстрая сортировка
    """
    lst = lst_f
    if len(lst) <= 1:
        return lst
    left = []
    center = []
    right = []
    for i in lst:
        if i < lst[0]:
            left.append(i)
        elif i > lst[0]:
            right.append(i)
        elif i == lst[0]:
            center.append(i)
    return (quick_sort(left) + center + quick_sort(right))

color_mas = ["черный", "белый", "серый", "красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый", "розовый"]
##генератор цвета
def color_rand():
    """генератор цвета"""
    return color_mas[random.randint(0, 10)]

number_mas = ["А", "В", "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У", "Х"]
##генератор гостударственного номера
def number_rand():
    """генератор гостударственного номера"""
    res = number_mas[random.randint(0, 11)] + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + number_mas[random.randint(0, 11)] +number_mas[random.randint(0, 11)]
    return res

model_mas = ["BMV", "Mercedes", "Audi", "Ford", "Honda", "Hyundai", "Kia", "Lada", "Mazda", "Mitsubishi", "Nissan", "Renault", "Skoda", "Toyota", "Volkswagen", "Jeep", "Lexus", "Tesla", "Dodge", "Subaru"]
##генератор модели
def model_rand():
    """генератор модели"""
    return model_mas[random.randint(0, 19)]

##генератор года выпуска
def year_rand():
    """генератор года выпуска"""
    return random.randint(1990, 2022)

surname_male_mas = ["Шевелёк", "Левкович", "Шеин", "Ягуткин", "Николаенко", "Сюсин", "Флёров", "Будаев", "Браславец", "Шашлов", "Сизов", "Усачёв", "Сиянцев", "Мишуринский", "Коллеров", "Ястребов", "Белорусов", "Зинченко", "Кирьянов", "Гавриленко", "Макаров", "Рюриков", "Мельник", "Фахриев", "Казнов", "Чупалов", "Моряев", "Чежеков", "Малиновский", "Каримов", "Яхлаков", "Меледин", "Цехановецкий", "Щербина", "Шаповалов", "Кугушев", "Шитов", "Тетерев", "Кравец", "Усилов", "Шкригунов", "Фоменков", "Хоботилов", "Яфраков", "Чуринов", "Ярополов", "Сёмин", "Хахалин", "Тютчев", "Крыжов", "Никулаичев", "Набиуллин", "Шурупов", "Краснопёров", "Казнов", "Шипицин", "Кауфман", "Зиновьев", "Каганович", "Рубцов", "Бореев", "Белевич", "Кирдань", "Леонов", "Собчак", "Баскаков", "Карманов", "Эмский", "Аристов", "Семянин", "Янцев", "Косоруков", "Фильченков", "Чепурин", "Куимов", "Носачёв", "Талызин", "Бубенцов", "Кириллов", "Крупин", "Кривоплясов", "Яндарбиев", "Сиянгулов", "Бегичев", "Теплухин", "Камкин", "Эвентов", "Шаршин", "Грибков", "Вязьмитин", "Типалов", "Ёжин", "Ябловский", "Латышев", "Лунин", "Бабкин", "Лобан", "Шентеряков", "Канадов", "Дрёмин", "Николаенко", "Ёжов", "Мяукин", "Северин", "Пугин", "Максимов", "Касьяненко", "Игонин", "Нырцев", "Саянский", "Ивкин", "Анисимов", "Виноградов", "Дроздов", "Воропаев", "Кожедуб", "Кадников", "Муратов", "Енин", "Яробкин", "Ягнышев", "Приказчиков", "Лачков", "Чучанов", "Жванецкий", "Хлебников", "Полотенцев", "Лысов", "Тимошкин", "Кетов", "Чичеринов", "Ажищенков", "Кравцев", "Ахременко", "Бальсунов", "Долгов", "Жеглов", "Дьяченко", "Мухов", "Сиянович", "Сигачёв", "Чичваркин", "Смышляев", "Лимаров", "Шурьев", "Александрович", "Брязгин", "Легкодимов", "Дубков", "Рытин", "Набиуллин", "Решетов", "Юдицкий", "Ахвледиани", "Пасхин", "Павленко", "Беломестнов", "Дмитровский", "Гусельников", "Нестеров", "Механтьев", "Шлыков", "Экономов", "Фонвизин", "Чендев", "Майсак", "Лавлинский", "Котяш", "Никеров", "Лисов", "Бурдаков", "Чигиркин", "Браславец", "Салтыков", "Дасаев", "Пряхин", "Аводков", "Шарапов", "Чернаков", "Челомцев", "Бабкин", "Бушуев", "Целиковский", "Криворотов", "Шагидзянов", "Чендев", "Балаев", "Грачев", "Пищальников", "Коротков", "Достоевский", "Райков", "Александрович", "Кочинян", "Поджио", "Климцов", "Силиванов", "Беломестный", "Шангин", "Синай", "Миронов", "Ядрищенский", "Болдаев", "Янцев", "Водопьянов", "Кругликов", "Краснокутский", "Щеголев", "Калюта", "Грешнев", "Справцев", "Кручинкин", "Зубов", "Котов", "Нустров", "Вахрушев", "Данькин", "Аргамаков", "Ермолов", "Вихорев", "Расторгуев", "Ларин", "Поздов", "Кузаев", "Блохин", "Иволгин", "Николаичев", "Проскуркин", "Посохов", "Гурьев", "Лисов", "Выгузов", "Лапаев", "Крупин", "Чечин", "Хомичев", "Щенин", "Михалицин", "Шкригунов", "Андроников", "Слепынин", "Ядрищенский", "Марков", "Сергеевич", "Должиков", "Мажулин", "Фламин", "Пименов", "Низамутдинов", "Аристархов", "Теплых", "Жабкин", "Родионов", "Лоскутов", "Мосяков", "Сидоров", "Щитт", "Науменко", "Березовский", "Ячменцев", "Аристов", "Ядов", "Кандаков", "Аксенчук", "Ткаченко", "Ляпушкин", "Дьяконов", "Собачкин", "Алешин", "Пондяков", "Чекин", "Рязанцев", "Борков", "Борзилов", "Трухин", "Трошкин", "Геремеш", "Икрамов", "Папенин", "Сигачёв", "Махов", "Цыцын", "Достовалов", "Думановский", "Щередин", "Корявов", "Яншин", "Суриков", "Панюшкин", "Хохорин", "Малкин", "Асланов", "Набойщиков", "Любимцев", "Баушев", "Нагиев", "Шадрин", "Колпаков", "Антимонов", "Пузаков", "Катаев", "Мелехов", "Федоренко", "Цельнер", "Яромеев", "Горемыкин", "Краснопёров", "Лощилов", "Пенкин", "Экземплярский", "Якшилов", "Фастер", "Красильников", "Мандрыка", "Шуляк", "Коржев", "Трибой", "Москвин", "Подкользин", "Валюхов", "Усов", "Якунин", "Белевич", "Савицкий", "Кольцов", "Компанец", "Бушуев", "Чуприн", "Кутузов", "Шелагин", "Снытко", "Смирнитский", "Тукаев", "Чужинов", "Шмелёв", "Золотов", "Машир", "Фотин", "Яскин", "Царев", "Ягфаров", "Антипин", "Жарыхин", "Туполев", "Лель", "Лягушов", "Телицын", "Шастин", "Мамин", "Зонов", "Шапиро", "Романенко", "Курышин", "Якусик", "Ханипов", "Козлитин", "Ясенков", "Майоров", "Чичеров", "Яскин", "Мозговой", "Никитин", "Дыховичный", "Дубков", "Сергеев", "Щербина", "Попков", "Ковшевников", "Юрьев", "Летавин", "Ворожцов", "Шелепин", "Чеботарев", "Русаков", "Бабатьев", "Яндашевский", "Завьялов", "Катасонов", "Швечиков", "Другов", "Лимаров", "Рудавин", "Тенишев", "Кузинов", "Образцов", "Коренев", "Чалый", "Ялбачев", "Яковленко", "Кравцев", "Апакидзе", "Лоскутников", "Щерба", "Пондяков", "Кярбер", "Кружков", "Шумов", "Кизатов", "Пугачев", "Комзин", "Соломинцев", "Григорьев", "Бажанов", "Шкловский", "Наполов", "Тредиаковский", "Нутрихин", "Кораблёв", "Яйцов", "Андроников", "Лопатин", "Гуковский", "Бессонов", "Викашев", "Воробьев", "Богатырёв", "Целиковский", "Корзоватых", "Котяш", "Юнге", "Жиганов", "Ясин", "Ягубский", "Гаранин", "Лапухин", "Рябкин", "Ягуткин", "Калашников", "Варфоломеев", "Староволков", "Кирилловский", "Шайн", "Остроумов", "Зубок", "Актжанов", "Шайнюк", "Бенедиктов", "Енотин", "Абрамович", "Ярославцев", "Колобов", "Лозанов", "Юнкин", "Лоскутов", "Живков", "Рожков", "Януть", "Голубов", "Купцов", "Кваснин", "Ярославцев", "Окрокверцхов", "Ноздрин", "Шмелев", "Карамзин", "Курдиков", "Ходяев", "Каменев", "Витвинин", "Новомейский", "Натаров", "Гребнев", "Лялюшкин", "Кораблёв", "Лель", "Чюличков", "Дудник", "Ячменев", "Кайназаров", "Астафьев", "Ханилов", "Брантов", "Цорн", "Яйцев", "Элефтеров", "Корсаков", "Чичваркин", "Павлов", "Кривоплясов", "Трофимов", "Сигаев", "Вышегородских", "Мосин", "Толбугин", "Фуриков", "Каиров", "Ядрышников", "Капитанчук", "Ложкин", "Ледовской", "Якубович", "Булка", "Ярощук", "Желваков", "Сукин", "Саввин", "Янукович", "Полешко", "Зюлёв", "Скосырский", "Кружков", "Эльмпт", "Васин", "Мукосеев", "Чечин", "Оленев", "Аношкин", "Демин", "Якубов", "Гусин", "Худовеков", "Чечуров", "Бояринов", "Бабушкин", "Каримов", "Ялунин", "Кирилловский", "Северин", "Степанишин", "Утёсов", "Ханинов", "Оболенский", "Горюнов", "Огородников", "Кузубов", "Сагадеев", "Левтев", "Набоков", "Соломинцев", "Якунчиков", "Арсеньев", "Токмаков", "Еськов", "Остроумов", "Жербин", "Оболенский", "Беломестных", "Крутой", "Казаков", "Хадеев", "Шуршалин", "Осокин", "Петрухин", "Москвитин", "Курчатов", "Еркулаев", "Питосин", "Букавицкий", "Лель", "Русаков", "Капп", "Котельников", "Берлунов", "Рыбаков", "Дворников", "Астрединов", "Клименков", "Образцов", "Андроников", "Юмашев", "Трохин", "Тизенгаузен", "Жикин", "Горбачев", "Будников", "Батурин", "Грибакин", "Розенбах", "Трухин", "Михалёв", "Думановский", "Липин", "Шапкин", "Кооскора", "Бабанин", "Буряков", "Куджиашвили", "Автухов", "Романов", "Лившиц", "Нусинов", "Новомейский", "Кунаковский", "Демин", "Лидин", "Родин", "Петрухин", "Сухарев", "Заболотный", "Чечин", "Закрятин", "Худовеков", "Коденко", "Сочинский", "Смотров", "Голубцов", "Борцов", "Уваров", "Дёмшин", "Ярочкин"]
name_male_mas = ["Марк", "Глеб", "Александр", "Илья", "Максим", "Андрей", "Георгий", "Артём", "Фёдор", "Иван", "Дмитрий", "Ян", "Лев", "Мирон", "Михаил", "Владимир", "Ярослав", "Захар", "Дамир", "Матвей", "Егор", "Платон", "Николай", "Кирилл", "Владислав", "Карим", "Пётр", "Артур", "Руслан", "Никита", "Тимофей", "Адам", "Данил", "Савелий", "Роман", "Константин", "Тихон", "Даниил", "Макар", "Елисей", "Сергей", "Борис", "Юрий", "Артемий", "Гордей", "Давид", "Даниэль", "Василий", "Денис", "Степан", "Святослав", "Демьян", "Тимур", "Алексей", "Григорий", "Арсений", "Семён", "Мирослав", "Марсель", "Роберт", "Анатолий", "Павел", "Станислав", "Антон", "Али", "Евгений", "Яков", "Виктор", "Олег", "Вячеслав", "Билал", "Филипп", "Савва", "Леон", "Леонид", "Серафим", "Эмиль", "Лука", "Всеволод", "Богдан", "Вадим", "Тигран", "Ибрагим", "Игорь", "Герман", "Данила", "Рустам", "Назар", "Демид", "Виталий", "Альберт", "Эмир", "Родион", "Клим", "Марат", "Камиль", "Яромир", "Эмин", "Даниль", "Аркадий", "Тихон", "Бронислав", "Онуфрий", "Наум", "Филимон", "Макар", "Филипп", "Дементий", "Серафим", "Ипполит", "Иннокентий", "Павел", "Федот", "Максимильян", "Яромир", "Рустам", "Игнатий", "Фома", "Лев", "Кузьма", "Родион", "Осип", "Денис", "Роман", "Евграф", "Михаил", "Демид", "Адам", "Феликс", "Аркадий", "Агап", "Геннадий", "Виссарион", "Степан", "Арсен", "Всеволод", "Григорий", "Иосиф", "Чеслав", "Эмиль", "Ярослав", "Валерьян", "Данияр", "Кирилл", "Мстислав", "Валерий", "Антон", "Дмитрий", "Рюрик", "Остап", "Борис", "Прокл", "Петр", "Камиль", "Андриян", "Эрик", "Артемий", "Фадей", "Данила", "Данил", "Капитон", "Юлиан", "Арсений", "Эмир", "Виктор", "Вацлав", "Феофан", "Гаврила", "Тимофей", "Казимир", "Владимир", "Эрнст", "Терентий", "Кондрат", "Антип", "Евгений", "Тигран", "Святослав", "Аристарх", "Дамир", "Вячеслав", "Вениамин", "Прохор", "Никифор", "Даниил", "Владлен", "Данис", "Егор", "Фока", "Радислав", "Никанор", "Богдан", "Тарас", "Агафон", "Глеб", "Владилен", "Захар", "Евстигней", "Руслан", "Юлий"]
father_male_mas = ["Ааронович", "Абрамович", "Августович", "Авдеевич", "Аверьянович", "Адамович", "Адрианович", "Акимович", "Аксёнович", "Александрович", "Алексеевич", "Анатольевич", "Андреевич", "Андроникович", "Анисимович", "Антипович", "Антонович", "Ануфриевич", "Аркадьевич", "Арсенович", "Арсеньевич", "Артёмович", "Артемьевич", "Артурович", "Архипович", "Афанасьевич", "Ахматович", "Батькович", "Бедросович", "Бенедиктович", "Богданович", "Бориславич", "Бориславович", "Борисович", "Борисыч", "Брониславович", "Ваганович", "Вадимович", "Валентинович", "Валерианович", "Валерьевич", "Валерьянович", "Васильевич", "Вахтангович", "Венедиктович", "Вениаминович", "Викентьевич", "Викторович", "Виленович", "Вилорович", "Виссарионович", "Витальевич", "Владиленович", "Владимирович", "Владиславович", "Владленович", "Власович", "Вольфович", "Всеволодович", "Гавриилович", "Гаврилович", "Гаджиевич", "Геннадиевич", "Геннадьевич", "Генрихович", "Георгиевич", "Герасимович", "Германович", "Гертрудович", "Глебович", "Гордеевич", "Григорьевич", "Гурьевич", "Давидович", "Давыдович", "Даниилович", "Данилович", "Демидович", "Демьянович", "Денисович", "Димитриевич", "Дмитриевич", "Дорофеевич", "Евгеньевич", "Евграфович", "Евдокимович", "Евсеевич", "Евстигнеевич", "Егорович", "Елизарович", "Елисеевич", "Емельянович", "Еремеевич", "Ермилович", "Ермолаевич", "Ерофеевич", "Ефимович", "Ефимьевич", "Ефремович", "Ефстафьевич", "Жанович", "Жоресович", "Захарович", "Захарьевич", "Зиновьевич", "Ибрагимович", "Иванович", "Иваныч", "Игнатович", "Игнатьевич", "Игоревич", "Измаилович", "Изотович", "Израилевич", "Иларионович", "Ильгизович", "Ильич", "Ильмирович", "Ильнурович", "Ильсурович", "Ильясович", "Иоаннович", "Иосипович", "Иосифович", "Исаевич", "Исидорович", "Каллиникович", "Каллистратович", "Константинович", "Леонидович", "Леонович", "Леонтьевич", "Львович", "Магомедович", "Магометович", "Макарович", "Максимилианович", "Максимович", "Маркович", "Маркыч", "Матвеевич", "Михайлович", "Михалыч", "Натанович", "Наумович", "Никандрович", "Никанорович", "Никитич", "Никитович", "Никифорович", "Никодимович", "Николаевич", "Никонович", "Олегович", "Осипович", "Павлович", "Петрович", "Платонович", "Прохорович", "Романович", "Ростиславович", "Рудольфович", "Русланович", "Рустамович", "Семёнович", "Сергеевич", "Сидорович", "Сильвестрович", "Соломонович", "Степанович", "Тарасович", "Теймуразович", "Терентьевич", "Тимофеевич", "Тимурович", "Тихонович", "Трифонович", "Трофимович", "Устинович", "Фадеевич", "Фёдорович", "Федосеевич", "Федосьевич", "Федотович", "Феликсович", "Феодосьевич", "Феоктистович", "Феофанович", "Филатович", "Филимонович", "Филиппович", "Фокич", "Фомич", "Фролович", "Харитонович", "Харламович", "Харлампович", "Харлампьевич"]
surname_female_mas = ["Ясева", "Цызырева", "Кобелева", "Лебедева", "Кутякова", "Дубинкина", "Короткова", "Слобожанина", "Горбачева", "Ковтунова", "Дрягина", "Юркова", "Яскина", "Гудкова", "Якимычева", "Пивоварова", "Цыркунова", "Бородина", "Борева", "Глинка", "Яблонева", "Ковшутина", "Потапова", "Грибоедова", "Лидина", "Скороходова", "Грекова", "Пичугина", "Никитина", "Мамыкина", "Васнецова", "Зууфина", "Абоимова", "Уржумцева", "Яшвили", "Челпанова", "Кулешова", "Дворецкова", "Куприянова", "Исмайлова", "Ямбаева", "Гречко", "Ибрагимова", "Чупрова", "Чеснокова", "Муленко", "Воеводина", "Строганова", "Мерзлова", "Жиганова", "Панькива", "Прудникова", "Шибалкина", "Щавлева", "Гайдукова", "Суружу", "Богачёва", "Савкина", "Полухина", "Чистякова", "Безукладникова", "Ижутина", "Дёмшина", "Двойнева", "Любимова", "Игошина", "Левтева", "Вагина", "Александрова", "Проскура", "Божко", "Аргамакова", "Абалышева", "Сиянгулова", "Иноземцева", "Булатова", "Мосенцова", "Толстой", "Куклачёва", "Балина", "Саянкова", "Черная", "Зиновьева", "Левкович", "Гольца", "Веточкина", "Шаврина", "Николина", "Ветрова", "Архаткина", "Калачева", "Колосова", "Пьянкова", "Глоба", "Седыха", "Грибалева", "Азаренкова", "Майсака", "Язина", "Снаткина", "Абросимова", "Колобова", "Апалкова", "Крайнева", "Щукина", "Яковалева", "Ульянова", "Ивашечкина", "Лукина", "Битнера", "Круглова", "Снегирёва", "Валуева", "Киреева", "Пелёвина", "Ясинова", "Цулукидзе", "Сиясинова", "Портнова", "Доронина", "Бершова", "Бармыкина", "Блинова", "Толкачёва", "Морозова", "Капица", "Менде", "Дябина", "Ельцова", "Платонова", "Загидуллина", "Дукачёва", "Яцко", "Добронравова", "Яимова", "Подмазко", "Кризько", "Чичваркина", "Гришкина", "Тесла", "Рыжкова", "Моисеева", "Остальцева", "Карамзина", "Клокова", "Чикунова", "Жарыхина", "Корявова", "Шерстова", "Сильвестрова", "Козлитина", "Эссена", "Апраксина", "Графова", "Тычкина", "Голованова", "Галиаскарова", "Ермолова", "Панкратова", "Брынскиха", "Царева", "Чижова", "Кулактина", "Логвинова", "Таланова", "Красенкова", "Ильинская", "Ярыкина", "Бояринова", "Кочеткова", "Терентьева", "Акимова", "Антонович", "Дуркина", "Яушкина", "Жжёнова", "Соломинцева", "Жикина", "Сенькина", "Пустохина", "Куликова", "Анюкова", "Зубова", "Нугаева", "Жарова", "Ярощука", "Петрищева", "Ильюшина", "Немова", "Целобанова", "Сиянович", "Ястребова", "Прохорова", "Шурша", "Быстрова", "Ёжина", "Мащенко", "Корнейчука", "Никитенко", "Пряхина", "Кучава", "Лапухова", "Эпингера", "Парамонова", "Севостьянова", "Минина", "Подколодный", "Малинина", "Справцева", "Яцкевич", "Янкова", "Низовцова", "Расторгуева", "Абарникова", "Державина", "Кимаска", "Набадчикова", "Русанова", "Кондратова", "Демидова", "Пшеничникова", "Унтилова", "Янкилович", "Лукьянова", "Любова", "Нилина", "Лашкина", "Жевлакова", "Курепина", "Манторова", "Можаева", "Агейкина", "Милюкова", "Гольдина", "Приходько", "Аллилуева", "Ильясова", "Махмудова", "Пономарёва", "Шипицина", "Сенотрусова", "Плюхина", "Ярыгина", "Дроздова", "Югова", "Фирсова", "Белова", "Косомова", "Сергеевич", "Курышина", "Шувалова", "Занина", "Калашникова", "Лазарева", "Некрасова", "Радченко", "Ямалтдинова", "Кидина", "Кропанина", "Швецова", "Никерова", "Якунова", "Холода", "Дементьева", "Бабикова", "Пахомова", "Ягемана", "Хромченко", "Зарубина", "Дуболазова", "Балтабева", "Суслова", "Захарьина", "Хейчеева", "Субботина", "Курневич", "Гавриленкова", "Яненко", "Кушнарёва", "Матвеева", "Яклашкина", "Сереброва", "Садовничая", "Сухова", "Муратова", "Дульцева", "Болокана", "Пережогина", "Пустоходова", "Сафонова", "Бранта", "Разуваева", "Кузинова", "Мешкова", "Муравьева", "Фомичева", "Полторака", "Малюгина", "Савицкая", "Кондакова", "Кожедуба", "Веселкова", "Калинина", "Позона", "Калугина", "Куваева", "Дейнекина", "Костина", "Комяхова", "Спиридонова", "Поликарпова", "Этуша", "Бирюкова", "Михеева", "Северинова", "Михалёва", "Дюженкова", "Кирилова", "Берестова", "Сай", "Урусова", "Мигунова", "Нагибина", "Гусева", "Гулина", "Гуслякова", "Островерхова", "Талалина", "Белоусова", "Успенская", "Черенчикова", "Головченко", "Озерова", "Москвина", "Силина", "Крючкова", "Чемериса", "Сиякаева", "Федорова", "Розенбаха", "Никаева", "Висенина", "Петровская", "Гавшина", "Ягешева", "Лескова", "Мячина", "Янчурова", "Милютина", "Корнилова", "Ахвледиани", "Никольская", "Чебыкина", "Янаева", "Шаньгина", "Головина", "Семина", "Ювелева", "Кириллова", "Жарикова", "Кулумбаева", "Эфирова", "Пономарева", "Энтина", "Званцева"]
name_female_mas = ["Эльвира", "Валерия", "Анисья", "Алиса", "Анфиса", "Лилия", "Марфа", "Глафира", "Пелагея", "Алёна", "Айлин", "Агафья", "Римма", "Аза", "Жасмин", "Лейла", "Сафина", "Ариана", "Стела", "Христина", "Ирина", "Тамара", "Евдокия", "Марьяна", "Елена", "Дария", "Сафия", "Лиана", "Аделя", "Амалия", "Василина", "Милана", "Милослава", "Алисия", "Сабрина", "Ольга", "Ярослава", "Наталья", "Амина", "Полина", "Агния", "Елизавета", "Бронислава", "Вероника", "Майя", "Камилла", "Мадина", "Асия", "Фатима", "Соня", "Евангелина", "Эмилия", "Светлана", "Айша", "Мариам", "Мия", "Ангелина", "Таисия", "Злата", "Дарья", "Розалия", "Станислава", "Оксана", "Юлиана", "Миа", "Изольда", "Владлена", "Ульяна", "Инга", "Анисия", "Ника", "Алеся", "Алина", "Аврора", "Зинаида", "Кира", "Лия", "Рената", "Аглая", "Серафима", "Евгения", "Олеся", "Дана", "Ефросиния", "Татьяна", "Стефания", "Юнона", "Теона", "Сара", "Лада", "Анастасия", "Каролина", "Мария", "Милена", "Медина", "Изабелла", "Лина", "Катерина", "Регина", "Александра", "Виктория", "Жанна", "Элеонора", "Нона", "Альбина", "Варвара", "Наталия", "Марьям", "Виталина", "Ксения", "Антонина", "Тея", "Есения", "Моника", "Ясина", "Доминика", "Эвелина", "Мишель", "Ираида", "Анжелика", "Лея", "Вера", "Ася", "Аяна", "Рада", "Эмма", "Белла", "Диана", "Берта", "Инесса", "Мила", "Аиша", "Роза", "Любава", "Элина", "Сабина", "Василиса", "Марина", "Дарина", "Ева", "Нина", "Надежда", "Марианна", "Ясмина", "Зоя", "Адриана", "Раиса", "Яна", "Анна", "Ариадна", "Инна", "Ефросинья", "Алсу", "Софья", "Кристина", "Мира", "Оливия", "Всеслава", "Николь", "Ясмин", "Юлия", "Нелли", "Екатерина", "Малика", "Амира", "Влада", "Карина", "Виолетта", "Лидия", "Амелия", "Алла", "Галина", "Адель", "Камила", "Людмила", "Валентина", "Дина", "Лариса", "Альфия", "Мирослава", "София", "Афина", "Фаина", "Аида", "Клара", "Маргарита", "Владислава", "Любовь", "Мелания", "Мелисса", "Марта", "Арина", "Агата"]
father_female_mas = ["Александровна", "Алексеевна", "Анатольевна", "Андреевна", "Антоновна", "Аркадьевна", "Артемовна", "Богдановна", "Борисовна", "Валентиновна", "Валерьевна", "Васильевна", "Викторовна", "Виталиевна", "Владимировна", "Владиславовна", "Вячеславовна", "Геннадиевна", "Георгиевна", "Григорьевна", "Даниловна", "Денисовна", "Дмитриевна", "Евгеньевна", "Егоровна", "Ефимовна", "Ивановна", "Игоревна", "Ильиничн", "Иосифовна", "Кирилловна", "Константиновна", "Леонидовна", "Львовна", "Максимовна", "Матвеевна", "Михайловна", "Николаевна", "Олеговна", "Павловна", "Петровна", "Платоновна", "Робертовна", "Романовна", "Семеновна", "Сергеевна", "Станиславовна", "Степановна", "Тарасовна", "Тимофеевна", "Федоровна", "Феликсовна", "Филипповна", "Эдуардовна", "Юрьевна", "Яковлевна", "Ярославовна"]
##генератор имени владельца
def name_rand():
    """генератор имени владельца"""
    if random.randint(0, 1) == 0:
        return surname_male_mas[random.randint(0, 599)] + " " + name_male_mas[random.randint(0, 199)] + " " + father_male_mas[random.randint(0, 197)]
    else:
        return surname_female_mas[random.randint(0, 364)] + " " + name_female_mas[random.randint(0, 192)] + " " + father_female_mas[random.randint(0, 56)]

##создание таблицы
def create_table(n):
    """создание таблицы"""
    names = []
    models = []
    years = []
    numbers = []
    colors = []
    for i in range(0, n):
        names.append(name_rand())
        models.append(model_rand())
        years.append(year_rand())
        numbers.append(number_rand())
        colors.append(color_rand())
    table = pd.DataFrame({'ФИО' : names, 'марка' : models, 'год выпуска' : years, 'номер': numbers, 'цвет' : colors})
    table.to_csv('car' + str(n) + '.csv', index = False)

##создание таблиц
def create_tables(n):
    """создание таблиц"""
    for i in n:
        create_table(i)

n = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000]
create_tables(n)

##сортировка таблицы
def work_for_one(n):
    """сортировка таблицы"""
    table = pd.read_csv('car' + str(n) + '.csv')
    mas = []
    for i in range(0, n):
        elem = Car(table.iloc[i])
        mas.append(elem)
    sort_names1 = []
    sort_models1 = []
    sort_years1 = []
    sort_numbers1 = []
    sort_colors1 = []
    sort_names2 = []
    sort_models2 = []
    sort_years2 = []
    sort_numbers2 = []
    sort_colors2 = []
    sort_names3 = []
    sort_models3 = []
    sort_years3 = []
    sort_numbers3 = []
    sort_colors3 = []
    start1 = time()
    sort_list1 = choice_sort(mas)
    time1 = time() - start1
    start2 = time()
    sort_list2 = merge_sort(mas)
    time2 = time() - start2
    start3 = time()
    sort_list3 = quick_sort(mas)
    time3 = time() - start3
    for i in range(0, n):
        sort_names1.append(sort_list1[i].name)
        sort_names2.append(sort_list2[i].name)
        sort_names3.append(sort_list3[i].name)
        sort_models1.append(sort_list1[i].model)
        sort_models2.append(sort_list2[i].model)
        sort_models3.append(sort_list3[i].model)
        sort_years1.append(sort_list1[i].year)
        sort_years2.append(sort_list2[i].year)
        sort_years3.append(sort_list3[i].year)
        sort_numbers1.append(sort_list1[i].number)
        sort_numbers2.append(sort_list2[i].number)
        sort_numbers3.append(sort_list3[i].number)
        sort_colors1.append(sort_list1[i].color)
        sort_colors2.append(sort_list2[i].color)
        sort_colors3.append(sort_list3[i].color)
    sort_table1 = pd.DataFrame({'ФИО' : sort_names1, 'марка' : sort_models1, 'год выпуска' : sort_years1, 'номер': sort_numbers1, 'цвет' : sort_colors1})
    sort_table2 = pd.DataFrame({'ФИО' : sort_names2, 'марка' : sort_models2, 'год выпуска' : sort_years2, 'номер': sort_numbers2, 'цвет' : sort_colors2})
    sort_table3 = pd.DataFrame({'ФИО' : sort_names3, 'марка' : sort_models3, 'год выпуска' : sort_years3, 'номер': sort_numbers3, 'цвет' : sort_colors3})
    sort_table1.to_csv('sort_car1_' + str(n) + '.csv', index = False)
    sort_table2.to_csv('sort_car2_' + str(n) + '.csv', index = False)
    sort_table3.to_csv('sort_car3_' + str(n) + '.csv', index = False)
    print(n, time1, time2, time3)
    return time1, time2, time3

##сортировка таблиц
def work_for_every(n):
    """сортировка таблиц"""
    x = []
    y1 = []
    y2 = []
    y3 = []
    for i in n:
        time1, time2, time3 = work_for_one(i)
        x.append(i)
        y1.append(time1)
        y2.append(time2)
        y3.append(time3)
    time_table = pd.DataFrame({'Количество элементов' : x, 'Сортировка выбором' : y1, 'Сортировка слиянием' : y2, 'Быстрая сортировка' : y3})
    time_table.to_csv('time.csv', index = False)
    plt.plot(x, y1, x, y2, x, y3)
    plt.show()

work_for_every(n)
