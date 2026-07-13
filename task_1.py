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

    # Создаем метод для подсчета общей стоимости покупок.
    def check_amount(self):
        total = []
        # Собираем цены всех товаров, которые лежат в чеке.
        for item in self.__name_item:
            total.append(self.__item_price[item])
        # Считаем сумму списка цен.
        total_sum = sum(total)

        # Проверяем условие скидки (больше 10 товаров в чеке).
        if len(self.__name_items) > 10:
            return  total_sum * 0.9
        
        return total_sum

    # Создаем метод для рассчета НДС товаров, у которых ставка 20%.
    # Метод для вычисления НДС 20%.
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        # Фильтруем товар со ставкой 20%.
        for item in self.__name_items:
            if self.__tax_rate[item]  == 20:
                twenty_percent_tax.append(item)

        total = []
        # Находим цены для отфильтрованых товаров.
        for item in twenty_percent_tax:
            total.append(self.__item_price[item])
        # Считаем базовую сумму НДС (стоимость товаров * 0.2).
        tax_sum = sum(total) * 0.2

        # Если товаров в чеке больше 10, уменьшаем сумму НДС на 10% скидки. 
        if len(self.__name_items) > 10:
            return tax_sum * 0.9
        return tax_sum

    # Создаем метод для рассчета НДС товаров, у которых ставка 10%.
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        # Фильтруем товар со ставкой 10%.
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)

        total = []
        # Находим цены для отрицательных товаров.
        for item in ten_percent_tax:
            total.append(self.__item_price[item])
        # Считаем базовую стоимость НДС (стоимость товаров * 0.1).
        tax_sum = sum(total) * 0.1

        # Если товаров в чеке больше 10, уменьшаем сумму НДС на 10% скидки.  
        if len(self.__name_items) > 10:
            return tax_sum * 0.9
        return tax_sum


