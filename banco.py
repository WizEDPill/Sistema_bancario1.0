total=0
contador=0
while True:
    valor = int(input('Informe o valor a ser Depositado ='))
    total+=valor

    contint= input('voce deseja continuar depositando ? y-sim n- nao')
    if contint=='n':
        sq=input('deseja ver extrado? y-sim n-nao').strip().lower()
        if sq=='n':
            break;
        if sq=='y':
            print(f'O valor do seu extrato: ------- R${total}-------')
            numb=input('Voce deseja fazer o saque de algum valor ? y-sim n- nao')
            if numb=='n':
                break;
            if numb=='y': 
                saq= int(input('Informe o valor do saque: '))
                print('O Limite são 3 saques diarios de no maximo R$500reais ')
                mumb=+saq
                if saq>total: 
                        print(f'seu saldo e R$ {saq-total} a menos que seu valor em conta, assim não sera possivel fazer o saque.')
                elif saq>500: 
                        print('Valor de saque excede o limite de R$500,00 por saque')
                        continue;
                elif contador>3: 
                        print('voce ultrapassou o limite de saques diarios')
                else: 
                        print(f'seu saque de R${saq} foi feito com sucesso seu extrato agora é de R$ {total-saq} ')
                        contador+=1
                        valor= input('Deseja voltar o menu de deposito ou concluir a operacao?y- sim ,n- nao')
                if valor=='y': 
                            continue; 
                else: 
                            break; 
                    
print(f'O valor total depositado é R${total}.')

