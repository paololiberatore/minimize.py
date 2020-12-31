analyze(
    'a clause may not maintain its superirredundancy if it resolves with\n'
    'both parts of the clause that is split\n\n'
    'this run shows a formula where the first clause a v b v c v d is\n'
    'superirredundant before splitting the second clause -a v b -c v d',
    'abcd', '-ab-cd', 'ae', '-e-a-c'
)

analyze(
    'a clause may not maintain its superirredundancy if it resolves with\n'
    'both parts of the clause that is split\n\n'
    'the first clause a v b v c v d resolves with both parts -a v b and\n'
    '-c v d of the second; it does not remain superirredundant after\n'
    'the split',
    'abcd', '-abx', '-x-cd', 'ae', '-e-a-c'
)

analyze(
    'a clause may not maintain its superirredundancy if it resolves with\n'
    'both parts of the clause that is split\n\n'
    'second shot: a v b v c v d is made superirredundant by splitting',
    'aby', '-ycd', '-abx', '-x-cd', 'ae', '-e-a-c'
)
