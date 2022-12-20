numbers = [1, 2, 3, 4, 5]
number_list = [item ** 2 for item in numbers if item % 2 == 0]
# print(number_list)

product_list = ['ciocolata', 'suc', 'mere', 'miere', 'apa']
new_list = [x for x in product_list if 'a' in x]
# print(new_list)

l = [x for x in range(10) if x < 5]
# print(l)

new_product_list = [x if x != 'suc' else 'apa minerala' for x in product_list]
# print(new_product_list)

a = "Ana are mere"
l2 = [e for i,e in enumerate(list(a)) if i % 2 == 0]
# print(l2)
l3 = [e if i % 2 == 0 else 'impar' for i,e in enumerate(list(a))]
# print(l3)
