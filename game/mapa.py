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


