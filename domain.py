class DataTable:
    """ Representa uma Tabela de dados

        Essa classe representa uma tabela de dados do portal
        da transparência. Deve ser capaz de validar linhas
        inseridas de acordo com as colunas que possui. As
        linhas inseridas ficam registradas dentro dela.

        Attributes:
            name: Nome da tabela
            columns: [lista de colunas]
            data: [Lista de dados]

    """
    def __init__(self, name):
        """ Constructor

            Args:
                name: Nome da Tabela
        """
        self._name = name
        self._columns = []
        self.data = []
        self._references = []
        self._referenced = []

    def add_column(self, name, kind, description):
        column = Column(name, kind, description)
        self._columns.append(column)
        return column

    def add_references(self, name, to, on):
        """ Cria uma referência dessa tabela para outra tabela

        :param name: nome da relação
        :param to: instância da tabela apontada
        :param on: instância coluna em que existe a relação

        """
        relationship = Relationship(name, self, to, on)
        self._references.append(relationship)

    def add_referenced(self, name, by, on):
        """ Cria uma refererência para outra tabela que aponta para essa

        :param name: nome da realação
        :param by: instância da tabela que aponta para o esquema
        :param on: instância coluna em que existe a relação
        """

        relationship = Relationship(name, by, self, on)
        self._referenced.append(relationship)


class Column:
    """ Representa uma coluna em um DataTable

        Essa classe contém as informações de uma coluna
        e deve validar um dado de acordo com um tipo de
        dado configurado no construtor.

        Attributes:
            name: Nome da coluna
            kind: Tipo de dado (varchar, bigint, numeric)
            description: Descrição da coluna

    """

    def __init__(self, name, kind, description=""):
        """Cpnstructor

            Args:
                :param name: Nome da coluna
                :param kind: Tipo de dado (varchar, bigInt, numeric)
                :param description: Descrição da coluna
        """
        self._name = name
        self._kind = kind
        self._description = description


class Relationship:
    """ Classe que representa um relacionamento entre DataTables

        Essa classe tem todas as informações que identificam um relacionamento entre tabelas.
        Em qual coluna ele existe, de onde vem e para onde vai

    """
    def __init__(self, name, _from, to, on):
        """ Constructor

        :param name: Nome
        :param _from: Tabela de onde sai
        :param to: Tabela para onde vai
        :param on: instância da coluna onde existe
        """

        self._name = name
        self._from = _from
        self._to = to
        self._on = on


