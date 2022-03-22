#Criação da Pilha
pilha = [];

#Criação do Menu de opções
option_menu = 0;
while option_menu !=5:
    print('''
        MENU:

        [1] - Empilhar
        [2] - Desempilhar
        [3] - Limpar
        [4] - Mostrar Pilha
        [5] - Sair
    ''')
    option_menu = int(input('Escolha uma opção: '));

#Adicionando itens a pilha
    if option_menu == 1:
        itens_pilha = int(input('Quantos itens quer adicionar na pilha? MAX. 30: '))
        if itens_pilha > 30:
            print('Erro! Número de itens ultrapassa valor máximo.');
        else:
            for x in range(0, itens_pilha):
                topo = input('Insira os itens em sua pilha: ');
                pilha.append(topo);
            print('Itens adicionados com sucesso!');
        print('Retornando ao menu...');

#Removendo itens da pilha
    if option_menu == 2:
        retira_pilha = int(input('O último item adicionado será removido! Confirmar? (1 - Sim/ 2- Não): '))
        if retira_pilha == 1:
            item_removido = pilha.pop();
            print('O último item foi removido com sucesso!'); 
        else:
            print('Cancelando operação!');
        print('Retornando ao menu...');

#Limpando pilha
    if option_menu == 3:
        limpar_pilha = int(input('A pilha será excluída! Confirmar? (1 - Sim/ 2- Não): '))
        if limpar_pilha == 1:
            pilha.clear();
            print('Limpeza concluída!'); 
        else:
            print('Cancelando operação!');
        print('Retornando ao menu...');

#Mostrando Pilha enumerada
    if option_menu == 4:
        for indice, dados in enumerate(pilha):
            print('Indice:',indice, 'Elemento:',dados);
        print('Retornando ao menu...');

#Encerrando loop do menu
    if option_menu == 5:
        print('Encerrando programa!')
        break;
            
