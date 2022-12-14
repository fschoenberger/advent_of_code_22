import numpy as np


def main():
    with open("Puzzle 08.txt") as f:
        grid_list = [[c for c in line if c != "\n"] for line in f.readlines()]
        grid = np.array(grid_list, dtype=int)

        print(grid)

        grid_size_x, grid_size_y = np.shape(grid)

        visible_count = grid_size_x * 2 + grid_size_y * 2 - 4

        for i in range(1, grid_size_x - 1):
            for j in range(1, grid_size_y - 1):
                tree_height = grid[i][j]

                top = np.max(grid[:i, j])
                bottom = np.max(grid[i + 1:, j])
                right = np.max(grid[i, j + 1:])
                left = np.max(grid[i, :j])

                if left < tree_height or right < tree_height or top < tree_height or bottom < tree_height:
                    #print(f"Tree ({i}, {j}) with height {tree} is visible: left={left}, right={right}, top={top}, bottom={bottom}")
                    visible_count += 1

        print(f"Part 1: There are {visible_count} visible trees.")

        del top, left, bottom, right

        max_scenic_score = 0

        for i in range(1, grid_size_x - 1):
            for j in range(1, grid_size_y - 1):
                tree_height = grid[i][j]

                left = 0
                for k in reversed(grid[i, :j]):
                    left += 1
                    if k >= tree_height:
                        break

                right = 0
                for k in grid[i, j+1:]:
                    right += 1
                    if k >= tree_height:
                        break
                
                top = 0
                for k in reversed(grid[:i, j]):
                    top += 1
                    if k >= tree_height:
                        break
                
                bottom = 0
                for k in grid[i+1:, j]:
                    bottom += 1
                    if k >= tree_height:
                        break
                
                scenic_score = top * bottom * left * right
                print(f"Tree ({i}, {j}, h={tree_height}) with score {scenic_score}: up={top}, left={left}, right={right}, down={bottom}")

                if scenic_score > max_scenic_score:
                    max_scenic_score = scenic_score

        print(f"Part 2: The max scenic score was {max_scenic_score}")


if __name__ == "__main__":
    main()
