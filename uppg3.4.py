temp = float(input('Vad är tempen: '))


if temp < 20:
    print('Det är lite kyligt')
elif temp < 18:
    print('Det är kallt!')
    print('Sätt på värmen')
elif temp < 12:
    print('Det är riktigt kallt!')
    print('Elda och ta på dig jackan')
elif temp < 7:
    print('Det är ju fan antarktis här inte')
    print('Elda då ditt skräll')
elif temp > 24:
    print('Nu är det för varm här inne')
    print('Det behövs inte elsas mer nu')
elif temp > 30:
    print('det är bastu här inne')
    print('Öppna ett fönster!')
else:
    print('Nu är det lagom varmt här inne')