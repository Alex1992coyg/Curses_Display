import curses
import time

# # class DisplayBlock:
#     def __init__(self,stdscr,status,row_position):
#         self.stdscr = stdscr
#         self.status = status
#         self.row_position = row_position
#         self.create_newwindow()
#
#     def create_newwindow(self):
#         self.my_win = curses.newwin(2,30,1,1)
#         self.adjust_window_position(self.row_position)
#
#     def update_window(self,info):
#         self.my_win.addstr(0,0, self.status+"  " , curses.A_REVERSE)
#         self.my_win.addstr(0,15, ": " +str(info))
#         self.my_win.refresh()
#
#     def adjust_window_position(self,row_position):
#         self.my_win.mvwin(row_position,1)
#         self.my_win.refresh()
#
#     def screen_size(self):
#         num_rows, num_cols = self.stdscr.getmaxyx()
#         #curses.endwin()
#         print("Rows:    %d" % num_rows)
#         print("Columns: %d" % num_cols)

class DisplayBlockPad:
    def __init__(self,stdscr,status):
        self.stdscr = stdscr
        self.status = status
        # self.row_position = row_position
        self.create_pad("Stat")

    def create_pad(self,info):
        self.my_pad = curses.newpad(100,100)

        self.my_pad.addstr(0,0, self.status , curses.A_REVERSE)
        curses.doupdate()

        self.my_pad.refresh(0,0,0,0,2,60)
        self.my_pad.addstr(1,0, self.status , curses.A_REVERSE)
        self.my_pad.refresh(0,0,0,0,2,60)
        # self.my_pad.addstr(0,15, ": " +str(info))
        # self.my_pad.refresh(0,0,1,1,15,30)

    #
    # def adjust_window_position(self,row_position):
    #     self.my_pad.mvpad(row_position,10)
    #     self.my_pad.refresh(0,0,5,5,15,30)

    def screen_size(self):
        num_rows, num_cols = self.stdscr.getmaxyx()
        #curses.endwin()
        print("Rows:    %d" % num_rows)
        print("Columns: %d" % num_cols)

def main():
    stdscr = curses.initscr()
    # curses.noecho(1)
    curses.curs_set(0)
    a = DisplayBlockPad(stdscr,"Battery Status ")
    # b = DisplayBlockPad(stdscr,"Task Status",2)
    # Use the 'q' key to quit
    stdscr.keypad(1)
    k=0
    stdscr.refresh()
    while (k != ord('q')):
        a.create_pad("99 Percent")
        # b.create_pad("DOCKING")
        k = stdscr.getch()
    curses.endwin()
    # while 1:
    #     key = stdscr.getch()
    #     stdscr.clear()
    #     if key == curses.KEY_UP:
    #         curses.endwin()
    #     else:
    #         a.create_pad("99 Percent")
    #         # b.update_window("DOCKING")
    #     stdscr.refresh


if __name__ == "__main__":
    main()
