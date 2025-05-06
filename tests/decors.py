# def benchmark(func):
#     import time
    
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end-start))
#     return wrapper

# @benchmark
# def fetch_webpage_1():
#     import requests
#     webpage = requests.get('https://google.com')
#     print("!!!")

# @benchmark
# def fetch_webpage_2():
#     print("1")

# fetch_webpage_1()
# fetch_webpage_2()

def get(func):
    def wrapper(*args, **kwargs):
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func(*args, **kwargs)
        print('Выходим из обёртки')
    return wrapper

def hello_world(url, count) -> None:
    print('Hello world!')

@get
def fetch_webpage(url) -> None:
    print('Cool!!! ')

hello = get(hello_world)

hello(count = 1, url = "www.1c.ru")
fetch_webpage("www.test.ru")