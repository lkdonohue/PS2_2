codon_table_dict = {'GAA': 'glutamine', 'GAG': 'glutamine', 'AAA': 'lysine', 'AAG': 'lysine', 'CCU': 'proline', 'CCC': 'proline', 'CCA': 'proline', 'CCG': 'proline'}

amino_acid = input("Enter a codon:").upper()

result = (codon_table_dict[amino_acid])

print (amino_acid , result)

