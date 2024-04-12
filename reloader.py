import sys, typing
sys.dont_write_bytecode = True

def resolve_path(path: str) -> str:
    if path:
        return path.replace("\\", ".").replace("/", ".")


def reload_module(path: str, returns: typing.Sequence[str] | None) -> typing.Sequence[typing.Callable] | None:
    if isinstance(path, str):
        path = resolve_path(path)
    else:
        raise ValueError("Path argument must be `str`.")
    
    # removing cached module from system
    if path in sys.modules:
        del sys.modules[path]

    # re-importing module
    try:
        exec(f"import {path} as module")
    except Exception as error:
        return print(f"Failed to reload {path}. {type(error).__name__}: {error}")
    
    # returning callables
    if returns:
        return [getattr(sys.modules[path], x) for x in returns]
