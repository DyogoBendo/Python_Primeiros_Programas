# coding: UTF-8
import os
for meta_file in os.listdir('../data/meta-data'):
    print(meta_file)


def extract_entity_name(filename):
    return filename.split('.')[0]


print(extract_entity_name('Licitacao.txt'))


def read_meta_data(path):
    data = open(path, "rt")
    meta_data = []
    for line in data:
        line_data = line.split('\t')
        meta_data.append((line_data[0],
                         line_data[1],
                         line_data[2]))

    data.close()
    return meta_data


print(read_meta_data('../data/meta-data/Instituicao.txt'))


def read_lines(filename):
    _file = open(os.path.join("../data/meta-data", filename), "rt")
    data = _file.read().split("\n")
    _file.close()
    return data


def read_metadata(filename):
    metadata = []
    for column in read_lines(filename):
        if column:
            values = column.split('\t')
            nome = values[0]
            tipo = values[1]
            desc = values[2]
            metadata.append((nome, tipo, desc))
    return metadata


""""
def main():
    meta = {}
    for meta_data_file in os.listdir("data/meta-data"):
        table_name = extract_entity_name(meta_data_file)
        meta[table_name] = read_metadata(meta_data_file)
        for key, val in meta.items():
            print("Entidades {}".format(key))
            print("Attributes: ")
            for col in val:
                print(" {}: {}".format(col[1], col[0]))

"""


def main():
    # dicionario nome entidade -> atributos
    meta = {}

    # dicionario identificador -> nome entidade
    keys = {}

    for meta_data_file in os.listdir("../data/meta-data"):
        table_name = extract_entity_name(meta_data_file)
        atributtes = read_metadata(meta_data_file)
        identifier = atributtes[0][0]

        meta[table_name] = atributtes
        keys[identifier] = table_name
    for key, val in meta.items():
        for col in val:
            print(col)
            if col[0] in keys:
                if not col[0] == meta[key][0][0]:
                    print("Entiade {} -> {}".format(key, col[0]))


if __name__ == "__main__":
    main()
