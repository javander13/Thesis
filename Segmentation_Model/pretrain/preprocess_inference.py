## Merging labels
hard_coral = [4,5,6,7,8,9,10,11,12,13,14,17,18,118]

hard_coral_bleached = []

dead_coral = [1,2,3,29]

other_invertebrates = [15,16]

sand_rubble = [20,21,24]

other = [22,23,185]

algae = [25]

seagrass = []

unknown = []

no_label = [19]


def merge_mask(mask):
    for i in dead_coral:
        mask[mask == i] = 3
    for i in hard_coral:
        mask[mask == i] = 1
    for i in hard_coral_bleached:
        mask[mask == i] = 2
    for i in other_invertebrates:
        mask[mask == i] = 4
    for i in sand_rubble:
        mask[mask == i] = 5
    for i in other:
        mask[mask == i] = 6
    for i in algae:
        mask[mask == i] = 7
    for i in seagrass:
        mask[mask == i] = 8
    for i in unknown:
        mask[mask == i] = 9
    for i in no_label:
        mask[mask == i] = 0
    return mask