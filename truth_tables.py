from itertools import product
from inspect import signature


def implies(a: bool, b: bool) -> bool:
    """a implies b."""
    return (not a) or (a and b)


def iff(a: bool, b: bool) -> bool:
    """(a implies b) and (b implies a)."""
    return implies(a, b) and implies(b, a)


def func1(a: bool, b: bool, c: bool) -> bool:
    return implies(implies(a, implies(b, c)), implies(a and b, c))


def func2(a: bool, b: bool, c: bool) -> bool:
    return (not ((not a) or ((not b) or c))) or ((not (a and b)) or c)


def func3(a: bool, b: bool, c: bool) -> bool:
    return not (not (a and (b and (not c))) and ((a and b) and (not c)))


if __name__ == "__main__":
    funcs = [func1, func2, func3]

    # Funcs must take the same # of params. If not, just make a dummy param.
    n_params = len(signature(funcs[0]).parameters)

    names = [chr(97 + i) for i in range(n_params)] + [f"func{i}" for i in range(len(funcs))]
    print("\t".join(names))
    print("-" * 8 * len(names))

    bools = (True, False)
    for args in product(*(bools for i in range(n_params))):
        outputs = [f(*args) for f in funcs]

        bs = list(args) + outputs
        print("\t".join([str(i) for i in bs]))
