
import sys
for line in sys.stdin:
	pSGDID, fType, qualifier, feature, gene, aliases, parent, sSGDID, chromosome, start, stop, strand, pos, cVersion, sVersion, description = line.rstrip('/n/r').split('\t')	

chromosome = 16 #chromosome number

breakpoint_position_c16 = 788000 #breakpoint position for chromosome 16

chromosome_position_start = int(start) 

chromosome_position_stop = int(stop)

base_pair_distance = round(((chromosome_position_start + chromosome_position_stop)/2)) #find center base-pairing gene

distance = abs(788000 - base_pair_distance) #find the distance from breakpoint to center base-pairing gene

print(distance, pSGDID, feature, gene,sep='\t')  #seperate by tabs
