import sys

open_cdt_file = sys.argv[1] 	#run all command lines using sys.argv
open_gtr_file = sys.argv[2]
gene_name = sys.argv[3]
correlation_cutoff = float(sys.argv[4])	 #correlation cutoff for nodes will be defined by user input and used in the highest_node_function

ORF_gene_id_dict = {}	 #make dictionaries for ORFs and gene ids from cdt file
gene_id_ORF_dict = {}

parent_dict = {} 	#make dictionaries for tree building of parent and children nodes/genes from gtr file
child_1_dict = {}
child_2_dict = {}
correlation_dict = {} 	#also need a dictionary for correlation values


with open(open_cdt_file, "r") as cdt_file: 	#need to open cdt file
	for line in cdt_file:
		stripped_list = line.rstrip().split('\t') #seperate lines in cdt file by tabs
		ORF = stripped_list[1]
		gene_id = stripped_list[0]

		ORF_gene_id_dict.update({ORF: gene_id})	 #update dictionaries with ORFs and gene ids from cdt file
		gene_id_ORF_dict.update({gene_id: ORF})
  

with open(open_gtr_file, "r") as gtr_file: 	#need to open gtr file
	for line in gtr_file:
		stripped_list = line.rstrip().split('\t') 	#sepearte lines in gtr file by tabs
		
		parent_dict.update({stripped_list[1]:stripped_list[0]})		#make a parent dictionary with the parent nodes and their corresponding children
		parent_dict.update({stripped_list[2]:stripped_list[0]})
		child_1_dict.update({stripped_list[0]:stripped_list[1]}) 	#make dictionary for both child nodes and genes (branches and leaves)
		child_2_dict.update({stripped_list[0]:stripped_list[2]})
		correlation_dict.update({stripped_list[0]:float(stripped_list[3])})  	#correlation values need to be floated
 
"""
the function  find_highest_node serves to look through a tree of nodes and genes in order to find the highest node in the tree that passes 
a correlation cutoff as defined by the user. This function is also called on a gene of interest the user provides. The function will step 
backwards up the tree to the root, checking at every step to see if the current node it is on is above or equal to the correlation cutoff. 
In the end, it will return the highest node on the tree that passed the correlation requirement. This node is then passed on to the 
function: find_genes(input_node)
"""

input_gene = ORF_gene_id_dict[gene_name]	#get ORF for input gene run on command line and use this ORF to enter into the highest_node_function

def find_highest_node(input_gene, new_node):
	best_node = new_node 				#to start the best node is the input_gene but will be replaced once it finds better new nodes
	if input_gene in parent_dict:	 		#the root will not be in the parent dictionary, this serves as a "break" statement for the recursion
		last_node = parent_dict[input_gene]	#the last_node needs to be updated every time you pass through the tree so that you call the function on the parent node of the node you are currently on the next time you pass through the function

		if (correlation_dict[parent_dict[input_gene]]) >= correlation_cutoff: 	#check to see if the current node/gene passes the user's input correlation value
			best_node = parent_dict[input_gene]	#only update the best_node IF the correlation value is passed

		return find_highest_node(last_node, best_node) 	#need to keep track of the new last and possibly new best node before you go through the function again


	return best_node 	#want what you return to ONLY be the best node

output = (find_highest_node(input_gene, input_gene))    # output from the highest_node_function will return your highest node

"""
The function find_genes(input_node) is used to find all the genes that are coexpressed given the highest node found in the tree from the 
function: find_highest_node(input_gene, new_node). Given this node, the funciton will search through the two child dictionaries in order
to find all the "leaves" or genes within the tree that correspond to that node by searching back down the tree for all nodes that branch
off from the highest node. However, it will only record the gene ids (leaves) found at the bottom of the tree, not the nodes. Once done, 
you will have a list of all the gene ids that were found to be coexpressed. Be sure to change these gene ids into ORFs after for GO Term analysis!
"""

input_node = output	#the output generated from highest_node_function is the node that  will be used to generate a list of coexpressing genes
genes = []            #using the node identified in highest_node_function, need to generate a list of all the coexpressed genes

def find_genes(input_node):
	if child_1_dict[input_node].startswith("GENE"):	#given the highest node found in find_highest_genes, search for the genes belonging to that node 
		genes.append(child_1_dict[input_node])	#ONLY genes are to be added to your list, NOT nodes
	else:
		find_genes(child_1_dict[input_node])	#if a node is found instead of a gene, run the function again using THAT node as the input node
	if child_2_dict[input_node].startswith("GENE"):	#same as for child_1_dict
		genes.append(child_2_dict[input_node])
	else:
		find_genes(child_2_dict[input_node])
	return genes	#return the gene ids
find_genes(input_node)

for ORFS in genes:	#The last step is to convert the gene ids identified in find_genes to ORFs
	final_ORF_list = gene_id_ORF_dict[ORFS]
	print(final_ORF_list)	#Print the final list of your ORFs that correspond to the highest node
