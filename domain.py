from decimal import Decimal


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

    def _get_name(self):
        print("Getter executado!")
        return self._name

    def _set_name(self, _name):
        print("Setter executado!")
        self._name = _name

    def _del_name(self):
        print("Deletter executado!")
        raise AttributeError("Não pode deletar esse atributo")

    name = property(_get_name, _set_name, _del_name)


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
        """Constructor

            Args:
                :param name: Nome da coluna
                :param kind: Tipo de dado (varchar, bigInt, numeric)
                :param description: Descrição da coluna
        """
        self._name = name
        self._kind = kind
        self._description = description
        self._is_pk = False

    def __str__(self):
        _str = "Col: {} : {} {}".format(self._name, self._kind, self._description)

        return _str

    def _validate(cls, kind, data):
        if kind == "bigint":
            if isinstance(data, int):
                return True
            return False
        elif kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif kind == 'numeric':
            try:
                val = Decimal(data)
            except:
                return False
            return True

    validate = classmethod(_validate)


class PrimaryKey(Column):
    def __init__(self, table, name, kind, description=""):
        super().__init__(name, kind, description=description)
        self._is_pk = True

    def __str__(self):
        _str = "Col: {} : {} {} ".format(self._name, self._kind, self._description)
        return "{} - {}".format('PK', _str)


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
