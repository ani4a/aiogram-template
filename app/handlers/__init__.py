from . import start


def register(dp):
    handlers = [
        start,
    ]

    for i in handlers:
        i.register(dp)
