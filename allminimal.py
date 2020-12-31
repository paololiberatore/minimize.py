analyze(
    'a clause may be superredundant but in all minimal equivalent formulae\n\n'
    'the only minimal formula equivalent to {a, a=b} is {a, b};\n'
    'therefore, a is in all minimal equivalent formulae;\n'
    'it is however superredundant: a and a=b imply b, which implies a',
    '-minimal',
    'a', 'a=b'
)

