import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        logger.debug('-' * 40)
        logger.debug(f'{version1=}, {version2=}')
        v1_tuple = tuple(int(_) for _ in version1.split('.'))
        v2_tuple = tuple(int(_) for _ in version2.split('.'))
        logger.debug(f'{v1_tuple=}, {v2_tuple=}')
        if v1_tuple == v2_tuple:
            return 0

        len_diff = abs(len(v1_tuple) - len(v2_tuple))
        if len_diff:
            shortest_v_tuple = v1_tuple if len(v1_tuple) < len(v2_tuple) else v2_tuple
            extended_v_tuple = tuple(list(shortest_v_tuple) + [0 for _ in range(len_diff)])
            if shortest_v_tuple is v1_tuple:
                v1_tuple = extended_v_tuple
            else:
                v2_tuple = extended_v_tuple
        logger.debug(f'{v1_tuple=}, {v2_tuple=}')

        for i, v1 in enumerate(v1_tuple):
            if v1 > v2_tuple[i]:
                logger.debug('Return 1')
                return 1
            if v1 < v2_tuple[i]:
                logger.debug('Return -1')
                return -1

        logger.debug('Return 0')
        return 0


def main():
    assert Solution().compareVersion("0.1", "1.1") == -1
    assert Solution().compareVersion("1.0.1", "1") == 1
    assert Solution().compareVersion("7.5.2.4", "7.5.3") == -1
    assert Solution().compareVersion("1.01", "1.001") == 0
    assert Solution().compareVersion("1.0", "1.0.0") == 0


if __name__ == '__main__':
    main()
