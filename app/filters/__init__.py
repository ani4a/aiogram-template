from . import is_admin


def register(dp):
    filters = [
        is_admin,
    ]

    for i in filters:
        i.register(dp)
