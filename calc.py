import funções as f
import textos as t

escolha = '0'
case = '0'
print('\nBem-vindo a calculadora')
while escolha != '3':
    t.texto_inicial()
    escolha = input('Digite onde deseja ir: ')
    if escolha == '1':
        while True:
            t.texto_basicas()
            case = input('Digite o numero da operação: ')
            if case in ('1','2','3','4','5'):
                num1 = int(input('\nDigite o primeiro numero: '))
                num2 = int(input('Digite o segundo numero: '))  
            elif case == ('6'):
                num1 = int(input('Digite o numero: ')) 
            elif case == ('7'):
                num1 = int(input('\nDigite o valor de a: '))
                num2 = int(input('Digite o valor de b: '))  
                num3 = int(input('Digite o valor de c: '))   
            elif case == ('8'):
                break
            else:
                print('Digite um numero valido!')
                continue
            
            if case == '1':  
                resposta =  f.soma(num1, num2)
            elif case == '2':
                resposta = f.menos(num1, num2)
            elif case == '3':
                resposta = f.multiplicação(num1, num2)
            elif case == '4':
                resposta = f.Divisão(num1, num2)
            elif case == '5':
                resposta = f.potenciação(num1, num2)
            elif case == '6':
                resposta = f.fatorial(num1)
            elif case == '7':
                resposta = f.eq_segundo_grau(num1, num2, num3)  

            print('\nA resposta é:', resposta)       
    
    elif escolha == '2' or escolha == 'funções':
        while True:
            t.texto_funções()
            case = input('Digite o numero da função: ')
            if case in ('3','4','5'):
                num1 = int(input('digite o numero: '))
            elif case in ('1'):
                num1 = int(input('o valor de a: '))
                num2 = int(input('o valor de b: '))
            elif case == ('2'):
                num1 = int(input('o valor de a: '))
                num2 = int(input('o valor de b: '))
                num3 = int(input('o valor de c: '))
            elif case == ('6'):
                break
            else:
                print('\nDigite um numero valido!')
                continue
            
            if case == '1':
                resposta = f.plot_linear(num1, num2)
            elif case == '2':
                resposta = f.plot_quadratica(num1,num2, num3)
            elif case == '3':
                resposta = f.plot_exponencial(num1)
            elif case == '4':
                resposta = f.plot_raiz(num1)
            elif case == '5':
                resposta = f.plot_fatorial(num1)
            
            print('\nA resposta é:', resposta) 
    elif escolha != '3':
        print('\nDigite um numero valido')
        continue
print('Fim do programa')