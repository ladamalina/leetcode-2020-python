import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def rand7():
    pass


class Solution:
    def rand10(self):
        rand48 = 48;
        while rand48 >= 40:
            rand48 = (rand7() - 1) * 7 + rand7() - 1

        return rand48 % 10 + 1


def main():
    pass


if __name__ == '__main__':
    main()
