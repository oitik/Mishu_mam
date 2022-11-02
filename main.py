from colorama import Fore, Back, Style


def transition(q, a):
    ans = q
    for val in a:
        if val not in '01':
            print('Error code exiting...')
            return -1
        ans = delta(ans, val)
    return ans


def summary(q, a):
    i = 1
    ans = q
    save = q
    d = '\u03B4'
    dz = '\u03B6'
    st = '\u03b5'
    st += a
    print(Fore.RED+Back.WHITE+'-------------------------------------------------------')
    print('|')
    print(f'|\t{dz}({save}, \u03B5) = {ans} ')
    for val in a:
        if i > 1:
            print(f'|\t\u03B6({save}, {val}) = {d}({dz}({save}, {st[1:i]}), {val}) = ', end='')
        else:
            print(f'|\t\u03B6({save}, {val}) = {d}({dz}({save}, {st[:i]}), {val}) = ', end='')
        ans = delta(ans, val)
        print(f'{d}({save}, {val}) = {ans}')
        save = ans
        i += 1
    print('|')
    print('-------------------------------------------------------')
    print(Style.RESET_ALL+'')


def delta(q, inp):
    if q == 'q0' and inp == '0':
        return 'q2'
    if q == 'q0' and inp == '1':
        return 'q1'
    if q == 'q1' and inp == '0':
        return 'q3'
    if q == 'q1' and inp == '1':
        return 'q0'
    if q == 'q2' and inp == '0':
        return 'q0'
    if q == 'q2' and inp == '1':
        return 'q3'
    if q == 'q3' and inp == '0':
        return 'q1'
    if q == 'q3' and inp == '1':
        return 'q2'


def main_menu():
    print(Fore.BLUE+f'''
    Press 1 to see if the string is acceptable!
    Press 2 to see the summary of calculation
    press 3 to exit 
''')
    print(Style.RESET_ALL+'', end='')


def select_method():
    main_menu()
    x = input('Enter your string: ')
    while True:
        m = int(input('Enter your selection: '))
        if m == 1:
            if transition(start, x) == start:
                print(Fore.GREEN+'\t Your string only contains even number of 0 and 1')
                print('\t Hence it is acceptable')
                print(Style.RESET_ALL + '', end='')
            else:
                print(Fore.RED+'Your string is not acceptable')
                print(Style.RESET_ALL + '', end='')
        elif m == 2:
            summary(start, x)
        elif m == 3:
            exit('thanks for choosing oitik')


if __name__ == '__main__':
    q_li = ['q0', 'q1', 'q2', 'q3']
    e_li = [0, 1]
    start = 'q0'
    end = 'q0'
    select_method()
