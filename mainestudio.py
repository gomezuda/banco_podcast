from estudio import EpisodioPodcast
episodio = EpisodioPodcast()
opcao = 0

while opcao != 7:
        print('--- Estúdio de Podcast ---')
        print('1. Cadastrar Episódio')
        print('2. Consultar Episódios')
        print('3. Deletar Episódio')
        print('4. Atualizar Episódio')
        print('5. Consultar Episódio Individual')
        print('6. Consultar Episódios por Duração')
        print('7. Consultar Receita Esperada')
        print('8. Sair')
        opcao = int(input('Selecione uma opção: '))

        if opcao == 1:
            titulo = input('Título do Episódio: ')
            apresentador = input('Apresentador: ')
            duracao = float(input('Duração (em minutos): '))
            descricao = input('Descrição: ')
            preco = float(input('Preço: '))
            episodio.cadastrarEpisodio(titulo, apresentador, duracao, descricao, preco)

        elif opcao == 2:
            print('=== Episódios Cadastrados ===')
            episodio.consultarEpisodios()

        elif opcao == 3:
            id = int(input('Informe o ID do Episódio: '))
            episodio.deletarEpisodio(id)

        elif opcao == 4:
            id = int(input('Informe o ID do Episódio: '))
            print('Campos para atualização:')
            print('1. Título\n2. Apresentador\n3. Duração\n4. Descrição\n5. Preço')
            campo = int(input('Informe o campo que deseja atualizar: '))
            novo_valor = input('Informe o novo valor: ')

            if campo == 1:
                episodio.atualizarEpisodio(id, titulo=novo_valor)
            elif campo == 2:
                episodio.atualizarEpisodio(id, apresentador=novo_valor)
            elif campo == 3:
                episodio.atualizarEpisodio(id, duracao=float(novo_valor))
            elif campo == 4:
                episodio.atualizarEpisodio(id, descricao=novo_valor)
            elif campo == 5:
                episodio.atualizarEpisodio(id, preco=float(novo_valor))

        elif opcao == 5:
            id = int(input('Informe o ID do Episódio: '))
            episodio.consultarEpisodioIndividual(id)

        elif opcao == 6:
            duracao_min = float(input('Duração mínima: '))
            duracao_max = float(input('Duração máxima: '))
            episodio.consultarEpisodiosPorDuracao(duracao_min, duracao_max)
            
        elif opcao == 7:
            id = int(input('Informe o ID do Episódio: '))
            estimativa_ouvintes = int(input('Estimativa de ouvintes: '))
            episodio.calcularReceitaEsperada(id, estimativa_ouvintes)
            
        elif opcao == 8:
         id = int(input('Informe o ID do Episódio: '))
         estimativa_ouvintes = int(input('Informe a estimativa de ouvintes: '))
        # Calcula a receita potencial do episódio com base no preço e na quantidade de ouvintes estimada
         episodio.calcularReceitaEsperada(id, estimativa_ouvintes)

        elif opcao == 8:
            episodio.close()
            print("saindo")
            break
        else:
         print('Obrigado por usar o sistema de gerenciamento de estúdio de podcast!')
    
