tree = (('raccoon', 'bear'), (('sea_lion', 'seal'), (('monkey', 'cat'), 'weasel')))

def find_leaves(tree):
	leaves = []
	for x in tree:
		if isinstance(x, str):
			leaves.append(x)
		else:
			leaves += find_leaves(x)
	return leaves

leaves = find_leaves(tree)
print(leaves)
