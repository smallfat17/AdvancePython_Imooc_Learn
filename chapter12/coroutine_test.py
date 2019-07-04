def test_func():
    yield 1
    yield 2
    return 3

if __name__ == '__main__':
    result = test_func()
    for num in result:
        print(num)
    print(result)
    result.send()