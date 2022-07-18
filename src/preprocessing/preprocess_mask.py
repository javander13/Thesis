import numpy as np

## Merging labels
hard_coral = [1,3,5,7,9,13,16,19,29,32,34,36,40,42,
              46,49,52,54,55,57,59,64,66,70,74,76,81,
              83,89,90,91,93,95,97,99,100,101,103,105,
              106,108,110,111,113,114,135,136,138,
              140,141,142,143,144,148,150,155,156,157,
              158,159,160,161,162,163,164,165,166,167,
              168,169,170,171,172,173,174,175,176,177,
              178,179,180,181,182,183]

hard_coral_bleached = [2,4,6,10,14,15,17,30,33,41,43,47,50,
                       53,56,58,60,65,67,71,75,77,82,92,94,
                       96,98,102,104,107,109,112,115,139]

dead_coral = [37,38,116,117,152]

other_invertebrates = [11,12,18,28,44,45,63,68,69,72,73,80,
                       88,119,122,123,124,125,127,128,129,132,
                       134,137,184,185,186,187,188,189,190,191,
                       192,193,194,195,196,199,200]

sand_rubble = [79,118,120,145,149,151,201]

other = [35,48,51,86,126,153]

algae = [8,20,21,22,23,24,25,26,27,31,39,
         61,62,78,84,87,121,130,131,133,
        146,147,154,197,198,202,203]

seagrass = [204,205,206,207]

unknown = [85]

no_label = [255]


def merge_mask(mask):
    for i in hard_coral:
        mask[mask == i] = 1
    for i in hard_coral_bleached:
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
    for i in seagrass:
        mask[mask == i] = 8
    for i in unknown:
        mask[mask == i] = 9
    for i in no_label:
        mask[mask == i] = 0
    return mask

def expand_pixels(mask, maskPath):
    """Labels a 9x9 mask around each labelled pixel with the same label.
    Transforms the mask to Boolean."""
    new_mask = np.copy(mask)
    for i in range(len(np.nonzero(mask)[1])):
        x = np.nonzero(mask)[1][i]
        y = np.nonzero(mask)[0][i]

        try:
            new_mask[y-1,x] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")
        try:
            new_mask[y+1,x] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")
        try:
            new_mask[y,x-1] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")
        try:
            new_mask[y,x+1] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")             
        try:
            new_mask[y-1,x-1] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")             
        try:            
            new_mask[y+1,x-1] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")             
        try:            
            new_mask[y-1,x+1] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")             
        try:            
            new_mask[y+1,x+1] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}") 
        try:
            new_mask[y-2,x] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")
        try:
            new_mask[y+2,x] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")
        try:
            new_mask[y,x-2] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")
        try:
            new_mask[y,x+2] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")             
        try:
            new_mask[y-2,x-2] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")             
        try:            
            new_mask[y+2,x-2] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")             
        try:            
            new_mask[y-2,x+2] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")             
        try:            
            new_mask[y+2,x+2] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")
        try:
            new_mask[y-2,x-1] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")             
        try:            
            new_mask[y+2,x-1] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")             
        try:            
            new_mask[y-2,x+1] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")             
        try:            
            new_mask[y+2,x+1] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")
        try:
            new_mask[y-1,x-2] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")             
        try:            
            new_mask[y+1,x-2] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")             
        try:            
            new_mask[y-1,x+2] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")             
        try:            
            new_mask[y+1,x+2] = mask[y,x]
        except:
            print(f"this pixel is out of bounds !{maskPath}")
        
        # create a boolean mask 
        boo = np.copy(new_mask)
        for j in range(1,10):
            boo[boo == j] = 1
    
    return boo