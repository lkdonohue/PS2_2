import sys

open_cdt_file = sys.argv[1] #run all command lines using sys.argv
open_gtr_file = sys.argv[2]
gene_name = sys.argv[3]
correlation_cutoff = float(sys.argv[4])	 #correlation cutoff for nodes will be defined by user input

ORF_gene_id_dict = {}	#make dictionaries for ORFs and gene ids from cdt file
gene_id_ORF_dict = {}

parent_dict = {} #make dictionaries for tree building of parent and children nodes/genes from gtr file
child_1_dict = {}
child_2_dict = {}
correlation_dict = {} 	#also need a dictionary for correlation values


with open(open_cdt_file, "r") as cdt_file: #need to open cdt file
	for line in cdt_file:
		stripped_list = line.rstrip().split('\t') #seperate lines in cdt file by tabs
		ORF = stripped_list[1]
		gene_id = stripped_list[0]

		ORF_gene_id_dict.update({ORF: gene_id})	 #update dictionaries with ORFs and gene ids from cdt file
		gene_id_ORF_dict.update({gene_id: ORF})		
  

with open(open_gtr_file, "r") as gtr_file: #need to open gtr file
	for line in gtr_file:
		stripped_list = line.rstrip().split('\t') #sepearte lines in gtr file by tabs
		root = stripped_list[0] #parent nodes are the root
		branch = stripped_list[1] #children are the branches and leaves
		leaf = stripped_list[2]
		correlation_value = stripped_list[3]

		parent_dict.update({branch:root})	#make a parent dictionary with the parent nodes and their corresponding children
		parent_dict.update({leaf:root})
		child_1_dict.update({root:branch}) #make dictionary for both child nodes and genes (branches and leaves)
		child_2_dict.update({root:leaf})
		correlation_dict.update({root:float(correlation_value)})  #correlation values need to be floated
 
"""
The function  find_highest_node serves to look through a tree of nodes and genes in order to find the highest node in the tree that passes 
a correlation cutoff as defined by the user. This function is also called on a gene of interest the user provides. The function will step 
backwards up the tree to the root, checking at every step to see if the current node it is on is above or equal to the correlation cutoff. 
In the end, it will return the highest node on the tree that passed the correlation requirement. This node is then passed on to the 
function: find_genes(input_node)
"""

input_gene = ORF_gene_id_dict[gene_name]	#get gene id for ORF entered on command line. Enter into highest_node_function

def find_highest_node(input_gene, new_node):
	best_node = new_node 
	if input_gene in parent_dict:	 #the root will not be in the parent dictionary, this serves as a "break" statement for the recursion
		last_node = parent_dict[input_gene]	#the last_node needs to be updated every time to keep calling function as move up the tree

		if (correlation_dict[parent_dict[input_gene]]) >= correlation_cutoff: 
			best_node = parent_dict[input_gene]	#only update the best_node IF the node passes user input correlation value

		return find_highest_node(last_node, best_node) 	#need to update last_node and best_node (if passed) before calling function again

	return best_node #want what you return to ONLY be the best node

output = (find_highest_node(input_gene, input_gene))    # output from the highest_node_function will return your highest/best node

"""
The function find_genes(input_node) is used to find all the genes that are coexpressed given the highest node found in the tree from the 
function: find_highest_node(input_gene, new_node). Given this node, the funciton will search through the two child dictionaries in order
to find all the "leaves" or genes within the tree that correspond to that node by searching back down the tree for all nodes that branch
off from the highest node. However, it will only record the gene ids (leaves) found at the bottom of the tree, not the nodes. 
Because you find the gene ids, the function then goes back into your ORF/gene id dictionary to only print out the ORFS, 
which are what you want to use for GO Term analysis.
"""

input_node = output	#the output generated from highest_node_function is the node that  will be used to generate a list of coexpressing genes

def find_genes(input_node):
	if child_1_dict[input_node].startswith("GENE"): 
		print(gene_id_ORF_dict[child_1_dict[input_node]])	#ONLY the ORFs of the genes are to be printed, NOT nodes or the gene ids
	else:
		find_genes(child_1_dict[input_node])	#if a node is found instead of a gene, run the function again using THAT node as the input node

	if child_2_dict[input_node].startswith("GENE"):	#same as for child_1_dict
		print(gene_id_ORF_dict[child_2_dict[input_node]])
	else:
		find_genes(child_2_dict[input_node])

	return None #Since the ORFs will be printed out, there is nothing th return

find_genes(input_node)
