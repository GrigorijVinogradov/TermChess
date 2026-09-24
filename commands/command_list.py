from commands.command import Command
from commands.exit import Exit
from commands.gethistory import Get_History
from commands.playsequence import Play_Sequence


Command_List = [ 
    Exit(),
    Get_History(),
    Play_Sequence(),
]
