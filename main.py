from fastapi import FastAPI
import itertools
import re
from nltk.tree import Tree

app = FastAPI()

pat = re.compile(r"(NP\s->\s)(NP)(\s((CC)|(,))\s(NP))+")


def mix_algorithm(tree, positions_for_mix, limit):
    permutations = []

    index_permutations = list(itertools.permutations(positions_for_mix))
    index_permutations.remove(positions_for_mix)
    index_permutations = index_permutations[0:limit]

    original = tree.copy()

    for shift in index_permutations:
        for b in zip(positions_for_mix, shift):
            tree[b[0]] = original[b[1]]
        permutations.append(tree.copy())
    return permutations


@app.get("/paraphrase")
async def paraphrase(tree: str = "", limit: int = 20):
    t = Tree.fromstring(tree)

    all_positions = t.treepositions(order='preorder')
    leaves_positions = t.treepositions(order='leaves')
    lexical_positions = list(map(lambda x: x[:-1], leaves_positions))

    garbage_positions = leaves_positions + lexical_positions

    garbage_positions_hash = list(map(lambda x: hash(x), garbage_positions))
    trees_for_mixing = list(
        filter(lambda x: not (hash(x) in garbage_positions_hash) and re.fullmatch(pat, str(t[x].productions()[0])),
               all_positions))

    result = {"paraphrases": []}
    for i in trees_for_mixing:
        positions_for_mixing = tuple(range(0, len(t[i]) + 1, 2))
        for t[i] in mix_algorithm(t[i], positions_for_mixing, limit):
            result["paraphrases"].append({"tree": t.pformat(margin=500)})
            limit -= 1
    return result
