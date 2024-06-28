import typing

import pydantic


class Types(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra='allow')

    type_str: typing.Annotated[type, pydantic.Field(default=str, title="str"),]
    type_int: typing.Annotated[type, pydantic.Field(default=int, title="int"),]
    type_float: typing.Annotated[type, pydantic.Field(default=float, title="float"),]
    type_list: typing.Annotated[type, pydantic.Field(default=list, title="list"),]
    type_dict: typing.Annotated[type, pydantic.Field(default=dict, title="dict"),]


print([i for i in Types.model_fields])

# setattr()

print([i for i in Types.model_fields])

# breakpoint()

# x = Types(_int=int)




#     # def get_type(self, name: str) -> type | None:
#     #     try:
#     #         return getattr(self, f"_{name}")
#     #     except AttributeError:
#     #         pass


# x = [
#     ("any", typing.Any),
#     ("none", None),
#     ("bool", bool),
#     ("true", True),
#     ("false", False),
# ]

# for name, value in x:
#     setattr(Types, name, value)


x = 1
