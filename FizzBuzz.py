class FizzBuzz:
    def printFizzBuzz(self, count):
        for i in range(1, count + 1):
            msg = ""
            if i % 3 == 0:
                msg += "Fizz"
            if i % 5 == 0:
                msg += "Buzz"
            elif len(msg) == 0:
                msg = str(i)
            print(msg)

fizzbuzz = FizzBuzz()
fizzbuzz.printFizzBuzz(100)
