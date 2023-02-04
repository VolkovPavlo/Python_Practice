# shop_list = 'milk, bread, wine, beer'
# print(shop_list)

# check_list = ['shop', 'carwash', 'barbershop']
# print(check_list[2])
# print(check_list[0:2])
# len(check_list)
# print(len(check_list))
# print(type(check_list))
# check_list = check_list + ['beershop']
# check_list = check_list+[100]
# print(check_list)
# print( 100 in check_list)
#print([1, 2, 3]+[4, 5, 6])

# nums = (1, 2, 3, 4, 50)
# print(type(nums))
# print(nums[2])
# info = {'name' : 'Pavlo', 'surname' : 'Volkov', 'salary' : 1500}
# print(info['name'])
# del info['surname']
# print(info)
# info['salary'] = 2000
# print(info)

games = ['football', 'xbox']
foods = ['beer', 'meat']
favorites = (games + foods)
print(favorites)

name = 'Pavlo'
surname = 'Volkov'
text = 'Hello, %s %s'
print(text % (name, surname))

home = 25 * 3
tonnel = 40 * 2
sum = home + tonnel 
print(sum)