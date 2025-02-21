from constants import GAME_MAP

print(GAME_MAP)

mazefornodes = []
for i, row in enumerate(GAME_MAP):
    start = None
    for j, cell in enumerate(row):
        count = 0
        if cell == 1:
            pass # incomplete i need to append X

        if cell == 0 and count == 0 :
            while cell == 0:
                if start is None:
                    start = j
                    pass # incomplete

                elif start is not None:
                    pass # i need to append 
                

