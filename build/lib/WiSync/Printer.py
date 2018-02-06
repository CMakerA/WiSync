__print_cache = []


def print_once(text: str):
    if text not in __print_cache:
        print(text)
        __print_cache.append(text)
