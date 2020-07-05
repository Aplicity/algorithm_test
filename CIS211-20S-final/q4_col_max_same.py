"""All columns same max. Spring 2020 final exam problem.
For full credit, this must be solved without
creating new lists. Partial credit for solutions
that create new lists.

You may optionally write additional methods
or functions to break the problem down.
"""

from typing import List

class Grid(object):
    def __init__(self, grid_values: List[List[int]]):
        self._gv = grid_values

    def all_columns_same_max(self) -> bool:
        n_row = len(self._gv)
        try:
            n_col = len(self._gv[0])
            if n_col == 1:
                return True

            else:
                max_value = max([max(L) for L in self._gv])
                n_true = 0
                for j in range(n_col):
                    col_item = []
                    for i in range(n_row):
                        col_item.append(self._gv[i][j])
                        print(col_item)
                    if max(col_item) == max_value:
                        n_true += 1
                if n_true == n_col:
                    return True
                else:
                    return False


        except:
            flag = True

        return True  # FIXME

