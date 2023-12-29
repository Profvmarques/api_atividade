from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome="Benjamin", idade=40)
    pessoa.save()
    print(pessoa)


def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)


def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome="Benamin").first()  # Add parentheses here
    if pessoa:
        pessoa.nome = "Fabiana"
        pessoa.idade = 39
        pessoa.save()


def excluir_pessoas():
    pessoa = Pessoas.query.filter_by(nome="Fabiana").first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoas()
    excluir_pessoas()
    consulta_pessoas()
