class Fib:
    def __init__(self, number):
        self.number = number

    def series(self, a=0, b=1, count=1):
        data = a+b
        print(data)
        if count >= self.number:
            return
        count += 1
        self.series(b, data, count)


Fib(10).series()



