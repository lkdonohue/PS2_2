import sys

gene_names = sys.argv[1:]

with open("cellcycle.cdt", "r") as cdt_file:
	for line in cdt_file:
		stripped_list = line.rstrip().split('\t')
		input_search = [stripped_list[2]]
		ORF_gene_identifier = [stripped_list[1], stripped_list[0]]
		for information in input_search:
			for names in gene_names:
				if names.upper() == information:
					for value in ORF_gene_identifier:
						print(stripped_list[0])
						break

with open("cellcycle.gtr", "r") as gtr_file:
	for line in gtr_file:
		stripped_list = line.rstrip().split('\t')
		nodeID = stripped_list[0]
		geneID = stripped_list[1]
		parent_nodeID_dict = [nodeID, nodeID[:1]]
		parent_geneID_dict = [geneID, nodeID[:1]]

