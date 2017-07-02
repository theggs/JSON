import json

from loads import loads
from dumps import dumps
from examples.examples import examples


def test_dumps():
    print('TEST FOR DUMPS:')
    for i, eg in enumerate(examples, 1):
        a = dumps(eg)
        b = json.dumps(eg)
        print(i, a == b)


def test_loads():
    print('TEST FOR LOADS:')
    for i in range(1, 7):
        with open('examples/example{}.txt'.format(i), 'r', encoding='utf-8') as f:
            data = f.read()
        a = loads(data)
        b = json.loads(data)
        print(i, a == b)


if __name__ == '__main__':
    # output()
    test_dumps()
    print('\n')
    test_loads()
