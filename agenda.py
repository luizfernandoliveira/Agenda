db = {}
print('Agenda (Telefone e endereço)')
while True:
    print('Oque você gostaria de fazer?')
    print('Entre com A para adicionar um contato, V para visualizar um contato ou L para acessar a lista')
    print('Entre com  S para sair')
    action = input()
    if action == 'A':
        k = input('Entre com o contato: ')
        d = input('Entre com o telefone: ')
        e = input('Entre com o endereço: ')
        db[k] = {'nome': d, 'endereco': e}
    elif action == 'V':
        k = input('Entre com o contato: ')
        if k not in db:
            print('Não encontrado')
        else:
            print('Seu contato: {} \nTelefone: {} \nEndereço: {} \n'.format(k, db['nome'], db['endereco']))
    elif action == 'L':
        print('Contatos:')
        print(db)
    elif action == 'S':
        print('Até a próxima')
        break
