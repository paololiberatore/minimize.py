analyze(
    'resolving out is not minimally forgetting: '
    'may generate redundant clauses\n\n'
    'this run shows that {a v b v x, -x v c, a v c} is minimal and that\n'
    'forgetting x is expressed by {a v c}; resolving out x also generates\n'
    'a v b v c, where b is redundant (not shown by this run)',
    '-minimal',
    '-forget', 'x',
    'abx', '-xc', 'ac'
)

analyze(
    'resolving out is not minimally forgetting: '
    'may generate redundant literals\n\n'
    'the difference from the previous example is that the clause generated\n'
    'by resolving x out is not redundant but contains a redundant literal:\n'
    'resolving out x produces a v b v c; '
    'the clauses a v y and -y v b v -c imply\na v b v -c; '
    'therefore, a v b follows; '
    'this proves that c is redundant\nin a v b v c\n\n'
    'this run shows that the original formula is minimal and that\n'
    'forgetting x is expressed by {a v b, a v y, -y v b v -c}',
    '-minimal',
    '-forget', 'x',
    'ax', '-xbc', 'ay', '-yb-c'
)


analyze(
    'resolving out may generate irredundant but non-minimal formulae\n\n'
    'this run shows only that the formula is minimal',
    '-minimal',
    'a->b', 'a->c', 'a-b-c',
    'bx', '-xd',
    'cd'
)
analyze(
    'resolving out may generate irredundant but non-minimal formulae\n\n'
    'the formula in this run is obtained by resolving x out from the\n'
    'previous: it is irredundant but not minimal',
    '-minimal',
    'a->b', 'a->c', 'a-b-c',
    'bd',
    'cd'
)

