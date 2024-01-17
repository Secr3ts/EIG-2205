premier = True;
p = input("Entrez un nombre: ");
p = int(p);
i = 2;
for i in range(2, p):
    if p % i == 0:
        premier = False;
        break;

if not premier:
    print(f'{str(p)} = {str(i)} * {str(p // i)} : False');
else:
    print(f'{str(p)} : True');