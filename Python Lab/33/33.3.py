class Fraction:
    def __init__(self, num, deno):
        self.n = num
        self.d = deno

    def set_num(self, num):
        self.n = num

    def set_deno(self, deno):
        if deno != 0:
            self.d = deno
        else:
            print("Denominator cannot be zero.")

    def get_num(self):
        return self.n

    def get_deno(self):
        return self.d

    def display(self):
        print(f"{self.n}/{self.d}")


fraction1 = Fraction(1, 4)
fraction2 = Fraction(3, 4)

fraction1.display()
fraction2.display()


fraction1.set_num(7)
fraction1.set_deno(8)
fraction1.display()
