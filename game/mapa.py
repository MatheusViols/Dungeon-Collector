from bau import Bau

class Mapa:
    def __init__(self):
        self.tamanho_tile = 54
        self.imagens = {
                '.': 'caminho',
                '#': 'parede',
                'T': 'caminho',
                }
        self.layout = [
                "##############",
                "#....#.#...T.#",
                "#.####.#####.#",
                "#............#",
                "#.####.#####.#",
                "#.####T#####.#",
                "#.##########.#",
                "#...T........#",
                "#.##########.#",
                "#.#.########.#",
                "#.T.########T#",
                "##############",
                ]

        self.baus = []
        self.criar_baus()

    def criar_baus(self):
        for indice_linha, linha in enumerate(self.layout):
            for indice_coluna, tile in enumerate(linha):
                centro = (indice_coluna * self.tamanho_tile + self.tamanho_tile // 2, indice_linha * self.tamanho_tile + self.tamanho_tile // 2)
                if tile == "T":
                    self.baus.append(Bau(centro))


    def draw(self, screen):
        for indice_linha, linha in enumerate(self.layout):
            for indice_coluna, tile in enumerate(linha):
                posicao = (indice_coluna * self.tamanho_tile, indice_linha * self.tamanho_tile)
                screen.blit(self.imagens[tile], posicao)

    def andavel(self, novo_x, novo_y, WIDTH, HEIGHT):

        indice_linha = int(novo_y // self.tamanho_tile)
        indice_coluna = int(novo_x // self.tamanho_tile)

        if indice_linha < 0 or indice_linha >= len(self.layout):
            return False
        elif indice_coluna < 0 or indice_coluna >= len(self.layout[0]):
            return False

        andavel = self.layout[indice_linha][indice_coluna] == "." or self.layout[indice_linha][indice_coluna] == "T"

        return andavel






