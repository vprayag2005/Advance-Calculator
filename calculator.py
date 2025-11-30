class Calculator:
    def __init__(self):
        self.result = None

    def continue_result(self):
        if self.result is not None:
            ch = input("Do you want to calculate with previous Result? (y or n) : ").lower()
            if ch not in ["y", "n"]:
                raise ValueError("Input must be 'y' or 'n'")
            return  ch
        return "n"

    def use_any_function(self):
        print()
        print("1. Square Root")
        print("2. factorial")
        print("3. Power")
        print("4. Simple Interest")
        print("5. Compount interest")
        print("6. N_th Root")
        print("7. compute_log_base_a_of_b")
        print("8. compute sine degree")

        ch = input("Do you want use any of these function (y or n) : ").lower()
        if ch not in ["y", "n"]:
            raise ValueError("Input must be 'y' or 'n'")

        if ch == "y":
            choice = int(input("Choose the option below :"))
            if choice == 1:
                ans = self.find_square_root(input_need=False)
            elif choice == 2:
                ans = self.find_factorial(input_need=False)
            elif choice == 3:
                ans = self.find_power(input_need=False)
            elif choice == 4:
                ans = self.calculate_simple_interest()
            elif choice == 5:
                ans = self.calculate_compound_interest()
            elif choice == 6:
                ans = self.find_n_th_root(input_need=False)
            elif choice == 7:
                ans = self.compute_log_base_a_of_b(input_need=False)
            elif choice == 8:
                ans = self.calculate_sine(input_need=False)
            else:
                raise ValueError("Invalid input")

            return ans
        else:
            return ch

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        try:
            return num1 / num2
            
        except ZeroDivisionError:
            print("Division by Zero not possible")

    def find_square_root(self, num = None, input_need = True):
        num = float(input("Enter the number :")) if num is None else num

        # Heron algorithm
        guess = num/2
        accuracy = 0.0001
        while True:
            new_guess = (guess + (num / guess)) / 2
            if abs(guess - new_guess) < accuracy:
                return (num, new_guess) if input_need else new_guess

            guess = new_guess

    def find_factorial(self, num = None, input_need = True):
        if num is None:
            num = int(input("Enter the number :"))
        fact = 1
        for i in range(1, num+1):
            fact = fact*i
        return (num, fact) if input_need else fact

    def find_power(self, base = None, exp = None, input_need = True):
        if base is None and exp is None:
            base = float(input("Enter the base :"))
            exp = float(input("Enter the exponent :"))

        power = base
        for i in range(2, int(abs(exp)+1)):
            power = power * base
            
        if exp > 0:
            return (base, exp, power) if input_need else power
    
        return (base, exp, 1/power) if input_need else 1/power

    def calculate_simple_interest(self, principal=None, rate=None, time=None):
        if principal is None and rate is None and time is None:
            principal = float(input("Enter Principal Amount  :"))
            rate = float(input("Enter the Rate  :"))
            time = float(input("Enter the time  :"))

        return (principal * rate * time)/100

    def calculate_compound_interest(self, principal=None, rate=None, time=None, periods=None):
        if principal is None and rate is None and time is None and periods is None:
            principal = float(input("Enter Principal Amount  :"))
            rate = float(input("Enter the Rate  :"))
            time = float(input("Enter the time  :"))
            periods = float(input("Enter the Periods  :"))
        amount = principal * self.find_power((1 + (rate / periods)), time * periods, input_need=False)
        interest = amount - principal
        return interest

    def find_n_th_root(self, num=None, exp=None, input_need = True):
        # Newton Raphson Method
        if num is None and exp is None:
            num = int(input("Enter the base :"))
            exp = int(input("Enter the exponent :"))

        accuracy = 0.0001
        guess = num/exp
        while True:
            #f(x)
            fx = (self.find_power(guess, exp))[2] - num
            #f`(x)
            f_x = exp * self.find_power(guess, exp - 1)[2]
            new_guess = guess - (fx / f_x)

            if abs(guess - new_guess) < accuracy:
                return (num, exp, new_guess) if input_need else new_guess

            guess = new_guess

    def compute_log_base_a_of_b(self, num=None, base=None, input_need = True):
        # https://math.stackexchange.com/questions/635787/how-to-calculate-lnx
        if num is None and base is None:
            num = int(input("Enter the Number :"))
            base = int(input("Enter the base :"))
        if num < 1 or  base <= 1:
            raise ValueError("Number must be >= 1 and base must be > 1.")

        digits = []
        n = num
        for i in range(3):
            count = 0

            if i != 0:
                n = self.find_power(n, 10)[2]

            while n >= base:
                count += 1
                n /= base
            digits.append(count)

        return (num, base, (digits[0] + digits[1]/10 + digits[2]/100)) if input_need \
            else (digits[0] + digits[1]/10 + digits[2]/100)

    def calculate_sine(self, degree=None, input_need = True):
        # https://math.stackexchange.com/questions/1254713/maclaurin-series-approximation-of-sinx
        if degree is  None:
            degree = int(input("Enter the degree :"))
        radian = degree * (3.141592653589793/180)
        _sum = 0
        sign = 1

        for i in range(1, 21, 2):
            _sum += sign * (self.find_power(radian, i)[2]) / (self.find_factorial(i)[1])
            sign = -sign

        return (degree, _sum) if input_need else _sum

    def run_loop(self):
        while True:
            print("Menu")
            print("1. Addition")
            print("2. Substration")
            print("3. Multiplication")
            print("4. Division")
            print("5. Square Root")
            print("6. factorial")
            print("7. Power")
            print("8. Simple Interest")
            print("9. Compount interest")
            print("10. N_th Root")
            print("11. compute_log_base_a_of_b")
            print("12. compute sine degree")
            print("13. Exit")
            choice = int(input("Choose the option below :"))

            if choice == 1:
                ch = self.continue_result()
                if ch == "y":
                    func_choice_result = self.use_any_function()
                    num2 = float(input("Enter the  Number :")) if func_choice_result == "n" else func_choice_result
                    _sum  = self.add(self.result, num2)
                    print(f"{self.result} + {num2} = {_sum}")
                else:
                    func_choice_result = self.use_any_function()
                    num1 = float(input("Enter the  Number :")) if func_choice_result == "n" else func_choice_result
                    func_choice_result = self.use_any_function()
                    num2 = float(input("Enter the  Number :")) if func_choice_result == "n" else func_choice_result
                    _sum = self.add(num1, num2)
                    print(f"{num1} + {num2} = {self.add(num1, num2)}")

                self.result = _sum
            elif choice == 2:
                ch = self.continue_result()
                if ch == "y":
                    func_choice_result = self.use_any_function()
                    num2 = float(input("Enter the  Number :")) if func_choice_result == "n" else func_choice_result
                    diff = self.sub(self.result, num2)
                    print(f"{self.result} - {num2} = {diff}")
                else:
                    func_choice_result = self.use_any_function()
                    num1 = float(input("Enter the  Number :")) if func_choice_result == "n" else func_choice_result
                    func_choice_result = self.use_any_function()
                    num2 = float(input("Enter the  Number :")) if func_choice_result == "n" else func_choice_result
                    diff = self.sub(num1, num2)
                    print(f"{num1} - {num2} = {diff}")

                self.result = diff
            elif choice == 3:
                ch = self.continue_result()
                if ch == "y":
                    func_choice_result = self.use_any_function()
                    num2 = float(input("Enter the  Number :")) if func_choice_result == "n" else func_choice_result
                    multi = self.mul(self.result, num2)
                    print(f"{self.result} * {num2} = {multi}")
                else:
                    func_choice_result = self.use_any_function()
                    num1 = float(input("Enter the  Number :")) if func_choice_result == "n" else func_choice_result
                    func_choice_result = self.use_any_function()
                    num2 = float(input("Enter the  Number :")) if func_choice_result == "n" else func_choice_result
                    multi = self.mul(num1, num2)
                    print(f"{num1} * {num2} = {multi}")

                self.result = multi
            elif choice == 4:
                ch = self.continue_result()
                if ch == "y":
                    func_choice_result = self.use_any_function()
                    num2 = float(input("Enter the  Number :")) if func_choice_result == "n" else func_choice_result
                    divi = self.div(self.result, num2)
                    if divi:
                        print(f"{self.result} / {num2} = {divi}")
                else:
                    func_choice_result = self.use_any_function()
                    num1 = float(input("Enter the  Number :")) if func_choice_result == "n" else func_choice_result
                    func_choice_result = self.use_any_function()
                    num2 = float(input("Enter the  Number :")) if func_choice_result == "n" else func_choice_result
                    divi = self.div(num1, num2)
                    if divi:
                        print(f"{num1} / {num2} = {divi}")

                self.result = divi
            elif choice == 5:
                num, ans = self.find_square_root()
                print(f"sqrt_root({num}) = {ans}")
            elif choice == 6:
                num, ans = self.find_factorial()
                print(f"{num}! = {ans}")
            elif choice == 7:
                base, exp, ans = self.find_power()
                print(f"{base}^{exp} = {ans}")
            elif choice == 8:
                ans = self.calculate_simple_interest()
                print(f"simple interest = {ans}")
            elif choice == 9:
                ans = self.calculate_compound_interest()
                print(f"Compount interest = {ans}")
            elif choice == 10:
                base, exp, ans = self.find_n_th_root()
                print(f"{base}^{exp} = {ans}")
            elif choice == 11:
                num, base, ans = self.compute_log_base_a_of_b()
                print(f"log{base}({num}) = {ans}")
            elif choice == 12:
                deg, ans = self.calculate_sine()
                print(f"sin({deg}) = {ans}")
            elif choice == 13:
                break
            else:
                print("Invalid input")

            print()

if __name__ == "__main__":
    calc = Calculator()
    calc.run_loop()
