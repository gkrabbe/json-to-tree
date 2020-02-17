from colorama import Fore, Style, init

init()


def json_to_tree(key, value, key_stype=Fore.GREEN, value_stype=Fore.WHITE, **args):
       
    tp = type(value)
    if(tp == dict):
        _value = ""
        for k, v in value.items():
            _value += json_to_tree(key=str(k), value=v, type="recall")

    elif(tp == list):
        _value = ""
        for k, v in enumerate(value):
            _value += json_to_tree(key=str(k), value=v, type="recall")
    else:
        _value = f"{value_stype}{value}{Style.RESET_ALL}"

    space_key = " "*len(key)
    multi = False
    final = "\n"

    if(args.get("type") == "recall"):
        final += f"-- "

    final += f"{key_stype}{key}{Style.RESET_ALL}"

    for var in _value.splitlines():
        if(not var.strip()):
            continue

        if(not var.strip().startswith(('--','|'))):
            if(multi):
                final += f"\n   | {space_key}{var}"
            else:
                final += f": {var}"
                multi = True
        else:
            final += f"\n   |{var}"
            multi = False

    return final

