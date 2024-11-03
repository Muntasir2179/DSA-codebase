step = 1

def tower_of_hanoi(n, source, destination, auxiliary):
    global step
    if n == 0:
        return
    if n == 1:
        print(step, source, "-->", destination)
        step += 1
        return

    tower_of_hanoi(n-1, source, auxiliary, destination)
    print(step, source, "-->", destination)
    step += 1
    tower_of_hanoi(n-1, auxiliary, destination, source)


if __name__ == "__main__":
    tower_of_hanoi(5, 'source', 'destination', 'auxiliary')
