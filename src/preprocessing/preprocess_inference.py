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

def merge_mask2(mask):
    for i in [1]:
        mask[mask == i] = 1
    for i in [2]:
        mask[mask == i] = 2
    for i in [3]:
        mask[mask == i] = 3
    for i in [4]:
        mask[mask == i] = 4
    for i in [5]:
        mask[mask == i] = 5
    for i in [6]:
        mask[mask == i] = 6
    for i in [7]:
        mask[mask == i] = 7
    for i in [8]:
        mask[mask == i] = 8
    for i in [9]:
        mask[mask == i] = 9
    for i in [10]:
        mask[mask == i] = 10
    for i in [11]:
        mask[mask == i] = 11
    for i in [12]:
        mask[mask == i] = 12
    for i in [13]:
        mask[mask == i] = 13
    for i in [14]:
        mask[mask == i] = 14
    for i in [15]:
        mask[mask == i] = 15
    for i in [16]:
        mask[mask == i] = 16
    for i in [17]:
        mask[mask == i] = 17
    for i in [18]:
        mask[mask == i] = 18
    for i in [20]:
        mask[mask == i] = 19
    for i in [21]:
        mask[mask == i] = 20
    for i in [22]:
        mask[mask == i] = 21
    for i in [23]:
        mask[mask == i] = 22
    for i in [24]:
        mask[mask == i] = 23
    for i in [25]:
        mask[mask == i] = 24
    for i in [29]:
        mask[mask == i] = 25
    for i in [118]:
        mask[mask == i] = 26
    for i in [185]:
        mask[mask == i] = 27
    for i in [0, 19]:
        mask[mask == i] = 0
    return mask
