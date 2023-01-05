import pytest, test_demo as d
@pytest.mark.parametrize("n1, n2, r",[(2022, 10, 5)])
def test_call(n1, n2, r):
    if d.cal(n1, n2)==r:
        print(d.cal(n1, n2))
        return True
    else:
        return False

@pytest.mark.parametrize("Value,r",[(1,"sam")])
def test_key(Value, r):
    if d.key(Value)==r:
        return True
    else:
        return False

@pytest.mark.parametrize("l,r",[([1,2,3],[3,2,1])])
def test_desc(l, r):
    if d.desc(l)==r:
        return True
    else:
        return False
@pytest.mark.parametrize("l,r",[([1,12,30],1)])
def test_min(l, r):
    if d.minn(l)==r:
        return True
    else:
        return False
