import curses
import time

class DisplayBlock:
    def __init__(self,stdscr,status,row_position):
        self.stdscr = stdscr
        self.status = status
        self.row_position = row_position
        self.create_newwindow()

    def create_newwindow(self):
        self.my_win = curses.newwin(2,30,1,1)
        self.adjust_window_position(self.row_position)

    def update_window(self,info):
        self.my_win.addstr(0,0, self.status+"  " , curses.A_REVERSE)
        self.my_win.addstr(0,15, ": " +str(info))
        self.my_win.refresh()

    def adjust_window_position(self,row_position):
        self.my_win.mvwin(row_position,1)
        self.my_win.refresh()

    def screen_size(self):
        num_rows, num_cols = self.stdscr.getmaxyx()
        #curses.endwin()
        print("Rows:    %d" % num_rows)
        print("Columns: %d" % num_cols)

class DisplayBlockPad:
    def __init__(self,status,n_lines,n_columns):
        self.status_1 = status

        self.n_lines = n_lines
        self.n_columns = n_columns
        self.create_pad(14,34)

    def color(self): # define color pair
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_GREEN)
        # set background color
        # self.my_pad.bkgd(curses.color_pair(2) | curses.A_DIM)

    def create_pad(self,nlines,ncolumns):
        self.my_pad = curses.newpad(self.n_lines,self.n_columns) #creating a new pad of 14line and 34 colums
        # activate border for the pad
        self.my_pad.border(0)

    def update_pad(self,str_sypos,str_sxpos,info,str_iypos,str_ixpos):
        self.my_pad.addstr(str_sypos,str_sxpos, self.status_1 )
        self.my_pad.addstr(str_iypos,str_ixpos, ": " +str(info),curses.A_BLINK | curses.color_pair(1))

    def refresh(self,line_pos,chara_pos,rect_c0y,rect_c0x):
        '''The refresh() call displays a section of the pad
        in the rectangle extending from coordinate (5,5)
        to coordinate (20,75) on the screen;
        the upper left corner of the displayed section is coordinate (0,0) on the pad.
        Beyond that difference, pads are exactly like ordinary windows and support the same methods.
        '''
        '''Start printing text from (0,2) of the pad (first line, 3rd char)
        on the screen at position (5,5)
        with the maximum portion of the pad displayed being 20 chars x 15 lines  [pad.refresh(0, 2, 5, 5, 15, 20)]
        '''
        self.my_pad.refresh(line_pos,chara_pos,rect_c0y,rect_c0x,20,40)

    def screen_size(self):
        num_rows, num_cols = self.stdscr.getmaxyx()
        #curses.endwin()
        print("Rows:    %d" % num_rows)
        print("Columns: %d" % num_cols)

class DisplayBlockOnSamePad:
    # self.pad.addstr(self.pad_position,18, ": " +str(info1),curses.A_BLINK)
    def __init__(self,pad,status,pad_position):
        self.status_1 = status
        self.my_pad   = pad
        self.pad_position = pad_position

    def color(self): # define color pair
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_GREEN)
        # set background color
        self.my_pad.bkgd(curses.color_pair(2) | curses.A_DIM)


    def update_pad(self,info):
        self.my_pad.addstr(self.pad_position,2, self.status_1 )
        self.my_pad.addstr(self.pad_position,18, ": " +str(info),curses.A_BLINK)
        #self.refresh()

    def refresh(self):
        '''The refresh() call displays a section of the pad
        in the rectangle extending from coordinate (5,5)
        to coordinate (20,75) on the screen;
        the upper left corner of the displayed section is coordinate (0,0) on the pad.
        Beyond that difference, pads are exactly like ordinary windows and support the same methods.
        '''
        '''Start printing text from (0,2) of the pad (first line, 3rd char)
        on the screen at position (5,5)
        with the maximum portion of the pad displayed being 15 lines x 20 chars    [pad.refresh(0, 2, 5, 5, 15, 20)]
        '''
        # self.my_pad.refresh(self.pad_position,0,self.pad_position*2+2,10,20,40)

    def screen_size(self):
        num_rows, num_cols = self.stdscr.getmaxyx()
        #curses.endwin()
        print("Rows:    %d" % num_rows)
        print("Columns: %d" % num_cols)


def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    my_pad = curses.newpad(22,34)
    my_pad.border(0)
    # a = DisplayBlockOnSamePad(my_pad,"Battery Status",1)
    # b = DisplayBlockOnSamePad(my_pad,"Task Status",0)
    # c = DisplayBlockOnSamePad(my_pad,"DOCKING",2)
    db =[]
    for i in range(20):
        db.append(DisplayBlockOnSamePad(my_pad,"Dummy "+str(i),i+1))

    # Use the 'q' key to quit
    stdscr.keypad(1)
    k=0
    stdscr.refresh()
    while (k != ord('q')):
        # a.color()
        # a.update_pad("99 %")
        # # a.refresh(0,0,2,2)
        #
        # b.update_pad("ROBOT")
        # # b.refresh(1,0,4,2)
        #
        # c.update_pad("LIFT")
        # # c.refresh(2,0,6,2)
        for i in range(20):
            db[i].update_pad("Value "+str(i))
        my_pad.refresh(0,0,1,1,22,34)
        k = stdscr.getch()
    curses.endwin()


if __name__ == "__main__":
    main()
