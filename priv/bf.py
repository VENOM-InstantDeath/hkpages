o = "++++++++++[>+++>+++++>+++++++>++++++++++<<<<-]"
p = 0
a = [0 for i in range(6)]

a[1] = 30   # ' '
a[2] = 50   # '0'
a[3] = 70   # 'A'
a[4] = 100  # 'a'

bf = input('>> ')

if bf:
    for i in bf:
        if i.isdigit():
            if p < 2:
                for e in range(2-p): o += '>'
            else:
                for e in range(p-2): o += '<'
            p = 2
            if ord(i) < a[2]:
                for e in range(a[2] - ord(i)):
                    o += '-'
                    a[2] -= 1
            else:
                for e in range(ord(i) - a[2]):
                    o += '+'
                    a[2] += 1
        elif i.isupper():
            if p < 3:
                for e in range(3-p): o += '>'
            else:
                for e in range(p-3): o += '<'
            p = 3
            if ord(i) < a[3]:
                for e in range(a[3] - ord(i)):
                    o += '-'
                    a[3] -= 1
            else:
                for e in range(ord(i) - a[3]):
                    o += '+'
                    a[3] += 1
        elif i.islower():
            if p < 4:
                for e in range(4-p): o += '>'
            else:
                for e in range(p-4): o += '<'
            p = 4
            if ord(i) < a[4]:
                for e in range(a[4] - ord(i)):
                    o += '-'
                    a[4] -= 1
            else:
                for e in range(ord(i) - a[4]):
                    o += '+'
                    a[4] += 1
        elif i == ' ':
            if p < 1:
                for e in range(1-p): o += '>'
            else:
                for e in range(p-1): o += '<'
            p = 1
            if ord(i) < a[1]:
                for e in range(a[1] - ord(i)):
                    o += '-'
                    a[1] -= 1
            else:
                for e in range(ord(i) - a[1]):
                    o += '+'
                    a[1] += 1
        o += '.'
    print(o)
