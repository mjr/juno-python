import re


def _unpack(data):
    if isinstance(data, dict):
        return data.items()
    return data


def to_snake_case(value):
    """
    Convert camel case string to snake case
    :param value: string
    :return: string
    """
    first_underscore = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", value)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", first_underscore).lower()


def keys_to_snake_case(content):
    """
    Convert all keys for given dict to snake case
    :param content: dict
    :return: dict
    """
    return {to_snake_case(key): value for key, value in _unpack(content)}


def to_camel_case(value):
    """
    Convert the given string to camel case
    :param value: string
    :return: string
    """
    content = value.split("_")
    return content[0] + "".join(
        word.capitalize() for word in content[1:] if not word.isspace()
    )


def keys_to_camel_case(content):
    """
    Convert all keys for given dict to camel case
    :param content: dict
    :return: dict
    """
    return {to_camel_case(key): value for key, value in _unpack(content)}


def parse_keys(data, formatter):
    """
    Convert all keys for given dict/list to passed formatter recursively
    :param data: dict | list
    :param formatter: function
    :return: dict | list
    """
    if not isinstance(data, (list, dict)):
        raise TypeError("Invalid data type, use list or dict")

    formatted = type(data)()

    is_dict = lambda x: type(x) == dict
    is_list = lambda x: type(x) == list

    for key, value in _unpack(formatter(data)):
        if is_dict(value):
            formatted[key] = parse_keys(value, formatter)
        elif is_list(value) and len(value) > 0:
            formatted[key] = []
            for val in value:
                if isinstance(val, (list, dict)):
                    val = parse_keys(val, formatter)
                formatted[key].append(val)
        else:
            formatted[key] = value
    return formatted


def camelize(data):
    """
    Convert all keys for given dict from 'snake case' to 'camel case'
    :param data: dict
    :return: dict
    """
    return parse_keys(data, keys_to_camel_case)


def underscoreize(data):
    """
    Convert all keys for given dict from 'camel case' to 'snake case'
    :param data: dict
    :return: dict
    """
    return parse_keys(data, keys_to_snake_case)
