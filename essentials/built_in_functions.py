un_enetro = int("21")
print(un_enetro)
print(type(un_enetro))

print(bool("a"))
print(bool(""))
un_numero = 21
print(type(un_numero))
un_numero = float(un_numero)
print(type(un_numero))


def x(nombre):
    def x(a): return a + 10
    print(x(5))
    return "ed" + nombre


print(x('d Colón'))
