def solve(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 's':
                x = i
                y = j
                break

    granisa_x = len(maze)
    granisa_y = len(maze[0])

    def poisk_puti(x, y, put):
        if x < 0 or x >= granisa_x or y < 0 or y >= granisa_y:
            return None
        if maze[x][y] == '#':
            return None
        if maze[x][y] == 'x':
            return put
        if maze[x][y] != 's':
            stroka = list(maze[x])
            stroka[y] = '#'
            maze[x] = ''.join(stroka)
        result = poisk_puti(x, y + 1, put + ['right'])
        if result is not None:
            return result

        result = poisk_puti(x + 1, y, put + ['down'])
        if result is not None:
            return result

        result = poisk_puti(x, y - 1, put + ['left'])
        if result is not None:
            return result

        result = poisk_puti(x - 1, y, put + ['up'])
        if result is not None:
            return result

        if maze[x][y] != 's':
            stroka = list(maze[x])
            stroka[y] = '-'
            maze[x] = ''.join(stroka)

        return None

    return poisk_puti(x, y, [])

maze = ['s----',
        '##---',
        '---##',
        '----x']
print(solve(maze))