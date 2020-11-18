cars = ['Toyota', 'Benz', 'Ferrari', 'BMW']
prices = [12_000, 15_000, 25_000, 30_000]

print(cars[0], '$',prices[0])
print(cars[1], '$',prices[1])
print(cars[2], '$',prices[2])
print(cars[3], '$',prices[3])

print('\n-----------------------------\n')

print(cars)
print(prices)
cars[2] = 'Audi'
prices[2] = 17_000
print(cars)
print(prices)

print('\n-----------------------------\n')

cars.insert(2, 'Ferrari')
print(cars)

cars.append('Luxes')
print(cars)

print(prices.reverse())