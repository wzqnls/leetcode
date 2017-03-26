"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.

Example:
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]

    Answer: 16
"""

"""
题目翻译：
给定一个二维的表格，每个格子中的数字为1代表陆地，数字为0则代表为海洋。表格完全被海洋包围，而且只有一块岛屿，
这块岛屿由多个陆地格子连接所形成。这个岛屿不会有水渗进来，不考虑进水的问题。每一个格子的边长都为1，
整个表格是一个正方形，并且边长不会超过100.计算真个岛屿的周长。
"""

"""
解题思路：
由于整个岛屿中表格的方位与数量是动态可变的，所以需要归纳分类
整个岛屿的周长由每个格子的外边长度相加所得，故只需要计算每个格子对外的周长，然后相加即岛屿的周长

对每个格子的上下左右相邻格子的数值进行判断，故分为四类进行讨论。
举例：格子上方是否存在陆地
    首先判断格子上方还有没有格子了，保证数组不会越界（下面几种分类判断思路相同）
    判断上方格子值是否为0
    若上方没有格子了，或者上方格子数值为0，则周长加1

将单个格子的周长计算由函数进行封装，然后遍历整个表格，相加所有格子周长，即得总周长
"""


class Solution(object):

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def cell_perimeter(y, x):
            perimeters = 0
            if y == 0 or grid[y - 1][x] == 0:
                perimeters += 1
            if y == len(grid) - 1 or grid[y + 1][x] == 0:
                perimeters += 1
            if x == 0 or grid[y][x - 1] == 0:
                perimeters += 1
            if x == len(grid[0]) - 1 or grid[y][x + 1] == 0:
                perimeters += 1
            return perimeters
        return sum(cell_perimeter(y, x) for y, lst in enumerate(grid) for x, cell in enumerate(lst) if cell)
