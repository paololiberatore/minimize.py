analyze(
    'an example of splitting a clause\n\n'
    'a formula that contains a superredundant clause: a v b v c',
    'abc', '-ad', '-cd', '-dac'
)

analyze(
    'an example of splitting a clause\n\n'
    'the formula where a v b v c is split into a v b v x and -x v c:\n'
    'the new clauses are superirredundant, the others remain so',
    'abx', '-xc', '-ad', '-cd', '-dac'
)

