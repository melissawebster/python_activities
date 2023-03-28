from time import sleep

def decorator_imprimir(function):
    def imprimir(*args,**kwargs):
        print('-' * 20)
        print('Calculando seu investimento...')
        sleep(1)
        function(*args,**kwargs)
        print('Volte sempre!')
    return imprimir

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    print(capital * (taxa/100) * tempo)


capital = float(input('Digite o capital: '))
taxa = float(input('Digite a taxa: '))
tempo = float(input('Digite o tempo: '))

juros_simples(capital, taxa, tempo)
