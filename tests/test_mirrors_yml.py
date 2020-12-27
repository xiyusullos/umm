import C


def test_mirrors_yaml():
    assert 'pip' in C.MIRRORS
    assert 'npm' in C.MIRRORS
    assert 'composer' in C.MIRRORS
    assert 'brew' in C.MIRRORS
