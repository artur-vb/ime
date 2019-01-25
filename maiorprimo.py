## taks: find the highest prime number of a given number. 

def maior_primo(x):
    i = 2

    while i < x:
        if x%i != 0:
            i = i + 1
        else: 
            x = x-1
    return x
