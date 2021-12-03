def count(filename):
    increases = 0
    with open(filename, 'r') as depths:
        a = next(depths)
        for b in depths:
            if int(b) > int(a):
                increases += 1
                print("Increase")
            else:
                print("Decrease")
            a = b
    return increases


if __name__ == '__main__':
    print(count("Day1.1_input"))
