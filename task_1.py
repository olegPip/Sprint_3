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
    
     # Метод для добавления товара в чек.
    def add_item_to_cheque(self, name):
        # Проверяем длину названия товара.
        if len(name) == 0 or len(name) > 40: 
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')  
        # Проверяем наличие товара в справочнике цен.
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике') 
        # В остальных случаях добавляем товар в name_items и увеличивает значение number_items на 1.
        self.__name_items.append(name)
        self.__number_items += 1

       # Создаем метод для удаления товара из чека. 
    def delete_item_from_check(self, name):
        # Проверяем, есть ли товар в самом чеке.
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')       
        # Удаляем товар и уменьшаем счётчик на 1.
        self.__name_items.remove(name)
        self.number_items -=  1

































































