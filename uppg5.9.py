text = input(str('Skriv din text: '))

a = text.replace(" ", "")
b = a[::-1]


if a == b:
    print('din text är en palyndrom')

else:
    print('din text är inte en palyndrom')
