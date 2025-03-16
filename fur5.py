def main():
    s = ""
    for _ in'!'*(int(input())-1):
        s = s.replace('C', 'D').replace('B', 'C').replace('D', 'B') + 'AC\n' + s.replace('A', 'D').replace('B', 'A').replace('D', 'B')
    print(s.replace('C', 'D').replace('B', 'C').replace('D', 'B'))
    print('AC')
    print(s.replace('A', 'D').replace('B', 'A').replace('D', 'B'))
main()