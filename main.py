import pygame

# Global VARs
DARK_GREY = (27, 27, 27)
WHITE = (255, 255, 255)
LIGHT_GREY = (181, 181, 181)
GREEN = (119, 186, 144)

GRID_WIDTH = 20
GRID_HEIGHT = 20
MARGIN = 5

WINDOW_SIZE = (800, 355)


def make_grid():
    grid = []
    for y in range(14):
        grid.append([])
        for x in range(8):
            if y in (0, 13):
                if 3 <= x <= 4:
                    grid[y].append(0)
                else:
                    grid[y].append('')
            if y in (1, 12):
                if 2 <= x <= 5:
                    grid[y].append(0)
                else:
                    grid[y].append('')
            if y in (2, 11):
                if 1 <= x <= 6:
                    grid[y].append(0)
                else:
                    grid[y].append('')
            if y in (3, 6, 7, 10):
                grid[y].append(0)
            if y == 4:
                if 2 <= x <= 5:
                    grid[y].append(2)
                else:
                    grid[y].append(0)
            if y == 5:
                if 3 <= x <= 4:
                    grid[y].append(2)
                else:
                    grid[y].append(0)
            if y == 8:
                if 3 <= x <= 4:
                    grid[y].append(1)
                else:
                    grid[y].append(0)
            if y == 9:
                if 2 <= x <= 5:
                    grid[y].append(1)
                else:
                    grid[y].append(0)

    return grid


def draw_grid(grid, screen):
    for y in range(14):
        for x in range(8):
            color = DARK_GREY
            if grid[y][x] == 0:
                color = LIGHT_GREY
            if grid[y][x] == 2:
                color = GREEN
            elif grid[y][x] == 1:
                color = WHITE
            pygame.draw.rect(screen, color, [(MARGIN + GRID_WIDTH) * x + MARGIN,
                                             (MARGIN + GRID_HEIGHT) * y + MARGIN,
                                             GRID_WIDTH, GRID_HEIGHT])


def get_mouse_pos():
    pos = pygame.mouse.get_pos()
    column = pos[0] // (GRID_WIDTH + MARGIN)
    row = pos[1] // (GRID_HEIGHT + MARGIN)
    return pos, column, row


def is_winning(grid):
    if (grid[0][3] == 1 and grid[0][4] == 1) or (grid[13][3] == 2 and grid[13][4] == 2):
        return True


def is_legal(grid_pos, selected_row, selected_column):
    if (grid_pos[2]-1 != -1 or grid_pos[2]+1 != 14) and (grid_pos[1]-1 != -1 or grid_pos[1]+1 != 8):
        if (grid_pos[2]-1 <= selected_row <= grid_pos[2]+1) and \
         (grid_pos[1]-1 <= selected_column <= grid_pos[1]+1):
            print("true")
            return True
        else:
            print("false")


def is_canter(grid, grid_pos, selected_row, selected_column):
    if grid_pos[2]-2 <= selected_row <= grid_pos[2]+2 and grid_pos[1] == selected_column:
        if grid_pos[2]+1 > 13:
            if grid[grid_pos[2]-1][grid_pos[1]] == 1:
                return True
        elif grid_pos[2]-1 < 0:
            if grid[grid_pos[2]+1][grid_pos[1]] == 1:
                return True
        elif (grid[grid_pos[2]+1][grid_pos[1]] == 1) or (grid[grid_pos[2]-1][grid_pos[1]] == 1):
            return True
    elif grid_pos[1]-2 <= selected_column <= grid_pos[1]+2 and grid_pos[2] == selected_row:
        if grid_pos[1]+1 > 7:
            if grid[grid_pos[2]][grid_pos[1]-1] == 1:
                return True
        elif grid_pos[1]-1 < 0:
            if grid[grid_pos[2]][grid_pos[1]+1] == 1:
                return True
        else:
            if (grid[grid_pos[2]][grid_pos[1]+1] == 1) or (grid[grid_pos[2]][grid_pos[1]-1] == 1):
                return True


def is_capturing(grid, grid_pos, selected_row, selected_column):
    if grid_pos[2]-2 <= selected_row <= grid_pos[2]+2 and grid_pos[1] == selected_column:
        if grid_pos[2]+1 > 13:
            if grid[grid_pos[2]-1][grid_pos[1]] == 2:
                return True
        elif grid_pos[2]-1 < 0:
            if grid[grid_pos[2]+1][grid_pos[1]] == 2:
                return True
        elif (grid[grid_pos[2]+1][grid_pos[1]] == 2) or (grid[grid_pos[2]-1][grid_pos[1]] == 2):
            return True
    elif grid_pos[1]-2 <= selected_column <= grid_pos[1]+2 and grid_pos[2] == selected_row:
        if grid_pos[1]+1 > 7:
            if grid[grid_pos[2]][grid_pos[1]-1] == 2:
                return True
        elif grid_pos[1]-1 < 0:
            if grid[grid_pos[2]][grid_pos[1]+1] == 2:
                return True
        else:
            if (grid[grid_pos[2]][grid_pos[1]+1] == 2) or (grid[grid_pos[2]][grid_pos[1]-1] == 2):
                return True


# Alpha-Beta Search
# def a_b_search(grid, depth):
#
#     def max_val(grid, alpha, beta, depth, count_max_prune, count_min_prune):
#         v = -1000
#         for actions in is_available(grid):
#             v = max(v, min_val(result_of(actions, grid), alpha, beta, depth+1, count_min_prune, count_max_prune))
#             depth += 1
#             if v >= beta:
#                 count_max_prune += 1
#                 return v
#         return v
#
#     def min_val(grid, alpha, beta, depth, count_min_prune, count_max_prune):
#         v = 1000
#         for actions in is_available(grid):
#             v = max(v, max_val(result_of(actions, grid), alpha, beta, depth+1, count_max_prune, count_min_prune))
#             depth += 1
#             if v <= alpha:
#                 count_min_prune += 1
#                 return v
#         return v
#
#     best_score = -1000
#     beta = -1000
#     for actions in is_available(grid):
#         v = min_val(result_of(actions, grid), best_score, beta, 1, 0, 0)
#         if v > best_score:
#         best_score = v
#         best_action = actions
#
#     return best_action, count_max_prune, count_min_prune, depth


# Main function to start game
def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Mini Camelot")
    grid = make_grid()
    done = False
    clock = pygame.time.Clock()
    selected_row = -1
    selected_column = -1

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or is_winning(grid):
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                grid_pos = get_mouse_pos()
                if grid_pos[1] > 7 or grid_pos[2] > 13:
                    continue
                else:
                    if grid[grid_pos[2]][grid_pos[1]] == 1 or grid[grid_pos[2]][grid_pos[1]] == 0:
                        print("Row:", grid_pos[2], ", Column:", grid_pos[1], ", Value:", grid[grid_pos[2]][grid_pos[1]])
                        if 0 <= selected_row <= 13 and 0 <= selected_column <= 7:
                            if grid[grid_pos[2]][grid_pos[1]] == 0:
                                if is_legal(grid_pos, selected_row, selected_column) or is_canter(grid, grid_pos, selected_row, selected_column):
                                    grid[grid_pos[2]][grid_pos[1]] = 1
                                    grid[selected_row][selected_column] = 0
                                    selected_row = -1
                                    selected_column = -1
                                elif is_capturing(grid, grid_pos, selected_row, selected_column):
                                    if grid_pos[2] - 2 <= selected_row <= grid_pos[2] + 2 and grid_pos[1] == selected_column:
                                        if grid_pos[2] + 1 > 13:
                                            if grid[grid_pos[2] - 1][grid_pos[1]] == 2:
                                                grid[grid_pos[2] - 1][grid_pos[1]] = 0
                                        elif grid_pos[2] - 1 < 0:
                                            if grid[grid_pos[2] + 1][grid_pos[1]] == 2:
                                                grid[grid_pos[2] + 1][grid_pos[1]] = 0
                                        else:
                                            if grid[grid_pos[2] - 1][grid_pos[1]] == 2:
                                                grid[grid_pos[2] - 1][grid_pos[1]] = 0
                                            elif grid[grid_pos[2] + 1][grid_pos[1]] == 2:
                                                grid[grid_pos[2]+1][grid_pos[1]] = 0
                                    elif grid_pos[1] - 2 <= selected_column <= grid_pos[1] + 2 and grid_pos[2] == selected_row:
                                        if grid_pos[1] + 1 > 7:
                                            if grid[grid_pos[2]][grid_pos[1] - 1] == 2:
                                                grid[grid_pos[2]][grid_pos[1]-1] = 0
                                        elif grid_pos[1] - 1 < 0:
                                            if grid[grid_pos[2]][grid_pos[1] + 1] == 2:
                                                grid[grid_pos[2]][grid_pos[1]+1] = 0
                                        else:
                                            if grid[grid_pos[2]][grid_pos[1]-1] == 2:
                                                grid[grid_pos[2]][grid_pos[1]-1] = 0
                                            elif grid[grid_pos[2]][grid_pos[1]+1] == 2:
                                                grid[grid_pos[2]][grid_pos[1]+1] = 0

                                    grid[grid_pos[2]][grid_pos[1]] = 1
                                    grid[selected_row][selected_column] = 0
                                    selected_row = -1
                                    selected_column = -1
                                else:
                                    continue
                        elif selected_row == -1 and selected_column == -1:
                            if grid[grid_pos[2]][grid_pos[1]] == 1:
                                selected_row = grid_pos[2]
                                selected_column = grid_pos[1]
                                print("Stored row:", selected_row, " ,Stored column:", selected_column)
                            else:
                                selected_row = -1
                                selected_column = -1
                                print(selected_row, selected_column)

        screen.fill(DARK_GREY)
        draw_grid(grid, screen)
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()


# Run application
if __name__ == '__main__':
    main()
