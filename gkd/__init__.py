import sys
try:
    import dill as pickle
except ImportError:
    import pickle
import os


import pathlib
from contextlib import contextmanager
from wisepy2 import wise


@contextmanager
def _load_config():
    path = pathlib.Path("~/.GKD-db").expanduser()
    if not path.exists():
        path.parent.mkdir(mode=0o777, exist_ok=True, parents=True)    
        config = {}
    else:
        
        with path.open("rb") as f:
            config = pickle.loads(f.read())
    try:
        yield config
    finally:
        with path.open("wb") as f:
            f.write(pickle.dumps(config))

def call_op(config: dict, rt, op, args):
    config = config.setdefault(rt, {})
    
    def _get(config, x):
        return config.get(x, '')
    
    
    def _set(config: dict, x, v):
        config[x] = v
        return ''

    
    def _push(config: dict, x, v):
        stack = config.setdefault(x, [])
        stack.append(v)
        return ''
    
    def _pop(config: dict, x):
        stack = config.setdefault(x, [])
        try:
            return stack.pop()
        except IndexError:
            return ''
    
    def _reset(config):
        config.clear()
        return ''

    def _uuid(config):
        from uuid import uuid4
        return uuid4()

    def _call(config, f, arg):
        return eval(f)(arg)
        
    def _bnf(config, file_in):
        import paperbnf
        with open(file_in) as f:
            src = f.read()
        return paperbnf.parse(src, file_in)

    def _createDirFor(config, file_in):
        pathlib.Path(file_in).parent.mkdir(mode=0o777, exist_ok=True, parents=True)
        return ''

    return locals().get("_" + op, lambda *_: '')(config, *args)



def main(*args, op: str = "", rt : str = ""):
    if not op or not rt:
        return ''
    

    with _load_config() as config:
        print(call_op(config, op=op, rt=rt, args=args))


def callmain():
    wise(main)()
    
