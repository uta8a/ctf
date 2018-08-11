def _rot(_num, _chr):
    if 'A' <= _chr and _chr <= 'Z':
        return chr((ord(_chr) - ord('A') + _num) % 26 + ord('A'))

    if 'a' <= _chr and _chr <= 'z':
        return chr((ord(_chr) - ord('a') + _num) % 26 + ord('a'))

    return _chr


class ROT:
    def __init__(self):
        pass
    def rot(_num, _str):
        g = (_rot(_num, c) for c in _str)
        return ''.join(g)
    
    # rot全列挙スクリプト