
def main():
    lista = [1, 10, 100, 1000]
    print(takaperin(lista))
    print(lista) 

def takaperin(lista):
    x = sorted(lista, reverse=True)
    return x

main()