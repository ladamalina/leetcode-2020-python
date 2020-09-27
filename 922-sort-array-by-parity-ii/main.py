import logging
from typing import Generator, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        def get_el(l: List[int], even: bool = False, odd: bool = False) -> Generator[int, None, None]:
            for i in range(len(l)):
                if even and l[i] % 2 == 0:
                    yield l[i]
                if odd and l[i] % 2 == 1:
                    yield l[i]

            return None

        gen_even = get_el(A, even=True)
        gen_odd = get_el(A, odd=True)

        next_even = next(gen_even, None)
        next_odd = next(gen_odd, None)

        res = []
        while next_even is not None and next_odd is not None:
            res.extend([next_even, next_odd])
            next_even = next(gen_even, None)
            next_odd = next(gen_odd, None)

        return res


def main():
    assert Solution().sortArrayByParityII([4,2,5,7]) == [4,5,2,7]


if __name__ == '__main__':
    main()
