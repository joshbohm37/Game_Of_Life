import random

from config import screen_w, screen_h, grid_size, grid_padding, cell_size, global_center, grid_top_left
from cell import Cell


def gen_grid(size):
    grid = []

    for row in range(size):
        tmp_row = []

        for col in range(size):
            # tmp_row.append(random.choices([0, 1], [3, 1])[0])
            tmp_row.append(0)

        grid.append(tmp_row)

    return grid


def gen_grid_sprites(size, grid, sprite_group):
    padding = grid_padding
    grid_w = ((grid_size - 1) * (cell_size + padding)) + cell_size
    center = global_center
    top_left = ((center[0] - (grid_w/2)), (center[1] - (grid_w/2)))



    for row in range(size):
        for col in range(size):
            position = (
                top_left[0] + ((cell_size + padding) * col),
                top_left[1] + ((cell_size + padding) * row)
            )

            cell = Cell(start_pos = position, state = grid[row][col], cell_size = cell_size)
            sprite_group.add(cell)


def validate_neighbors(grid, size, cell_row, cell_col):
    valid_neighbors = []
    for row in [-1, 0, 1]:
        for col in [-1, 0 , 1]:
            neighbor_col = cell_col + col
            neighbor_row = cell_row + row


            valid = True

            if neighbor_col < 0 or neighbor_col >= size or neighbor_row < 0 or neighbor_row >= size or (cell_row == neighbor_row and cell_col == neighbor_col):
                valid = False

            if valid:
                valid_neighbors.append(grid[neighbor_row][neighbor_col])

    return sum(valid_neighbors)


def update_grid(start_grd):
    new_grid = []
    for row in range(len(start_grd)):
        tmp_row = []
        for col in range(len(start_grd[row])):
            score = validate_neighbors(start_grd, grid_size, row, col)

            if not start_grd[row][col]:
                if score == 3:
                    tmp_row.append(1)
                else:
                    tmp_row.append(0)

            else:
                if score < 2:
                    tmp_row.append(0)
                if score > 3:
                    tmp_row.append(0)
                if score == 2 or score == 3:
                    tmp_row.append(1)

        new_grid.append(tmp_row)

    return  new_grid

