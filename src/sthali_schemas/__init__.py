import json
import typing

import pydantic
import yaml

import sthali_db


class Field(pydantic.BaseModel):
    name: str
    type: type


class Types:
    any = typing.Any
    none = None
    bool = bool
    true = True
    false = False
    str = str
    int = int
    float = float
    list = list
    dict = dict


class ConfigException(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)


def get_type(type_str: str) -> type:
    return str
#     type_str = type_str.strip().lower()
#     try:
#         return getattr(Types, type_str)
#     except AttributeError as exception:
#         raise ConfigException("Invalid type") from exception


def load_and_parse_spec_file(spec_file_path: str) -> list[Field]:
    fields: list[Field] = []
    spec_dict = load_spec_file(spec_file_path)

    for resource in spec_dict["resources"]:
        for field in resource["fields"]:
            fields.append(Field(name=field["name"], type=get_type(field["type"])))


            # if isinstance(field["type"], str):
            #     field["type"] = get_type(field["type"])
            # elif isinstance(field["type"], list):
            #     types_list = tuple(get_type(type) for type in field["type"])
            #     field["type"] = typing.Union[types_list]  # type: ignore
            # else:
            #     raise ConfigException("Invalid field type")
            # if "has_default" in field:
            #     field["has_default"] = get_type(field["has_default"])
            # # fields  .append(field)
    return fields


def load_spec_file(file_path: str) -> dict[str, typing.Any]:
    *_, file_extension = file_path.split(".")
    if file_extension not in ["yaml", "yml", "json"]:
        raise ConfigException("Invalid file extension")

    with open(file_path, "r", encoding="utf-8") as spec_file:
        return (yaml.safe_load(spec_file), json.load(spec_file))[file_extension == "json"]
