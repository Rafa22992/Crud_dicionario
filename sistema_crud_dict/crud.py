registrer_dict = {}
vl_salve = '' # salva o valor da chave
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
    print('D- ver dicionário completo')
    print('E- sair do sistema')
    print('=' * 35)

# insere dados
def data_collect(name_key,name_value):
    registrer_dict[name_key] = name_value
    return registrer_dict

# edita dados
def data_edition(old_key,new_key,new_value):
    del registrer_dict[old_key]
    registrer_dict.update(
        {new_key: new_value
         })
    return registrer_dict

#apaga chaves
def data_del(name_key,salve_key):
    salve_key = registrer_dict.pop(name_key)
    return salve_key

# salva as chaves excluídas
def salve_keys(key,value):
    salve_values.append((key,value))
    print(f'valor salvo: {salve_values}')

#limpar tela
def clean_screen():
    print('Limpar tela?')
    new_screen = input('[s]im /[n]ão: ').upper()
    new_screen = options(new_screen,'S')
    if new_screen:
        system('cls')
# -------------------- funções de um nó

# opções do usuário
options = lambda option,letter: option.startswith(letter) and option.endswith(letter)
# condição para dicionário vazio
null_value = lambda null_dict: len(null_dict) == 0
# caso vl digitado não esteja no dicionário
no_dict = lambda user_input,dict: not user_input in dict

while True:
    header()
    option = input('Escolha uma opção [A]-[B]-[C]-[D]-[E]: ').upper()
    print(border)
    new_screen = clean_screen()

    allowed_options = not option in 'ABCDE' #opções permetidas
    not_alpha = not option.isalpha()
    max_one = len(option) > 1

    if not_alpha or max_one or allowed_options:
        print('DADOS INVÁLIDOS: Digite Novamente.')
        
    data_insert = options(option,'A')
    
    # inserir dados
    if data_insert:
        name_key = input('Digite o nome da chave: ').upper()
        print(border)
        name_value = input('Digite o valor da chave: ').upper()
        print(border)
        dict_data = data_collect(name_key,name_value)
        clean_screen()

    #alterar chave
    option_edition =  options(option,'B')

    if option_edition:
        old_key = input('Chave que deseja trocar: ').upper()
        print(border)
        clean_screen()

        no_dict_old_key = no_dict(old_key,registrer_dict)
        if no_dict_old_key:
            print('Essa chave não está registrada!!!')
            
        else:
            new_key = input('Nova chave: ').upper()
            print(border)
            new_value = input('Novo valor: ').upper()
            print(border)
            data_edition(old_key,new_key,new_value)
        
    #apagar chave
    data_delete =  options(option,'C')
    dict_null = null_value(registrer_dict)
    
    if data_delete:
        delete = input('Apagar Chave: ').upper()
        print(border)

        no_dict_delete = no_dict(delete,registrer_dict)
        if no_dict_delete:
            print('Essa chave não está registrada!!!')
            
        else:
            print('Deseja salvar o valor da chave excluída?')
            print(border)
            salve_key = input('[s]im / [n]ão ').upper()
            
            yes =  options(salve_key,'S')

            if yes:
                salve_sucessul = data_del(delete,vl_salve)
                sal_k = salve_keys(delete,salve_sucessul)
                                      
            else:
                key_del = data_del(delete,vl_salve)
                clean_screen()
                print('Chave excuída com sucesso!!!')
          
    # ver dicionário
    dict_view =  options(option,'D')

    if dict_view:
        if dict_null:
            print(f'{"Dicionário vazio":-^35}')
            
        else:
            for name_key,name_values in registrer_dict.items():
                key_value = f'|{name_key}:{name_values}|'
                print(f'{key_value:^35}')

    bye =  options(option,'E')

    if bye:
        print('Até Logo!!!')
        print(border)
        break  