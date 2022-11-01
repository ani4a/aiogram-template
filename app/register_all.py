from app import filters, handlers


def register_all(dp):
    filters.register(dp)
    handlers.register(dp)