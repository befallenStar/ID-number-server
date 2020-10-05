# -*- encoding: utf-8 -*-
from operations import read


def main():
    try:
        ID = '141082199802012327'
        read(ID)
        ID = '320101199801012314'
        read(ID)
        ID = '141082190002292381'
        read(ID)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
