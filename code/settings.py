level_map = [
'                            ',
'                            ',
'                            ',
' XX    XXX            XX    ',
' XX P                       ',
' XXXX         XX         XX ',
' XXXX       XX              ',
' XX    X  XXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

vertical_tile_number = 11
tile_size = 64
screen_width = 1200
screen_height = vertical_tile_number * tile_size
fps = 60


if __name__ == '__main__':
    print(len(level_map) * tile_size)
    # stro = 0
    # for stroka in level_map:
    #     for symbol in stroka:
    #         if symbol == "X":
    #             print('ПРЫК-СКОК')
    #         if symbol == " ":
    #             print("Тыг-Дык")