import datetime

debug = True


def write_line(msg):
    with open('example.log', 'a') as f:
        f.write(f'{datetime.datetime.now()} {msg}\n')


def handle_msg(msg):
    write_line(msg)
    print(msg)


def calc_sum_of_list(l):
    s = 0
    for n in l:
        s += n
        if debug:
            handle_msg(f'Adding {n}, actual sum: {s}')
    return s


def main():
    handle_msg('Hi')
    l = [123, 345, 42, 11]
    s = calc_sum_of_list(l)
    handle_msg(f'Sum of {l}: {s}')


if __name__ == '__main__':
    main()
