def sum_of_digits(coordinate: int) -> int:
    '''Подсчет суммы цифр в координате.'''

    return sum(int(digit) for digit in str(coordinate))


def is_accessible(x: int, y: int) -> bool:
    '''Проверка суммы цифр в координате.'''

    return sum_of_digits(x) + sum_of_digits(y) <= 25


def ant_moves(x: int, y: int, visited: set) -> set:
    '''Подсчет возможных перемещений муравья.'''

    visited.add((x, y))
    moves = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]
    for move in moves:
        if move not in visited and is_accessible(*move):
            ant_moves(*move, visited)
        else:
            return visited


if __name__ == '__main__':
    start_x, start_y = 1000, 1000
    visited_cells = ant_moves(start_x, start_y, set())
    print(f'Муравей может посетить {len(visited_cells)} клеток.')
