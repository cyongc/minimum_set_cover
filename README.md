# minimum_set_cover

main.py implements an algorithm in an attempt to solve NP-complete problem, minimum set cover. Algorithm is written in Python 3 and uses the anytree module to implement the set cover tree. If module installation is needed, run: $ pip install anytree. PyCharm should take care of the rest.

**Set Cover recap..**
The set cover problem takes as input a collection S of m subsets of the universal set U = {1, . . . , n}. The goal is to find the smallest subset S<sub>0</sub> ∈ S such that the union of the subsets in S<sub>0</sub> is U. Set cover arises whenever you try to efficiently acquire or represent items which have been packaged in a fixed set of lots. You want to obtain all the items while buying as few lots as possible. Finding a cover is easy, for you can buy one of each lot. However, by finding a small set cover you can avoid buying unnecessary lots.

**Regarding data sets..**
Each file has a name like “s-X-10-20”, meaning that the file contains a set of 20 subsets of special type X, with U = {1, . . . , 10}.  The first line of each file will contain the size of the universal set, and the second line the number of subsets in S. Each subsequent line contains a list of the elements in the associated subset.

Completed for CSE 373 with Steven Skiena
