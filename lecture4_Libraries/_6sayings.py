# rough practice 6:-

# This  is my own 'sayings' module.
# self made package: bundle set if codes

def main():
    hello("world")
    goodbye("world")
def hello(name):
    print(f"hello, {name}")
def goodbye(name):
    print(f"goodbuy, {name}")


# __name__ : special symbol. 
if __name__=="__main__":
    main()