minimize.py
============

Program used in the article:
[The ghosts of forgotten things: A study on size after forgetting](https://arxiv.org/abs/2005.04123)

It computes the redundant and superredundant clauses of a formula. It
optionally computes the minimal-size formulae equivalent to it. It optionally
forgets a variable and computes the minimal-size formulae expressing
forgetting. Being aimed at the short example formulae in the article, it is
simple rather than efficient.


Input
-----

The formula and variable to forget are passed from the commandline or in a
file. For example:

```
minimize.py -f -minimal -forget c 'a=bc' 'c->d' 'da'
minimize.py -t test1.py
```

In the first form, ``c`` is the variable to forget, ``'a=bc' 'c->d' 'da'``
is the formula:

- ``da`` is the clause *d v a*
- ``c->d`` is the clause *-c v d*
- ``a=bc`` stands for the clauses *-a v b, -a v c, -b v -c v a*

In the second form, ``test1.py`` is a file that contains a label (an arbitrary
string) followed by the same arguments as in the commandline, like in the
following example.

```
analyze(
    'an example',
    '-minimal',
    '-forget', 'b',
    'ab->c', 'be', 'cd=e'
)
```

Variables can only be single letters. This limits the number of variables, but
avoids the need of separators between them.


Output
------

- the formula in its clausal form: ``ab->c`` and ``cd=e`` are converted
into clauses:
the first becomes ``-a-bc``,
the second ``-de-c, -ec, -ed``
(the disjunction sign ``v`` between literals is implicit in the output)

- the resolution closure of the formula

- the set of its prime implicates

- its redundant clauses

- its superredundant clauses

- if requested by ``-minimal``, its smallest equivalent formulae

- if requested by ``-forget variable``, a formula expressing forgetting
that variable; namely, the set of prime implicates of the formula that do not
contain the variable; also the smallest formulae equivalent to it are produced


Internals
---------

- Clauses are converted from strings to sets of literals, where each literal is
  a string like ``-a`` or ``b``. Formulae are sets of clauses.

- ``resolve(a,b)`` calculates the resolution of the two clauses
  ``a`` and ``b``. The result is not a clause but a set: the empty set if the
  two clauses do not resolve, otherwise the singleton comprising the clause
  they resolve into. According to the convention used in this article, two
  clauses do not resolve if they would normally resolve in a tautology.

- The program hinges around ``close()``, which calculates the
  resolution closure of a formula. It works by adding the resolution of every
  two clauses of the formula to it until it no longer changes.

  It optionally removes all clauses that strictly contain others at each step.
  The result is the set of prime implicates of the formula. Equality of such
  sets is how equivalence is checked.

- Redundant clauses are determined by removing each clause from the formula and
  checking equivalence. The function also takes the clauses that are to be
  checked for redundancy as an optional second argument; the default is to
  check all of them.

- Superredundant clauses are determined by checking redundancy of the clauses
  of the formula in its resolution closure. This is the definition of
  superredundancy.

- The minimal-size formulae equivalent to the given one are calculated by
  iterating over the sets of prime implicates. This is correct because the
  minimal-size formulae are all sets of prime implicates.

  After finding all prime implicants as described above, their sets are checked
  for equivalence with the formula in order of increasing number of clauses.
  Checking stops when the number of clauses is greater than the size of the
  formula, which implies that the sets that would be generated afterwards are
  larger than the formula.

  This mechanism produces some formulae that are equivalent to the given
  formula, including all minimal ones. A further function selects the formulae
  of minimal size.

  Optionally, a set of clauses known to be in all minimal equivalent formulae
  can be passed to avoid the equivalence check on subsets not containing all of
  them.

- Forgetting a variable is done by removing all clauses containing it from the
  set of prime implicates. The smallest formulae equivalent to the result is
  calculated as for the original formula.

