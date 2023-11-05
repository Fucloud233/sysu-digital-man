from threading import Thread

def main():
    Thread(target=display).start()
    print("hello")
    pass

def display():
    print("hello world")

if __name__ == '__main__':
    main()