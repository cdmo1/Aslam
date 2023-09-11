# Dicionário global(como variável global) para armazenar os usuários
banco_usuarios = []
"""
    Cadastro de um usuário no "banco de dados".
    Argumentos(parâmetros):
        campos_obrigatorios (tupla): Uma tupla com os campos obrigatórios para o cadastro.
    Retorno, response:
        dicionário: O dicionário com os dados do usuário cadastrado.
"""
def cadastrar_usuario(campos_obrigatorios):

    usuario = {}
    for campo in campos_obrigatorios:
        valor = input(f"Digite o valor para o campo '{campo}': ")
        usuario[campo] = valor
    aux = True
    while aux:
        campo_extra = input("Digite um campo adicional (ou 'sair' para encerrar): ")
        if campo_extra.lower() == 'sair':
            break
        valor_extra = input(f"Digite o valor para o campo '{campo_extra}': ")
        usuario[campo_extra] = valor_extra

    banco_usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    return usuario
"""
    Imprime os usuários com base nas opções selecionadas.

    Argumentos(parâmetros):
        *args: Argumentos posicionais (nomes dos usuários).
        **kwargs: Argumentos chave-valor (campos e valores de filtro).

"""
def imprimir_usuarios(*args, **kwargs):

    opcao = int(input("1 - imprimir todos\n2 - filtrar por nomes\n3 - filtrar por campos\n4 - filtrar por nomes e campos\n"))
    
    if opcao == 1:
        for usuario in banco_usuarios:
            print(usuario)
    elif opcao == 2:
        nomes = args
        for usuario in banco_usuarios:
            if usuario['nome'] in nomes:
                print(usuario)
    elif opcao == 3:
        campos = kwargs.keys()
        for usuario in banco_usuarios:
            if all(usuario.get(campo) == valor for campo, valor in kwargs.items()):
                print(usuario)
    elif opcao == 4:
        nomes = args
        campos = kwargs.keys()
        for usuario in banco_usuarios:
            if usuario['nome'] in nomes and all(usuario.get(campo) == valor for campo, valor in kwargs.items()):
                print(usuario)
    else:
        print("Opção inválida!")
"""
    função principal para inicialização do processo de cadastro no "banco de dados"
"""
def main():
    campos_obrigatorios = input("Digite os nomes dos campos obrigatórios separados por vírgula: ").split(',')
    aux = True
    while aux:
        print("\nMenu:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("0 - Encerrar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario(campos_obrigatorios)
        elif opcao == '2':
            imprimir_usuarios()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
