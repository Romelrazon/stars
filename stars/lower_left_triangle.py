def main(size): 
    while size >= 1:
        col = 1
        while col <= size:
            print('*', end="")
            col += 1
        print("")
        size -= 1

main(5)