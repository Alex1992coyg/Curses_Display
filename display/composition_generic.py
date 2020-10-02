#!/usr/bin/python3
import curses
from display_block_latest import DisplayBlockOnSamePad
import abc

class AbsCompDisplayBlock(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self,screen,pad_name,n_lines,n_columns):
        self.screen = screen
        self.pad_name =pad_name
        self.pad = curses.newpad(n_lines,n_columns)
        self.pad.border(0)
        self.display_block = []

    @abc.abstractmethod
    def label(self,info,label_ref_pos):
        label = curses.newpad(20,10)
        label.addstr(str(info))
        label.refresh(0,0,label_ref_pos,1,18,15)

    @abc.abstractmethod
    def create_display_blocks(self):
            self.display_block.append(DisplayBlockOnSamePad(self.pad,"--",1))
            self.display_block.append(DisplayBlockOnSamePad(self.pad,"--",3))
            self.display_block.append(DisplayBlockOnSamePad(self.pad,"--",2))
            self.display_block.append(DisplayBlockOnSamePad(self.pad,"--",4))
            self.display_block.append(DisplayBlockOnSamePad(self.pad,"--",5))
            self.display_block.append(DisplayBlockOnSamePad(self.pad,"--",6))

    @abc.abstractmethod
    def updating_db(self,pad_ref_pos):
        for i in range(len(self.display_block)):
            self.display_block[i].update_pad(" info "+str(i))
        self.pad.refresh(0,0,pad_ref_pos,1,10,34)
    # @abc.abstractmethod
    # def screen_size(self):
    #     num_rows, num_cols = self.stdscr.getmaxyx()
    #     #curses.endwin()
    #     print("Rows:    %d" % num_rows)
    #     print("Columns: %d" % num_cols)


class DisplayBlockRobots(AbsCompDisplayBlock):

    def __init__(self,screen,pad_name,n_lines,n_columns):
        self.screen = screen
        self.pad_name =pad_name
        self.pad = curses.newpad(n_lines,n_columns)
        self.pad.erase()
        self.pad.border(0)
        self.display_block = []
        self.create_display_blocks()

    def label(self,info,label_ref_pos,x,y):
        label = curses.newpad(x,y)
        label.addstr(str(info))
        label.refresh(0,0,label_ref_pos,10,x-1,y-1)

    def create_display_blocks(self):
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"Battery Status",1))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"Task Status",3))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"Lidar Status",2))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"Motor Status",4))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"Lifting Status",5))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"Network Quality",6))


    def updating_db(self,pad_ref_y,pad_ref_x):
        num_rows, num_cols = self.screen.getmaxyx()
        self.screen_size()
        # print("Pad Row Pos: %d" % pad_ref_y)
        # print("Pad Columns Pos: %d" % pad_ref_x)

        for i in range(len(self.display_block)):
            if  ( (pad_ref_y < num_rows) and (pad_ref_x < num_cols)):
                self.display_block[i].update_pad(" info "+str(i))
                pad_rows = min(22,num_rows)
                pad_columns = min(34,num_cols)
                print("Pad Row Pos: %d" % pad_rows)
                print("Pad Columns Pos: %d" % pad_columns)
                self.pad.refresh(0,1,pad_ref_y,pad_ref_x,pad_rows,pad_columns)

    def screen_size(self):
        num_rows, num_cols = self.screen.getmaxyx()
        print("Scr Rows: %d" % num_rows)
        print("Scr Columns: %d" % num_cols)


class DisplayBlockStacker(AbsCompDisplayBlock):

    def __init__(self,pad_name,n_lines,n_columns):
        self.pad_name =pad_name
        self.pad = curses.newpad(n_lines,n_columns)
        # self.pad.border(0)
        self.display_block = []
        self.create_display_blocks()

    def label(self,info,label_ref_pos):
        label = curses.newpad(20,20)
        label.addstr(str(info))
        label.refresh(0,0,label_ref_pos,1,18,15)

    def create_display_blocks(self):
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"IP_ADDRESS",1))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"IP",3))


    def updating_db(self,pad_ref_pos):
        for i in range(len(self.display_block)):
            self.display_block[i].update_pad(" 192.168.1."+str(i))
        self.pad.refresh(0,0,pad_ref_pos,1,22,34)

class DisplayBlockDOCKER(AbsCompDisplayBlock):
    def __init__(self,pad_name,n_lines,n_columns):
        self.pad_name =pad_name
        self.pad = curses.newpad(n_lines,n_columns)
        # self.pad.border(0)
        self.display_block = []
        self.create_display_blocks()

    def label(self,info,label_ref_pos):
        label = curses.newpad(20,20)
        label.addstr(str(info))
        label.refresh(0,0,label_ref_pos,1,18,15)

    def create_display_blocks(self):
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"TASK MANAGER",1))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"INIT",3))
        self.display_block.append(DisplayBlockOnSamePad(self.pad,"NAV",3))

    def updating_db(self,pad_ref_pos):
        for i in range(len(self.display_block)):
            self.display_block[i].update_pad(" ACTIVE"+str(i))
        self.pad.refresh(0,10,pad_ref_pos,20,22,34)


def main():
    stdscr = curses.initscr()
    stdscr.keypad(1)
    curses.noecho()
    curses.curs_set(0)

    stdscr.refresh()
    escape = False


    a=DisplayBlockRobots(stdscr,"Robot 1",8,30)
    #
    # b=DisplayBlockStacker("STACKER",100,100)
    # #
    # c=DisplayBlockDOCKER("DOCKER",100,100)

    # print(type(c))
    #
    # k=0
    # while (k != ord('q')):
    #     #
    #     a.label("ROBOT 1",0,10,20)
    #     a.updating_db(1,10,34)
    #
    #     # a.screen_size()
    #
    #     # b.label("STACKER",9)
    #     # b.updating_db(10)
    #     #
    #     # c.label("DOCKER",15)
    #     # c.updating_db(16)
    #     k =stdscr.getch()
    #     curses.KEY_RESIZE
    #     # curses.erase()
    while escape == False:
        # a.label("ROBOT 1",0,10,20)
        a.updating_db(2,1)
        # b.label("STACKER",9)
        # b.updating_db(10)
        # # #     #
        # c.label("DOCKER",15)
        # c.updating_db(16)
        # maxY, maxX = screen.getmaxyx()
        # screen.border('|', '|', '-', '-', '+', '+', '+', '+')
        # screen.addstr(4, 2, "MaxY: " + str(maxY))
        # screen.addstr(5, 2, "MaxX: " + str(maxX))

        x = stdscr.getch()
        if x == ord("q"):
            escape = True
            stdscr.clear()
            curses.endwin()
        elif x == curses.KEY_RESIZE:

            y,x = stdscr.getmaxyx()

            # a.pad.erase()
            # curses.resizeterm(y,x)
            stdscr.refresh()
            # self.height,self.width = self.screen.getmaxyx()
            # stdscr.draw_screen()

            # screen.addstr(2, 2, " Screen Resize Test "+str(count), curses.A_UNDERLINE)
            # stdscr.erase()
    curses.endwin()

if __name__ == '__main__':
    main()
