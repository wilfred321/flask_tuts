def square(x):
    result = x*x
    return result

def main():
    for i in range(10):
        print(f'{i} square is equal to {square(i)}')


if __name__ == '__main__':
    main()
    