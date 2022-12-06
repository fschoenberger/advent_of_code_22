def rolling_window(seq, window_size):
    it = iter(seq)
    win = [it.next() for cnt in xrange(window_size)] # First window
    yield win
    for e in it: # Subsequent windows
        win[:-1] = win[1:]
        win[-1] = e
        yield win
    

def main():
    with open("./Puzzle 06.txt") as f:
        line = f.readline()
        i = 0
        window_size = 14
        for i in range(len(line) - window_size + 1):
            window = line[i : i + window_size]
            if len(set(window)) == window_size:
                print(i + window_size)
                break




if __name__ == "__main__":
    main()