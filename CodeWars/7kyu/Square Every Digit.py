def square_digits(num):
    a = []
    for i in str(num):
        i = int(i)
        a.append(i*i)
    string = [str(int) for int in a]
    string = ''.join(string)
    string = int(string)
    return string
        