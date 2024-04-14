# zmienna zadeklarowana lokalnie w metodzie jest nadal przechowywana w pamięci (i jej referencja), po jej wywołaniu

if __name__ == "__main__":
    def add1(a):
        def add2(b):
            return a+b
        return add2

    

    add3 = add1(3);
        
    print(add3(4)); 
