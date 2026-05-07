from functions2 import hello

def test_argument():
    for name in ["Brian", "Mugai", "Nyaga"]:
        assert hello(name) == f"hello, {name}"
    
def test_default():
    assert hello() == "hello, world"