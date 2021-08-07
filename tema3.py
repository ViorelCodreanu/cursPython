if __name__ == '__main__':
    class Fractie:
        def __init__(self, name, value):
            self.name = str(name)
            self.value = float(value)
n = 0
numarator = Fractie("Numarator", n)
numitor = Fractie("Numitor", n)

numarator.name = "Numarator"
numarator.value = input('type your numarator: ')
numarator.value = float(numarator.value)

numitor.name = "Numitor"
numitor.value = input('type your numitor: ')
numitor.value = float(numitor.value)


def __str__(self):
    return f'"Object Name: "{numarator.name}, {type(numarator.name)}, "Object Name: "{numitor.name}, {type(numitor.name)}, \n{float(numarator.value)} / {float(numitor.value)}'


print(__str__(1))


def div():
    division = float(numarator.value / numitor.value)
    return f'the result of your first number divided with the second is: {division:.3f}'


print(div())

# numarator2 = Fractie("Numarator2", n)
# numitor2 = Fractie("Numitor2", n)
#
# numarator2.name = "Numarator2"
# numarator2.value = input('type your numarator2: ')
# numarator2.value = float(numarator2.value)
#
# numitor2.name = "Numitor2"
# numitor2.value = input('type your numitor2: ')
# numitor2.value = float(numitor2.value)
#
#
# def __add__():
#     adunarea = (numarator.value / numitor.value) + (numarator2.value / numitor2.value)
#     return f'fractia rezultata din adunarea celor doua fractii introduse este: \n{adunarea:.3f}'
#
# print(__add__())
