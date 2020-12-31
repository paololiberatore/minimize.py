# similar to bothparts.py but c does not contain all variables of c1 v c2

analyze(
    'a v b v c v d is superirredundant before the split',
    'abcd', '-abe-cd', '-ea'
)

analyze(
    'but resolves with both parts: does not remain superirredundant',
    'abcd', '-abex', '-x-cd', '-ea'
)

analyze(
    'second shot: make it superirredundant by splitting',
    'aby', '-ycd', '-abex', '-x-cd', '-ea'
)
