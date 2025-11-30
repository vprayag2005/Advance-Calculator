from calculator import Calculator

calc = Calculator()

def test_addition():
    result = calc.add(10, 90)
    assert result == 100


def test_subtraction():
    result = calc.sub(100, 90)
    assert result == 10

def test_multiplication():
    result = calc.mul(7, 3)
    assert result == 21


def test_division():
    result = calc.div(10, 2)
    assert result == 5

    result = calc.div(10, 0)
    assert result is None


def test_square():
    result = calc.find_square_root(49, input_need=False)
    assert result == 7.0


def test_factorial():
    result = calc.find_factorial(5, input_need=False)
    assert result == 120


def test_power():
    result = calc.find_power(base = 2, exp = 4, input_need=False)
    assert result == 16


def test_simple_interest():
    result = calc.calculate_simple_interest(10000, 4, 1)
    assert result == 400


def test_compound_interest():
    result = calc.calculate_compound_interest(3000, 0.1, 2, 2)
    expected = 646.51875
    assert abs(result - expected) < 1e-6


def test_n_th_root():
    result = calc.find_n_th_root(27, 3, input_need=False)
    expected = 3
    assert abs(result - expected) < 1e-6


def test__log_base_a_of_b():
    result = calc.compute_log_base_a_of_b(num=7, base=3, input_need=False)
    expected = 1.77
    assert result == expected


def test_sine():
    result = calc.calculate_sine(90, input_need=False)
    assert result == 1.0