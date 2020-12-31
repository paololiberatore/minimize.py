analyze(
    'a minimal formula comprising only superredundand clauses\n\n'
    'the formula is a loop of variables: a->b->c->a; it is minimal, as is\n'
    'its equivalent opposite loop c->b->a->c; equivalence makes all clauses\n'
    'superredundant\n'
    'this formula not only shows that a superredundant clause may be\n'
    'in a minimal formula, but also that all clauses of a minimal formula\n'
    'may be superredundant',
    '-minimal',
    'a->b', 'b->c', 'c->a'
)
