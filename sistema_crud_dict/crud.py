registrer_dict = {}
from os import system

# function data insert
def data_collect(name_key,name_value):
    dynamic_key = name_key
    registrer_dict[dynamic_key] = name_value
    return registrer_dict

# function key_del
def data_del(name_key):
    dynamic_key = name_key
    del registrer_dict[dynamic_key]
    return registrer_dict

border = '-' * 35
while True:
    # CABEÇALHO ---------------------------
    print(border)
    print(f'{"CRUD-DICIONÁRIO":=^35}')
    print(border)
    print('=' * 35)
    print('A- inserir par de (chave/valor)')
    print('B- alterar par de (chave/valor)')
    print('C- apagar par de (chave/valor)')
    print('D- ver dict completo')
    print('=' * 35)

    option = input('Escolha uma opção [A] [B] [C] [D]: ').upper()
    print(border)
    system('cls')

    data_insert = option.startswith('A') and option.endswith('A')

    if not option.isalpha() or len(option) > 1:
        print('DADOS INVÁLIDOS: Digite Novamente.')
        continue

    # inserir dados
    if data_insert:
        name_key = input('Digite o nome da chave: ').upper()
        print('-' * 35)
        name_value = input('Digite o valor da chave: ').upper()
        print('-' * 35)
        system('cls')
        dict_data = data_collect(name_key,name_value)

    #apagar chave
    data_delete = option.startswith('C') and option.endswith('C')

    if data_delete:
        delete = input('Apagar Chave: ').upper()
        print(border)

        if not delete in registrer_dict:
            print('Essa chave não está registrada!!!')
            continue

        else:
            key_del = data_del(delete)
            system('cls')
            print('Chave excuída com sucesso!!!')
            print(border)
          
    # ver dicionário
    dict_view = option.startswith('D') and option.endswith('D')

    if dict_view:
        if len(registrer_dict) == 0:
            print(f'{"Dicionário vazio":-^35}')
            continue

        else:
            for name_key,name_values in registrer_dict.items():
                system('cls')
                print(f'{name_key} : {name_values}')
                print('=' * 35)