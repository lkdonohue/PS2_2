import sys

open_cdt_file = sys.argv[1]
open_gtr_file = sys.argv[2]
gene_name = sys.argv[3]
correlation_cutoff = float(sys.argv[4])

ORF_gene_id_dict = {}
gene_id_ORF_dict = {}

with open(open_cdt_file, "r") as cdt_file:
	for line in cdt_file:
		stripped_list = line.rstrip().split('\t')
		ORF = stripped_list[1]
		gene_id = stripped_list[0]

		ORF_gene_id_dict.update({ORF: gene_id})
		gene_id_ORF_dict.update({gene_id: ORF})

parent_dict = {}
child_1_dict = {}
child_2_dict = {}
correlation_dict = {}

with open(open_gtr_file, "r") as gtr_file:
	for line in gtr_file:
		stripped_list = line.rstrip().split('\t')
		
		parent_dict.update({stripped_list[1]:stripped_list[0]})
		parent_dict.update({stripped_list[2]:stripped_list[0]})
		child_1_dict.update({stripped_list[0]:stripped_list[1]})
		child_2_dict.update({stripped_list[0]:stripped_list[2]})
		correlation_dict.update({stripped_list[0]:float(stripped_list[3])}) 

input_gene = ORF_gene_id_dict[gene_name] 

def find_highest_node(input_gene, new_node):
	best_node = new_node
	if input_gene in parent_dict:
		last_node = parent_dict[input_gene]	

		if (correlation_dict[parent_dict[input_gene]]) >= correlation_cutoff:
			best_node = parent_dict[input_gene]		

		return find_highest_node(last_node, best_node)


	return best_node

output = (find_highest_node(input_gene, input_gene))
#print(output)			

input_node = output
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
	return genes
find_genes(input_node)
#print(len(genes))

for ORFS in genes:
	final_ORF_list = gene_id_ORF_dict[ORFS]
	print(final_ORF_list)
