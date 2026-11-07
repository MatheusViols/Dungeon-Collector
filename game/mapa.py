class Mapa:
    def __init__(self):
        self.tamanho_tile = 54
        self.imagens = {
                '.': 'caminho',
                '#': 'parede',
                'T': 'tesouro',
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

    def draw(self, screen):
        for indice_linha, linha in enumerate(self.layout):
            for indice_coluna, tile in enumerate(linha):
                screen.blit(self.imagens[tile], (indice_coluna * self.tamanho_tile, indice_linha * self.tamanho_tile))

    def andavel(self, novo_x, novo_y, WIDTH, HEIGHT):

        indice_linha = int(novo_y // self.tamanho_tile)
        indice_coluna = int(novo_x // self.tamanho_tile)

        if indice_linha < 0 or indice_linha >= len(self.layout):
            return False
        elif indice_coluna < 0 or indice_coluna >= len(self.layout[0]):
            return False

        andavel = self.layout[indice_linha][indice_coluna] == "." or self.layout[indice_linha][indice_coluna] == "T"

        return andavel






