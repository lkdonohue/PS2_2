import sys

gene_names = sys.argv[1:]

remove_duplicates = [] #will append each unique piece of information from the stripped_list here later

for line in sys.stdin:
        stripped_list = line.rstrip().split('\t') #split str variable by tabs
        aliases = stripped_list[5].split("|") #convert alias and sSGDID into lists
        sSGDID = stripped_list[7].split("|")
        input_search = [stripped_list[0], stripped_list[3], stripped_list[4]] #takes what the user inputs to search through stripped list
        input_search.extend(aliases) #add aliases and sSGDID to input acceptable to search through in stripped list
        input_search.extend(sSGDID)

        for information in input_search: #what information you want to extract from data set searching based on user input
                for names in gene_names:
                        if names.upper() == information: #case-insenstitive to work with any user input
                                if stripped_list[6].startswith ("chromosome"): #print out based on chromosome rather than coding sequence
                                        i = [stripped_list[0],stripped_list[1],stripped_list[2],stripped_list[3],stripped_list[4],stripped_list[5],stripped_list[6],stripped_list[7],stripped_list[8],stripped_list[9],stripped_list[10],stripped_list[11],stripped_list[15]]
                                        if i in remove_duplicates: #will not add duplicates/information it has already read in stripped_list to remove_duplicates but will continue on if unique
                                                break
                                        else:
                                                remove_duplicates.append(i) #appends all unique information to remove_duplicates in the order it sees it

output = list(remove_duplicates) #convert remove_duplicates back to a list
for i in remove_duplicates:
        print('\t'.join(i)) #print information in tab delineated format
