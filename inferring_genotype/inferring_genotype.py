import re
import io
import unittest
from collections import Counter


PARSER = re.compile(r'([(),])')
GEN_VARIANTS = ('AA', 'Aa', 'aa')

EXAMPLE = '((((Aa,aa),(Aa,Aa)),((aa,aa),(aa,AA))),Aa)'
EXAMPLE_RESULT = [0.156, 0.5, 0.344]


class Node:
    index = 0

    def __init__(self, value=None, left=None, right=None):
        Node.index += 1
        self.index = Node.index
        self.value = value
        self.left = left
        self.right = right
        self.prob = None

    def __str__(self):
        return '<Node(index: {}, value: {})>'.format(self.index, self.value)

    def __repr__(self):
        return self.__str__()

    def is_leaf(self):
        return self.left is None and self.right is None


def read_newick(file_obj):
    """Convert string represention to python structure."""
    lst = [i for i in PARSER.split(file_obj.read().replace(' ', '')) if i]
    pointers = [[]]
    index = 0
    indexes = []
    for section in lst:
        if section == '(':
            pointers.append([])
            pointers[index].append(pointers[-1])
            index = len(pointers) - 1
            indexes.append(index)
        elif section == ',':
            continue
        elif section == ')':
            indexes.pop()
            try:
                index = indexes[-1]
            except IndexError:
                break
        else:
            pointers[index].append(section)
    return pointers[0][0]


def tree(lst, node=None):
    """Convert list structure to tree."""
    if node is None:
        Node.index = 0
    if isinstance(lst, list):
        node = Node()
        node.left = tree(lst[0], node)
        node.right = tree(lst[1], node)
    else:
        return Node(lst)
    return node


def add_edges(node, g):
    def node_name(n):
        return '{} - {} - {}'.format(n.index, n.value, n.prob)
    if node.left:
        g.edge(node_name(node), node_name(node.left))
        add_edges(node.left, g)
    if node.right:
        g.edge(node_name(node), node_name(node.right))
        add_edges(node.right, g)


def graph(node, fname):
    from graphviz import Graph
    g = Graph('G')
    add_edges(node, g)
    g.render(fname, view=True)


def gen_to_probability(obj):
    if obj not in GEN_VARIANTS:
        assert len(obj) == 3
        return obj
    gen = obj
    prob = [0, 0, 0]
    prob[GEN_VARIANTS.index(gen)] = 1
    return prob


def cross_probability(prob1, prob2):
    prob1 = gen_to_probability(prob1)
    prob2 = gen_to_probability(prob2)
    prob = [0, 0, 0]
    prob[0] = (prob1[0] * prob2[0] +
               prob1[0] * prob2[1] * 0.5 +
               prob1[1] * prob2[0] * 0.5 +
               prob1[1] * prob2[1] * 0.25)

    prob[1] = (prob1[0] * prob2[2] +
               prob1[0] * prob2[1] * 0.5 +
               prob1[1] * prob2[0] * 0.5 +
               prob1[1] * prob2[1] * 0.5 +
               prob1[1] * prob2[2] * 0.5 +
               prob1[2] * prob2[0] +
               prob1[2] * prob2[1] * 0.5)

    prob[2] = (prob1[1] * prob2[1] * 0.25 +
               prob1[1] * prob2[2] * 0.5 +
               prob1[2] * prob2[1] * 0.5 +
               prob1[2] * prob2[2])
    return prob


def calculate_genotype_probability(node):
    if node.is_leaf():
        return gen_to_probability(node.value)
    p1 = (calculate_genotype_probability(node.left) or
          node.left.prob)
    p2 = (calculate_genotype_probability(node.right) or
          node.right.prob)
    node.prob = cross_probability(p1, p2)


# === tests ===


def tree_to_list(node):
    if node is None:
        return []
    return [node.index] + tree_to_list(node.left) + tree_to_list(node.right)


def cross_gen(gen1, gen2):
    cnt = Counter()
    for i in gen1:
        for j in gen2:
            x, y = sorted((i, j))
            cnt[x + y] += 1
    s = sum(cnt.values())
    return [cnt.get(i, 0) / s for i in GEN_VARIANTS]


class InferringGenotypeTest(unittest.TestCase):
    def test_read_newick(self):
        def r(s):
            return read_newick(io.StringIO(s))
        self.assertEqual([], r('()'))
        self.assertEqual(['Aa', 'Aa'], r('(Aa,Aa)'))
        self.assertEqual(['Aa', ['Aa']], r('(Aa, (Aa))'))
        self.assertEqual(
            [[[['Aa', 'aa'], ['Aa', 'Aa']],
              [['aa', 'aa'], ['aa', 'AA']]], 'Aa'],
            r(EXAMPLE))

    def test_tree_to_list(self):
        self.assertEqual([1, 2, 3], tree_to_list(tree([1, 2])))
        self.assertEqual([1, 2, 3, 4, 5], tree_to_list(tree([[1, 2], 3])))

    def test_cross_gen(self):
        self.assertEqual([0, 1, 0], cross_gen('AA', 'aa'))
        self.assertEqual([0, 0.5, 0.5], cross_gen('Aa', 'aa'))
        self.assertEqual([0, 0, 1], cross_gen('aa', 'aa'))
        self.assertEqual([0.5, 0.5, 0], cross_gen('AA', 'Aa'))
        self.assertEqual([0.25, 0.5, 0.25], cross_gen('Aa', 'Aa'))
        self.assertEqual([1, 0, 0], cross_gen('AA', 'AA'))
        self.assertEqual(cross_gen('AA', 'aa'), cross_gen('aa', 'AA'))

    def test_cross_probability(self):
        self.assertEqual(cross_gen('AA', 'AA'), cross_probability('AA', 'AA'))
        self.assertEqual(cross_gen('AA', 'aa'), cross_probability('AA', 'aa'))
        self.assertEqual(cross_gen('Aa', 'Aa'), cross_probability('Aa', 'Aa'))

    def test_example(self):
        node = tree(read_newick(io.StringIO(EXAMPLE)))
        calculate_genotype_probability(node)
        prob = list(map(lambda x: round(x, 3), node.prob))
        self.assertEqual(EXAMPLE_RESULT, prob)


if __name__ == '__main__':
    unittest.main()
