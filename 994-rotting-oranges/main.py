import copy
import json
import logging
from typing import Dict, List, Set, Tuple

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        logger.debug("*" * 80)
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        fresh_count = 0
        minutes_elapsed = 0
        rotten_cells_having_fresh_neighbors: Dict[Tuple[int, int], List[Tuple[int, int]]] = dict()

        def get_fresh_neighbors(i: int, j: int, grid: List[List[int]]) -> List[Tuple[int, int]]:
            fresh_neighbors = []
            if i - 1 >= 0 and grid[i - 1][j] == FRESH:
                fresh_neighbors.append(tuple([i - 1, j]))
            if j + 1 < len(grid[0]) and grid[i][j + 1] == FRESH:
                fresh_neighbors.append(tuple([i, j + 1]))
            if i + 1 < len(grid) and grid[i + 1][j] == FRESH:
                fresh_neighbors.append(tuple([i + 1, j]))
            if j - 1 >= 0 and grid[i][j - 1] == FRESH:
                fresh_neighbors.append(tuple([i, j - 1]))

            return fresh_neighbors

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == FRESH:
                    fresh_count += 1
                    continue
                fresh_neighbors = get_fresh_neighbors(i, j, grid)
                if grid[i][j] == ROTTEN and fresh_neighbors:
                    rotten_cells_having_fresh_neighbors[tuple([i, j])] = fresh_neighbors
                    continue

        seen_grids: Set[str] = set()
        seen_grids.add(json.dumps(grid))

        current_grid = copy.deepcopy(grid)

        while fresh_count > 0:
            minutes_elapsed += 1
            logger.debug("-" * 40)
            logger.debug(f"{minutes_elapsed=}, {fresh_count=}")
            for row in current_grid:
                logger.debug(f"curr {row=}")
            logger.debug(f"{rotten_cells_having_fresh_neighbors=}")
            next_grid = copy.deepcopy(current_grid)
            just_rottened_cells: List[Tuple[int, int]] = []
            rotten_cells_to_check = list(rotten_cells_having_fresh_neighbors.keys())
            for rotten_cell in rotten_cells_to_check:
                for fresh_cell in rotten_cells_having_fresh_neighbors[rotten_cell]:
                    if next_grid[fresh_cell[0]][fresh_cell[1]] == FRESH:
                        next_grid[fresh_cell[0]][fresh_cell[1]] = ROTTEN
                        just_rottened_cells.append(fresh_cell)
                        fresh_count -= 1
                del rotten_cells_having_fresh_neighbors[rotten_cell]
            for row in next_grid:
                logger.debug(f"next {row=}")
            logger.debug(f"{just_rottened_cells=}")
            for just_rottened_cell in just_rottened_cells:
                fresh_neighbors = get_fresh_neighbors(just_rottened_cell[0], just_rottened_cell[1], next_grid)
                if fresh_neighbors:
                    rotten_cells_having_fresh_neighbors[just_rottened_cell] = fresh_neighbors

            grid_fingerprint = json.dumps(next_grid)
            if grid_fingerprint in seen_grids:
                return -1
            seen_grids.add(json.dumps(next_grid))

            current_grid = copy.deepcopy(next_grid)

        logger.debug(f"return {minutes_elapsed=}")

        return minutes_elapsed


def main():
    assert Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert Solution().orangesRotting([[0,2]]) == 0
    assert Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1


if __name__ == '__main__':
    main()
