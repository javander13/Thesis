## Merging labels
hard_coral = [1,3,5,7,8,9,13,16,19,29,32,34,36,40,42,
              46,49,52,54,55,57,59,64,66,70,74,76,81,
              83,89,90,91,93,95,97,99,100,101,103,105,
              106,108,110,111,113,114,122,135,136]

hard_coral_bleached = [2,4,6,10,14,15,17,30,33,41,43,47,50,
                       53,56,58,60,65,67,71,75,77,82,92,94,
                       96,98,102,104,107,109,112,115,123]

soft_coral = [124]

dead_coral = [37,38,116,117]

other_invertebrates = [11,12,18,28,44,45,63,68,69,72,73,80,
                       88,119,125,127,128,129,132,134,137]

sand_rubble = [79,118,120]

other = [35,48,51,86,126]

algae = [20,21,22,23,24,25,26,27,31,39,
         61,62,78,84,87,121,130,131,133]

unknown = [85,255]


def merge_mask(mask):
    for i in hard_coral:
        mask[mask == i] = 0
    for i in hard_coral_bleached:
        mask[mask == i] = 1
    for i in soft_coral:
        mask[mask == i] = 2
    for i in dead_coral:
        mask[mask == i] = 3
    for i in other_invertebrates:
        mask[mask == i] = 4
    for i in sand_rubble:
        mask[mask == i] = 5
    for i in other:
        mask[mask == i] = 6
    for i in algae:
        mask[mask == i] = 7
    for i in unknown:
        mask[mask == i] = 8
    return mask