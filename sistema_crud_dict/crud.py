registrer_dict = {}
vl_salve = ''
salve_values = []
border = '-' * 35
from os import system

def header():
    print(border)
    print(f'{"CRUD-DICIONÁRIO":=^35}')
    print(border)
    print('=' * 35)
    print('A- inserir par de (chave/valor)')
    print('B- alterar par de (chave/valor)')
    print('C- apagar par de (chave/valor)')
    print('D- ver dict completo')
    print('E- sair do sistema')
    print('=' * 35)

# insere dados
def data_collect(name_key,name_value):
    registrer_dict[name_key] = name_value
    return registrer_dict

# eidtar dados
def data_edition(old_key,name_key,name_value):
    del registrer_dict[old_key]
    registrer_dict.update(
        {name_key: name_value
         
         })
    return registrer_dict

# function key_del
def data_del(name_key,salve_key):
    salve_key = registrer_dict.pop(name_key)
    return salve_key

#limpar tela
def clean_screen():
    print('Limpar tela?')
    new_screen = input('[s]im /[n]ão: ')
    print(border)
    new_screen = new_screen.startswith('s') and new_screen.endswith('s')
    if new_screen:
        system('cls')

while True:
    header()
    option = input('Escolha uma opção [A] [B] [C] [D]: ').upper()
    print(border)
    new_screen = clean_screen()

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
        dict_data = data_collect(name_key,name_value)
        clean_screen()

    #alterar chave
    option_edition = option.startswith('B') and option.endswith('B')

    if option_edition:
        old_key = input('Chave que deseja trocar: ').upper()
        print(border)
        clean_screen()

        if not old_key in registrer_dict:
            print('Essa chave não está registrada!!!')
            continue

        else:
            new_key = input('Nova chave: ').upper()
            print(border)
            new_value = input('Novo valor: ').upper()
            print(border)
            data_edition(old_key,new_key,new_value)
        
    #apagar chave
    data_delete = option.startswith('C') and option.endswith('C')
    dict_null = len(registrer_dict) == 0

    if data_delete:
        delete = input('Apagar Chave: ').upper()
        print(border)

        if not delete in registrer_dict:
            print('Essa chave não está registrada!!!')
            continue

        else:
            print('Deseja salvar o valor da chave excluída?')
            print(border)
            salve_key = input('[s]im / [n]ão ').upper()
            
            yes = salve_key.startswith('S') and salve_key.endswith('S')

            if yes:
                salve_sucessul = data_del(delete,vl_salve)
                salve_values.append(salve_sucessul) # opção para acessar os valores salvos
                print(f'valor salvo: {salve_values}')
            
            else:
                key_del = data_del(delete,vl_salve)
                clean_screen()
                print('Chave excuída com sucesso!!!')
          
    # ver dicionário
    dict_view = option.startswith('D') and option.endswith('D')

    if dict_view:
        if dict_null:
            print(f'{"Dicionário vazio":-^35}')
            continue

        else:
            for name_key,name_values in registrer_dict.items():
                print(f'|{name_key} : {name_values}|')

    sair = option.startswith('E') and option.endswith('E')

    if sair:
        print('Até Logo!!!')
        print(border)
        break