from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome="Fabiana", idade=40)
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


def insere_usuarios(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_usuarios():
    usuario = Usuarios.query.all()
    print(usuario)


if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoas()
    #excluir_pessoas()
    #consulta_pessoas()
    insere_usuarios('Fabiana', 'fabi')
    insere_usuarios('vini', '123')
    insere_usuarios('ben', '123')
    consulta_usuarios()
