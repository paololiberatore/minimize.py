analyze(
    'an irredundant clause may be superredundant\n\n'
    'a is superredundant but irredundant',
    '-minimal',
    'a', 'a->b', 'b->a'
)
