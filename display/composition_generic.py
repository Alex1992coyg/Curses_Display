import curses
from display_block_latest import DisplayBlockOnSamePad
from abc import ABC, abstractmethod

class AbstractCompositionDisplayBlock:

    def __init__(self):



class CompositionDisplayBlockRobots(AbstractCompositionDisplayBlock):

    def __init__(self,pad_name,n_lines,n_columns):
        self.pad_name =pad_name
        self.pad = curses.newpad(n_lines,n_columns)
        self.pad.border(0)
        self.display_block = []
        self.create_display_blocks()

    def label(self,info):
        label = curses.newpad(20,10)
        label.addstr(str(info))
        label.refresh(0,0,0,1,18,15)

    def create_display_blocks(self):
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"Battery Status",1))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"Task Status",3))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"Lidar Status",2))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"Motor Status",4))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"Lifting Status",5))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"Network Quality",6))


    def updating_db(self):
        for i in range(len(self.display_block)):
            self.display_block[i].update_pad(" info "+str(i))
        self.pad.refresh(0,0,1,1,10,34)

class CompositionDisplayBlockStacker(AbstractCompositionDisplayBlock):

    def __init__(self,pad_name,n_lines,n_columns):
        self.pad_name =pad_name
        self.pad = curses.newpad(n_lines,n_columns)
        self.pad.border(0)
        self.display_block = []
        self.create_display_blocks()

    def label(self,info):
        label = curses.newpad(20,20)
        label.addstr(str(info))
        label.refresh(0,0,9,1,18,15)

    def create_display_blocks(self):
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"IP_ADDRESS",1))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"IP",3))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"IP",2))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"IP",4))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"IP",5))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"Quality",6))


    def updating_db(self):
        for i in range(len(self.display_block)):
            self.display_block[i].update_pad(" 192.168.1."+str(i))
        self.pad.refresh(0,0,10,1,22,34)

def main():
    stdscr = curses.initscr()
    stdscr.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    stdscr.refresh()

    a=CompositionDisplayBlockRobots("Robot 1",8,34)
    b=CompositionDisplayBlockStacker("STACKER",8,34)
    k=0
    while (k != ord('q')):

        a.label("ROBOT 1")
        a.updating_db()

        b.label("STACKER")
        b.updating_db()
        k =stdscr.getch()
    curses.endwin()

if __name__ == '__main__':
    main()
