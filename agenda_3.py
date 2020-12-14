contato = {}
print('Agenda (Telefone e endereço)')
while True:
    print('Oque você gostaria de fazer?')
    print('Entre com A para adicionar um contato, V para visualizar um contato ou L para acessar a lista')
    print('Entre com  S para sair')
    action = input()
    if action == 'A':
        contato = input('Entre com o contato: ')
        tel = input('Entre com o telefone: ')
        endereco = input('Entre com o endereço: ')
        contato = {'nome': contato, 'tel1': tel, 'end': endereco}
        contato = contato
    elif action == 'V':
        visu_contato = input('Entre com o contato: ')
        if visu_contato not in contato['nome']:
            print('Não encontrado')
        else:
            print(20 * '-')
            print('Seu contato: {} \nTelefone: {} \nEndereço: {} \n'
                  .format(contato['nome'], contato['tel1'], contato['end']))
            print(20 * '-')
    elif action == 'L':
        print(contato)

    elif action == 'S':
        print('Até a próxima')
        break
