def f(x1, x2):
    return 2 * x1 + x2 - (x1 * x2) ** 3

def get_neighbors(x1, x2):
    neighbors = []
    for dx1 in [-1, 0, 1]:
        for dx2 in [-1, 0, 1]:
            if dx1 == 0 and dx2 == 0:
                continue
            nx1, nx2 = x1 + dx1, x2 + dx2
            if 1 <= nx1 <= 350 and -3 <= nx2 <= 180:
                neighbors.append((nx1, nx2))
    return neighbors

def hill_climbing(start_x1, start_x2):
    current = (start_x1, start_x2)
    current_val = f(*current)
    while True:
        neighbors = get_neighbors(*current)
        next_neighbor = max(neighbors, key=lambda x: f(*x))
        next_val = f(*next_neighbor)
        if next_val > current_val:
            current, current_val = next_neighbor, next_val
        else:
            break
        # print(current, current_val)
    return current, current_val

if __name__ == '__main__':

    current1, current_val1 = hill_climbing(10,50)
    print(f"Punctul cel mai mare: {current1}")
    print(f"Valoarea cea mai mare: {current_val1}")
