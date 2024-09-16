def implies(p: bool, q: bool) -> bool:
    """Return True if p implies q is satisfied."""
    return (not p) or (p and q)


def iff(p: bool, q: bool) -> bool:
    """Return True if p implies q and q implies p."""
    return implies(p, q) and implies(q, p)


def func(p: bool, q: bool) -> bool:
    """Function to create truth table for."""
    return implies(p or (not q), p and q)


if __name__ == "__main__":
    print("P\tQ\tFunc")
    print("-" * 20)

    bools = (True, False)
    for p in bools:
        for q in bools:
            x = func(p, q)
            print(f"{p}\t{q}\t{x}")
