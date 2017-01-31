import sys

gene_names = sys.argv[1:]

ORF_gene_id_dict = {}
gene_id_ORF_dict = {}

with open("cellcycle.cdt", "r") as cdt_file:
	for line in cdt_file:
		stripped_list = line.rstrip().split('\t')
		input_search = [stripped_list[2]]
		ORF = stripped_list[1]
		gene_id = stripped_list[0]

		ORF_gene_id_dict.update({ORF: gene_id})
		gene_id_ORF_dict.update({gene_id: ORF})

parent_dict = {}
child_1_dict = {}
child_2_dict = {}
correlation_dict = {}

with open("cellcycle.gtr", "r") as gtr_file:
	for line in gtr_file:
		stripped_list = line.rstrip().split('\t')
		
		parent_dict.update({stripped_list[1]:stripped_list[0]})
		parent_dict.update({stripped_list[2]:stripped_list[0]})
		child_1_dict.update({stripped_list[0]:stripped_list[1]})
		child_2_dict.update({stripped_list[0]:stripped_list[2]})
		correlation_dict.update({stripped_list[0]:float(stripped_list[3])}) 

input_gene = "GENE1X"
node_correlation = {}

def find_highest_node(input_gene):
	if input_gene in parent_dict:
		for parent_dict[input_gene] in correlation_dict:
			if (correlation_dict[parent_dict[input_gene]]) >= float(0.86):
				node_correlation.update({parent_dict[input_gene]:correlation_dict[parent_dict[input_gene]]})
					
find_highest_node(input_gene)
for key in node_correlation:
	print(key)

#print(node_correlation)				

input_node = "NODE1X"
genes = []

def find_genes(input_node):
	if child_1_dict[input_node].startswith("GENE"):
		genes.append(child_1_dict[input_node])
	else:
		find_genes(child_1_dict[input_node])
	if child_2_dict[input_node].startswith("GENE"):
		genes.append(child_2_dict[input_node])
	else:
		find_genes(child_2_dict[input_node])

find_genes(input_node)
print(genes)

