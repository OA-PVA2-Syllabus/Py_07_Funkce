import reseni

#1
def test_hello(capfd):
    reseni.hello()
    out, err = capfd.readouterr()
    assert out == "Hello world\n"

#3
def test_showHello(capfd):
    reseni.showHello(3)
    out, err = capfd.readouterr()
    assert out == "Hello world\nHello world\nHello world\n"

def test_square():
    assert reseni.square(3) == 3**2
    assert reseni.square(10) == 10 ** 2

#5
def test_sumOfTwo():
    assert reseni.sumOfTwo(2,4) == 6

#6
def test_multiply():
    assert reseni.multiply(3,5,20) == 35
    assert reseni.multiply(3,5) == 25
    assert reseni.multiply(3) == 16

#7
def test_faktorial():
    assert reseni.faktorial(5) == 120