# from pprint import pprint

ing_book = {}
cook_book = {}

f = open("Cook_Book.txt", "r", encoding="utf-8")

for line in f:
    nc = line.strip()
    num = int(f.readline().strip())
    p = []
    for i in range(num):
        ing = f.readline().split("|")
        ing_book = {"ingredient_name": ing[0], "quantity": ing[1],"measure": ing[2]}
        p.append(ing_book)
    emp_str = f.readline().strip()
    cook_book[nc] = p
# pprint(cook_book)
#
dishes = 'Запеченный картофель'

ing_book_2 = {}
ing_book_3 = {}

def get_shop_list_by_dishes(dishes, person_count=1):
        if dishes in cook_book:
            for numb in cook_book[dishes]:
                ing_book_2 = {'measure':numb['measure'],'quantity':int(numb['quantity']) * person_count}
                ing_book_3 = {numb['ingredient_name'] : ing_book_2}
                print(f"{ing_book_3}")
        else:
            print("Такого облюда нет в книге рецептов")

get_shop_list_by_dishes(dishes,3)










f.close()









