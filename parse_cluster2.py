import sys

gene_names = sys.argv[1:]

with open("cellcycle.cdt", "r") as cdt_file:
	for line in cdt_file:
		stripped_list = line.rstrip().split('\t')
		input_search = [stripped_list[2]]
		geneID = stripped_list[0]
		ORF = stripped_list[1]
		ORF_gene_identifier = []
		for information in input_search:
			for names in gene_names:
				if names.upper() == information:
					ORF_gene_identifier.update[ORF, geneID]
					print(ORF)
					break

with open("cellcycle.gtr", "r") as gtr_file:
	for line in gtr_file:
		stripped_list = line.rstrip().split('\t')
		parent = stripped_list[0]
		child = stripped_list[1]
		parent_nodeID_dict = [nodeID, nodeID[:1]]
		parent_geneID_dict = [geneID, nodeID[:1]]


