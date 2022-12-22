# Aleksei Zabirnik <azabirnik@gmail.com>
# Avito Academy homework 4

class Pokemon:
    """ Base class for pokemons to use in pokedex """
    def __init__(self, name: str, poketype: str) -> None:
        self.name = name
        self.poketype = poketype

    def __str__(self) -> str:
        return f'{self.name}/{self.poketype}'


class EmojiMixin:
    emoji = {
        'grass': '🌿',
        'fire': '🔥',
        'water': '🌊',
        'electric': '⚡'
    }

    def __str__(self) -> str:
        """ The mixin that adds emoji to output """
        unformatted_str = super().__str__()
        for i in range(len(unformatted_str)):
            if unformatted_str[i] == '/':
                pokemon_type = unformatted_str[i+1:]
                if pokemon_type in self.emoji.keys():
                    return unformatted_str[:i+1] + self.emoji[pokemon_type]
        return unformatted_str


class EmojiPokemon(EmojiMixin, Pokemon):
    """ Pokemons with emojis """


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur)

    bulbasaur = EmojiPokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur)
