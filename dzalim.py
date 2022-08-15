class Fraction:
    def __init__(self,numertor,denumerator,numertor1,denumerator1):
        self.numertor = numertor
        self.denumerator = denumerator
        self.numertor1 = numertor1
        self.denumerator1 = denumerator1


    def add(self):
        add_numertor = self.numertor * self.denumerator1 + self.numertor1 * self.denumerator
        add_denumerator = self.denumerator * self.denumerator1
        print("Сумма", add_numertor, "/", add_denumerator)
        return (add_numertor, add_denumerator)

    def sub(self):
        sub_numertor = self.numertor * self.denumerator1 - self.numertor1 * self.denumerator
        sub_denumerator = self.denumerator * self.denumerator1
        print("разность", sub_numertor, "/", sub_denumerator)
        return (sub_numertor, sub_denumerator)


    def mul(self):
        mul_numertor = self.numertor * self.numertor1
        mul_denumerator = self.denumerator * self.denumerator1
        print("Произвдение равно: ", mul_numertor, "/", mul_denumerator)
        return (mul_numertor, mul_denumerator)


    def div(self):
        div_numerator = self.numertor * self.denumerator1
        div_denumerator = self.denumerator * self.numertor1
        print("Частное равно: ", div_numerator, "/", div_denumerator)
        return (div_numerator, div_denumerator)



object= Fraction(int(input("значение числителя первой дроби: ")),
                int(input("значение знаменателя первой дроби: ")),
                int(input("значение числителя второй дроби: ")),
                int(input("значение знаменателя второй дроби: ")))
object.add()
object.sub()
object.div()
object.mul()
