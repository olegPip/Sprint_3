import datetime

class OnlineSalesRegisterCollector: # Создан класс для работы с онлайн-кассой.   

    def __init__(self):
        self.__name_items = []     # Класс содержет, список name_items с перечнем товаров в чеке.
        self.__number_items = 0    # Класс содержет, переменную number_items с количеством товаров в чеке.
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}  # Класс содержет, словарь item_price, где перечислены товары магазина и их стоимость.
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}     # Класс содержет, словарь tax_rate, где записана налоговая ставка на товары. Она составляет 10% или 20% от стоимости.  

    # Геттеры, которые получают значения name_items и number_items.  
    # Геттер для получения списка названия товаров.
    @property
    def name_items(self):
        return self.__name_items
    
    # Геттер для получения количества товаров
    @property
    def number_items(self):
        return self.__number_items