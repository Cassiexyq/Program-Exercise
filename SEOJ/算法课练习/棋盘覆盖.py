# -*- coding: utf-8 -*-

"""
@Time    : 2019/2/28 16:40
@Author  : Cassie
@Description :
"""

# board 棋盘，size 不断分割的棋盘大小， tr 左上角行号 tc 左上角列号 dr 特殊方块行号 dc特殊方块列号
def chessboard(board, size, tr, tc, dr, dc):
    if size <= 1:
        return
    global tile
    tile += 1  # 表示L型骨牌编号
    current_tile = tile
    size //= 2  # 划分棋盘
    # 递归覆盖左上角棋盘
    if dr < tr + size and dc < tc + size:  # 若不在左上
        chessboard(board, size, tr, tc, dr, dc)
    else:
        board[tr + size - 1][tc + size - 1] = current_tile  # 用title覆盖右下角
        chessboard(board, size, tr, tc, tr + size - 1, tc + size - 1)

    if dr >= tr + size and dc < tc + size:  # 左下
        chessboard(board, size, tr + size, tc, dr, dc)
    else:
        board[tr + size][tc + size - 1] = current_tile
        chessboard(board, size, tr + size, tc,
                   tr + size, tc + size - 1)

    if dr < tr + size and dc >= tc + size:  # 右上
        chessboard(board, size, tr, tc + size, dr, dc)
    else:
        board[tr + size - 1][tc + size] = current_tile
        chessboard(board, size, tr, tc + size,
                   tr + size - 1, tc + size)

    if dr >= tr + size and dc >= tc + size:  # 右下
        chessboard(board, size, tr + size, tc + size, dr, dc)
    else:
        board[tr + size][tc + size] = current_tile
        chessboard(board, size, tr + size, tc + size,
                   tr + size, tc + size)


if __name__ == '__main__':
    tile = 0
    num = int(input())
    resultList = []
    for i in range(num):
        arr1 = [int(x) for x in input().split()]
        chessboard_size = pow(2, arr1[0])  # 棋盘大小
        board = [[0 for x in range(chessboard_size)] for y in range(chessboard_size)]
        chessboard(board, chessboard_size, 0, 0, arr1[1], arr1[2])
        arr2 = [int(x) for x in input().split()]
        label = board[arr2[0]][arr2[1]]  # 要找的坐标的骨牌编号
        resultstr = ''
        for i in range(chessboard_size):  # 行
            for j in range(chessboard_size):  # 列
                if i == arr2[0] and j == arr2[1]: # 跳过该坐标
                    continue
                else:
                    if board[i][j] == label:
                        resultstr += str(i) + " " + str(j) + ","
        resultList.append(resultstr[:-1])
    for result in resultList:
        print(result)
