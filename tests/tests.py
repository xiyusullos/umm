from src import C


def test_Mirror():
    from src.utils import Mirror
    mirror = Mirror(C.MIRRORS.get('npm'))
    print(mirror['npm'])
    mirror['npm'] = 'abc'
    print(mirror['npm'], 'npm' in mirror, 'a' in mirror)
    print(mirror)