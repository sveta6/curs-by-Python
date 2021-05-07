base = []
def hello(temp):
    print("Здравствуйте, ", temp, "! Вашу карту ищут...", sep="")


def search_card(temp):
    if temp in base:
        print("Ваша карта с номером ", base.index(temp) + 1, " найдена", sep="")
    else:
        print("Ваша карта не найдена")

