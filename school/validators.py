import re
from validate_docbr import CPF


def invalid_cpf(cpf):
    cpf_validator = CPF()
    return not cpf_validator.validate(cpf)


def invalid_name(name):
    return not name.replace(" ", "").isalpha()


def invalid_cellphone(cellphone):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    result = re.findall(model, cellphone)

    return not result
