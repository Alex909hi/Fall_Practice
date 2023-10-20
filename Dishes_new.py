# Задание: вывести продукты и их кол-во в зависимости от кол-ва гостей на празднике
cook_book = [
['салат',
[ ['картофель', 100, 'гр.'],
['морковь', 50, 'гр.'],
['огурцы', 50, 'гр.'],
['горошек', 30, 'гр.'],
['майонез', 70, 'мл.'], ] ],
['пицца',
[ ['сыр', 50, 'гр.'],
['томаты', 50, 'гр.'],
['тесто', 100, 'гр.'],
['бекон', 30, 'гр.'],
['колбаса', 30, 'гр.'],
['грибы', 20, 'гр.'], ] ],
['фруктовый десерт',
[ ['хурма', 60, 'гр.'],
['киви', 60, 'гр.'],
['творог', 60, 'гр.'],
['сахар', 10, 'гр.'],
['мед', 50, 'мл.'], ] ] ]

class cooking:
    #🥗🥗🥗🥗🥗
    def salad(self):
        print(f"🥗🥗🥗{str(cook_book[0][0]).capitalize()}")
        self.sum_weight(self.potatoes(), self.potatoes_weight(), sum_people )
        self.sum_weight(self.carrot(), self.carrot_weight(), sum_people )
        self.sum_weight(self.cucumber(), self.cucumber_weight(), sum_people )
        self.sum_weight(self.pea(),self.pea_weight(), sum_people )
        self.sum_weight( self.mayonnaise(), self.mayonnaise_weight(),sum_people  )
    #🥔🥔🥔
    def potatoes(self):
        return cook_book[0][1][0][0]
    def potatoes_weight(self):
        return int(cook_book[0][1][0][1])
    #🥕🥕🥕
    def carrot(self):
        return cook_book[0][1][1][0]
    def carrot_weight(self):
        return int(cook_book[0][1][1][1])
    #🥒🥒🥒
    def cucumber(self):
            return cook_book[0][1][2][0]
    def cucumber_weight(self):
        return int(cook_book[0][1][2][1])
    # Горошек
    def pea(self):
        return cook_book[0][1][3][0]
    def pea_weight(self):
        return int(cook_book[0][1][3][1])
    # Майонез
    def mayonnaise(self):
        return cook_book[0][1][4][0]
    def mayonnaise_weight(self):
        return int(cook_book[0][1][4][1])
    #=======================================================================
    #🍕🍕🍕🍕🍕
    def pizza(self):
        print(f"🍕🍕🍕{str(cook_book[1][0]).capitalize()}")
        self.sum_weight(self.cheese() ,self.cheese_weight() ,sum_people)
        self.sum_weight(self.tomato(),self.tomato_weight() ,sum_people)
        self.sum_weight(self.dough(),self.dough_weight() ,sum_people)
        self.sum_weight(self.bacon() ,self.bacon_weight() ,sum_people)
        self.sum_weight(self.sausage(),self.sausage_weight() ,sum_people)
        self.sum_weight(self.mushroom() ,self.mushroom_weight() ,sum_people)
    #🧀🧀🧀
    def cheese(self):
        return cook_book[1][1][0][0]
    def cheese_weight(self):
        return int(cook_book[1][1][0][1])
    #🍅🍅🍅
    def tomato(self):
        return cook_book[1][1][1][0]
    def tomato_weight(self):
        return int(cook_book[1][1][1][1])
    #🍞🍞🍞
    def dough(self):
        return cook_book[1][1][2][0]
    def dough_weight(self):
        return int(cook_book[1][1][2][1])
    #🥓🥓🥓
    def bacon(self):
        return cook_book[1][1][3][0]
    def bacon_weight(self):
        return int(cook_book[1][1][3][1])
    #🌭🌭🌭
    def sausage(self):
        return cook_book[1][1][4][0]
    def sausage_weight(self):
        return int(cook_book[1][1][4][1])
    #🍄🍄🍄
    def mushroom(self):
        return cook_book[1][1][5][0]
    def mushroom_weight(self):
        return int(cook_book[1][1][5][1])
    #=======================================================================
    #🍉🍋🍇🍊🍐
    def fruit_dessert(self): 
        print(f"🍇🍊🍐{str(cook_book[2][0]).capitalize()}")
        self.sum_weight(self.persimmon(), self.persimmon_weight(), sum_people)
        self.sum_weight(self.kiwi(),self.kiwi_weight(),sum_people)
        self.sum_weight(self.curd(),self.curd_weight(),sum_people)
        self.sum_weight(self.sugar(),self.sugar_weight(),sum_people)
        self.sum_weight(self.honey(),self.honey_weight(),sum_people)
    # Хурма
    def persimmon(self):
        return cook_book[2][1][0][0]
    def persimmon_weight(self):
        return int(cook_book[2][1][0][1])
    #🥝🥝🥝
    def kiwi(self):
        return cook_book[2][1][1][0]
    def kiwi_weight(self):
        return int(cook_book[2][1][1][1])
    # Творог
    def curd(self):
        return cook_book[2][1][2][0]
    def curd_weight(self):
        return int(cook_book[2][1][2][1])
    # Сахар
    def sugar(self):
        return cook_book[2][1][3][0]
    def sugar_weight(self):
        return int(cook_book[2][1][3][1])
    #🍯🍯🍯
    def honey(self):
        return cook_book[2][1][4][0]
    def honey_weight(self):
        return int(cook_book[2][1][4][1])

    def sum_weight(self, food_name, food_weight,  count_people ):
        print(f"{food_name} {food_weight * count_people}гр.")
# Конструктор
    def __init__(self, count_people):
        self.salad()
        self.pizza()
        self.fruit_dessert()

sum_people = int(input("Введите кол-во гостей: "))
chef = cooking(sum_people)