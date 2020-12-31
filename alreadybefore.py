analyze(
    'splitting a clause does not make a clause superirredundant if any of\n'
    'its parts are already superredundant alone\n\n'
    'the original formula is F = {a v b, a = c};\n'
    'this run proves that a is superredundant in F u {a}',
    'a', 'ab', 'a=c'
)

analyze(
    'splitting a clause does not make a clause superirredundant if any of\n'
    'its parts are already superredundant alone\n\n'
    'this is the formula F after splitting a v b into a v x and -x v b;\n'
    'the first clause a v x is superredundant',
    'ax', '-xb', 'a=c'
)
