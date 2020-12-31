#!/usr/bin/env python3
#
# resolution closure of a CNF formula
# prime implicates
# redundant and superredundant clauses
# minimal formulae
# forget a variable, minimal expression of forget

import itertools
import sys


# make a formula from a collection of lists

def clause(s):
    if isinstance(s, list):
        return frozenset([frozenset(s)])
    elif '=' in s:
        h = s.split('=')
        return clause(h[0] + '->' + h[1]) | clause(h[1] + '->' + h[0])
    elif '->' in s:
        all = frozenset()
        body = set()
        sign = '-'
        for c in s:
            if c == '>':
                sign = ''
            elif c == '-':
                pass
            elif sign == '-':
                body |= {sign + c}
            else:
                all |= {frozenset(body | {sign + c})}
        return all
    else:
        all = frozenset()
        sign = ''
        for c in s:
            if c == '-':
                sign = '-'
            else:
                all |= {sign + c}
                sign = ''
        return frozenset({all})

def formula(*l):
    return set().union(*{clause(x) for x in l})


# print a formula 

def formulaprint(a, l = None, b = True):
    if l:
        print(l, end = '')
    if b:
        print('(' + str(formulasize(a)) + ')', '', end = '')
    for c in a:
        print('(' + ' '.join(c) + ')', '', end = '')
    print()


# print a set of formulae

def setprint(a, l = None, b = True):
    if l:
        print(l)
    for s in a:
        formulaprint(s, None, b)


# size of a formula, as total occurrencies of variables

def formulasize(a):
    return sum([len(x) for x in a])


# check whether a clause is a tautology

def tautology(c):
    for l in c:
        if '-' + l in c:
            return True
    return False


# resolve two clauses; emptyset if they don't resolve or resolve to a tautology

def resolve(a, b):
    for x in a:
        for y in b:
            if x == '-' + y or '-' + x == y:
                r = a.difference([x]).union(b.difference([y]))
                return set() if tautology(r) else set({r})
    return set()


# minimal (not containing others) clauses of a formula

def minimal(s):
   r = set()
   for c in s:
       for d in s:
           if d < c:
               break
       else:
           r |= {c}
   return r


# resolution closure, optionally minimized: close(s, True) = prime implicates

def close(s, minimize = False):
    n = minimal(s) if minimize else s.copy()
    r = set()
    while n != r:
        r = n.copy()
        for a in r:
           for b in r:
              n |= resolve(a, b)
        if minimize:
            n = minimal(n)
    return n


# redundant clauses of a formula

def redundant(s, r = None):
    res = set()
    m = close(s, True)
    for c in s if r == None else r:
        w = s.copy()
        w.remove(c)
        if m == close(w, True):
            res |= {c}
    return res


# superredundant clauses of a formula

def superredundant(s):
    return redundant(close(s), s)


# remove all clauses containing the variables v from the formula s
# same as forgetting if done on the resolution closure or prime implicates

def removevariables(s, v):
    res = set()
    for c in s:
        for x in v:
            if not x in c and not '-' + x in c:
                res |= {c}
    return res


# some equivalent formulae of same size or equal, including all minimal ones

def shorter(s, necessary = set()):
    res = set()
    m = close(s, True)
    q = list(m)
    t = itertools.chain.from_iterable(itertools.combinations(q, r) \
        for r in range(len(q)+1))
    for e in t:
        if not necessary.issubset(e):
            continue
        if len(e) > formulasize(s):
            break
        if formulasize(e) > formulasize(s):
            continue
        if m != close(frozenset(e), True):
            continue
        res |= {e}
    return res


# set of minimal-size formulae equivalent to a formula

def shortest(e):
    m = -1
    for s in e:
        if m == -1 or formulasize(s) < m:
            t = set({s})
            m = formulasize(s)
        if (formulasize(s) == m):
            t |= {s}
    return t


# analyze a formula

def analyze(d, *s):
    print('#################################################################')
    print('##', d.replace('\n', '\n## '))
    print()

    minimize = False
    if s[0] == '-minimal':
        minimize = True
        s = s[1:]
    x = None
    if s[0] == '-forget':
        x = s[1]
        s = s[2:]
    f = formula(*s)

    # resolution closure and prime implicates
    formulaprint(f, 'original formula:\n')
    r = close(f)
    formulaprint(r, 'resolution closure:\n')
    m = minimal(r)
    formulaprint(m, 'prime implicates:\n')

    # redundant and superredundant clauses
    print('==========')
    formulaprint(redundant(f), 'redundant clauses:\n', False)
    formulaprint(superredundant(f), 'superredundant clauses:\n', False)

    # determine minimal-size equivalent formulae
    if minimize:
        print('==========')
        print('size of formula:', formulasize(f))
        setprint(shortest(shorter(f)), 'minimal equivalent formulae:')
        # setprint(shortest(shorter(f, f - superredundant(f))), \
        #    'minimal equivalent formulae:')

    # forget x
    if (x == None or x == ''):
        print()
        return
    print('==========')
    f = removevariables(m, x)
    formulaprint(f, 'forgetting ' + ', '.join(x) + ':\n')
    setprint(shortest(shorter(f)), 'minimal equivalent formulae:')
    print()


# do not analyze a formula

def donotanalyze(d, x, *s):
    return


# commandline arguments

if len(sys.argv) <= 1 or sys.argv[1] == '-h':
    if len(sys.argv) <= 1:
        print('no argument')
    print('usage:')
    print('\tminimize.py [-t] testfile.py')
    print('\tminimize.py -f [-minimal] [-forget var] clause clause...' )
    print('\t\tclause: ab->c, ab=c, abc (= a or b or c)')
elif sys.argv[1] == '-f':
    analyze('cmdline formula', *sys.argv[2:])
elif sys.argv[1] == '-t':
    exec(open(sys.argv[2]).read())
else:
    exec(open(sys.argv[1]).read())

