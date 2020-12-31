analyze(
    'resolution may generate clauses that are not minimal\n\n'
    'a v b v e and -e v c v d resolve into a v b v c v d,\n'
    'which is not minimal since the formula also contains a v b v c',
    'abc', 'abe', '-ecd'
)
