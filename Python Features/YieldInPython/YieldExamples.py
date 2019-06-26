class Features:
    def print_even(self, test_list): 
        for i in test_list: 
            if i % 2 == 0: 
                yield i 


def yield_test():
    test_list = [e for e in range(10)]
    print(test_list)
    gen = Features().print_even(test_list)
    print(gen)
    print(next(gen))
    print(next(gen))
    print(next(gen))

