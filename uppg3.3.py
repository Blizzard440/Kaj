poäng = int(input('Antal poäng på ditt prov: '))

# e = 25-29
# d = 30-34
# c = 35-39
# b = 40-44
# a = 45-50


if poäng > 50:
    print('För högt input')
elif poäng >= 45:
    print('Betyg A')
elif poäng >= 40:
    print('Betyg B')
elif poäng >= 35:
    print('Betyg C')
elif poäng >= 30:
    print('Betyg D')
elif poäng >= 25:
    print('Betyg E')
else:
    print('Du fick tyvärr underkänt')


# if poäng >= 25:
#     if poäng >= 30:
#         if poäng >= 35:
#             if poäng >= 40:
#                 if poäng >= 45:
#                     print('Betyg A')
#                 else:
#                     print('Betyg B')
#             else:
#                 print('Betyg C')
#         else:
#             print('Betyg D')
#     else:
#         print('Betyg E')
# else:
#     print('Betyg F')