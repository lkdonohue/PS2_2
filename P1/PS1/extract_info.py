import sys
for line in sys.stdin:
        pSGDID, fType, qualifier, feature, gene, aliases, parent, sSGDID, chromosome, start, stop, strand, pos, cVersion, sVersion, description = line.rstrip('/n/r').split('\t')

         #chromosome number 16 = c16

        breakpoint_position_c16 = 788000 #breakpoint position for chromosome 16

        base_pair_distance = round(((int(start) + int(stop))/2)) #find center base-pairing gene

        distance = abs(base_pair_distance - breakpoint_position_c16) #find the distance from breakpoint to center base-pairing gene

        print(distance, pSGDID, feature, gene,sep='\t')  #seperate by tabs
