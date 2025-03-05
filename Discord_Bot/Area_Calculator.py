print('Area Calculator\n')
print('1) Square')
print('2) Rectangle')
print('3) Triangle')
print('4) Circle')

menu_input = int(input('\nWhich shape (1-4): '))

if menu_input == 1:
  side = int(input('Side length: '))
  area = side ** 2
  print(f'The area is: {area}')
elif menu_input == 2:
  length = int(input('Length: '))
  width = int(input('Width: '))
  area = length * width
  print(f'The area is: {area}')
elif menu_input == 3:
  height = int(input('Height:'))
  base = int(input('Base:'))
  area = (height * base) / 2
  print(f'The area is: {area}')
elif menu_input == 4:
  radius = int(input('Radius:'))
  area = 3.14 * (radius ** 2)
  print(f'The area is: {area}')
else:
  print('Invalid input.')
