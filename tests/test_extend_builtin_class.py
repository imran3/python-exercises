from src.extend_builtin_class import UniqueList

def test_UniqueList_append():
    expected = [1, 2, 3]
    res = UniqueList()
    res.append(1)
    res.append(2)
    res.append(1)
    res.append(3)
    res.append(1)
    res.append(1)

    assert res == expected

def test_UniqueList_newPropertyValue():
    res = UniqueList()
    assert res.someNewProperty