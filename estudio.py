import sqlite3

class EpisodioPodcast:
    def __init__(self, db_name='estudioPodcast.db'):
        self.db_name = db_name
        self.conexao = self.criar_conexao()

    def criar_conexao(self):
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS episodios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                apresentador TEXT,
                duracao REAL,
                descricao TEXT,
                preco REAL
            )
        ''')
        conexao.commit()
        return conexao

    def cadastrarEpisodio(self, titulo, apresentador, duracao, descricao, preco):
        cursor = self.conexao.cursor()
        cursor.execute('INSERT INTO episodios (titulo, apresentador, duracao, descricao, preco) VALUES (?, ?, ?, ?, ?)',
                       (titulo, apresentador, duracao, descricao, preco))
        self.conexao.commit()
        print('Episódio cadastrado com sucesso.')

    def consultarEpisodios(self):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT * FROM episodios')
        episodios = cursor.fetchall()
        for episodio in episodios:
            print(f'ID: {episodio[0]}, Título: {episodio[1]}, Apresentador: {episodio[2]}, Duração: {episodio[3]}, Descrição: {episodio[4]}, Preço: {episodio[5]}')

    def deletarEpisodio(self, id):
        cursor = self.conexao.cursor()
        cursor.execute('DELETE FROM episodios WHERE id = ?', (id,))
        self.conexao.commit()
        if cursor.rowcount > 0:
            print('Episódio deletado com sucesso.')
        else:
            print('Erro: Episódio não encontrado.')

    def atualizarEpisodio(self, id, titulo=None, apresentador=None, duracao=None, descricao=None, preco=None):
        cursor = self.conexao.cursor()
        updates = []
        params = []

        if titulo:
            updates.append("titulo = ?")
            params.append(titulo)
        if apresentador:
            updates.append("apresentador = ?")
            params.append(apresentador)
        if duracao:
            updates.append("duracao = ?")
            params.append(duracao)
        if descricao:
            updates.append("descricao = ?")
            params.append(descricao)
        if preco:
            updates.append("preco = ?")
            params.append(preco)

        if updates:
            sql = f"UPDATE episodios SET {', '.join(updates)} WHERE id = ?"
            params.append(id)
            cursor.execute(sql, params)
            self.conexao.commit()
            print('Episódio atualizado com sucesso.')
        else:
            print('Nenhuma atualização realizada.')

    def consultarEpisodioIndividual(self, id):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT * FROM episodios WHERE id = ?', (id,))
        episodio = cursor.fetchone()
        if episodio:
            print(f'ID: {episodio[0]}, Título: {episodio[1]}, Apresentador: {episodio[2]}, Duração: {episodio[3]}, Descrição: {episodio[4]}, Preço: {episodio[5]}')
        else:
            print('Erro: Episódio não encontrado.')

    def consultarEpisodiosPorDuracao(self, duracao_min, duracao_max):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT * FROM episodios WHERE duracao BETWEEN ? AND ?', (duracao_min, duracao_max))
        episodios = cursor.fetchall()
        for episodio in episodios:
            print(f'ID: {episodio[0]}, Título: {episodio[1]}, Duração: {episodio[3]}')

    def calcularReceitaEsperada(self, id, estimativa_ouvintes):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT preco FROM episodios WHERE id = ?', (id,))
        episodio = cursor.fetchone()
        if episodio:
            receita = episodio[0] * estimativa_ouvintes
            print(f'Receita esperada para o episódio ID {id}: R$ {receita:.2f}')
        else:
            print('Erro: Episódio não encontrado.')

def main():
    episodio = EpisodioPodcast()
    opcao = 0