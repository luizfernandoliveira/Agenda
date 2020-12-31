'''db = {}
print('Agenda (Telefone e endereço)')
while True:
    print('Oque você gostaria de fazer?')
    print('Entre com A para adicionar um contato, V para visualizar um contato ou L para acessar a lista')
    print('Entre com  S para sair')
    action = input()
    if action == 'A':
        nome = input('Entre com o contato: ')
        telefone = input('Entre com o telefone: ')
        endereco = input('Entre com o endereço: ')
        db[nome] = {'nome': nome, 'telefone': telefone, 'endereco': endereco}
        print(db.values())
        print(db)
        print(db.keys())
        print(db.items())
        print(20*'-')
        # print(db['nome'])
        # print(db['telefone'])
        # print(db['endereco'])
    elif action == 'V':
        contato = input('Entre com o contato: ')
        if k not in db:
            print('Não encontrado')
        else:
            print('Seu contato: {} \nTelefone: {} \nEndereço: {} \n'.format(k, db[k], db[k]))
    elif action == 'L':
        print('Contatos:')
        print(db)
    elif action == 'S':
        print('Até a próxima')
        break
'''
