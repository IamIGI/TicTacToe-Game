TicTacDictionary = { 'TOP-L': ' ', 'TOP-M': ' ', 'TOP-R': ' ',
                     'MID-L': ' ', 'MID-M': ' ', 'MID-R': ' ',
                     'LOW-L': ' ', 'LOW-M': ' ', 'LOW-R': ' '}

MappingTicTacDictionary = { '1': 'TOP-L', '2': 'TOP-M', '3': 'TOP-R',
                            '4': 'MID-L', '5': 'MID-M', '6': 'MID-R',
                            '7': 'LOW-L', '8': 'LOW-M', '9': 'LOW-R'}

WinCombinations = [ #HORIZONTAL
                   ['TOP-L', 'TOP-M', 'TOP-R'],
                   ['MID-L', 'MID-M', 'MID-R'],
                   ['LOW-L', 'LOW-M', 'LOW-R'],
                    #VERTICAL
                   ['TOP-L', 'MID-L', 'LOW-L'],
                   ['TOP-M', 'MID-M', 'LOW-M'],
                   ['TOP-R', 'MID-R', 'LOW-R'],
                    #DIAGONAL
                   ['TOP-L', 'MID-M', 'LOW-R'],
                   ['TOP-R', 'MID-M', 'LOW-L']
]
