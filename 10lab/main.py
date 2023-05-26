import json

def ypr1():

    with open('10lab.json','r', encoding='utf-8') as f:
        data = json.load(f)

    for product in data["products"]:
        print("Название:", product["name"])
        print("Цена:", product["price"])
        print("Вес:", product["weight"])
        if product["available"]:
            print("В наличии")
        else:
            print("Нет в наличии!")

ypr1()
def ypr2():
    with open('10lab.json','r', encoding='utf-8') as f:
        data = json.load(f)

    new_product = {}
    new_product['name'] = input('Введите название товара: ')
    new_product['price'] = int(input('Введите цену товара: '))
    new_product['weight'] = int(input('Введите вес товара: '))
    new_product['available'] = bool(input('Есть ли товар в наличии (True/False): '))

    data['products'].append(new_product)

    with open('10lab.json', 'w') as f:
        json.dump(data, f)

    for product in data['products']:
        print('Название:', product['name'])
        print('Цена:', product['price'])
        print('Вес:', product['weight'])
        if product['available']:
            print('В наличии')
        else:
            print('Нет в наличии!')

ypr2()

def ypr3():
    ru_en = {}

    with open('en-ru.txt', 'r', encoding='utf-8') as f:
        for line in f:
            p = line.strip().split('-')
            if len(p) == 2:
                en_word = p[0].strip()
                ru_words = p[1].strip().split(', ')
                for i in ru_words:
                    if i in ru_en:
                        ru_en[i].append(en_word)
                    else:
                        ru_en[i] = [en_word]

    with open('ru-en.txt', 'w') as f:
        for i, en_word in ru_en.items():
            f.write(f"{i} - {en_word}\n")
ypr3()