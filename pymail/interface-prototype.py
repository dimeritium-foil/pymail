import curses as nc

X_START = 2

def main(stdscr):
    
    stdscr.clear()
    stdscr.border()
    stdscr.nodelay(True)
    nc.curs_set(0)

    # show logo and get the last y coordinate for the cursor
    logo_y = show_logo(stdscr)
    stdscr.refresh()

    message_window_width = int((nc.COLS - 1) / 1.5)
    message_window_height = 6

    message_window_y = logo_y + 1
    message_window_x = X_START

    message_window = nc.newwin(message_window_height, message_window_width, message_window_y, message_window_x)
    message_window.border()

    # color pair for a successful match
    nc.init_pair(1, nc.COLOR_GREEN, nc.COLOR_BLACK)

    message_window.addstr(2, 3, "Email: ")
    message_window.addstr("ixhixklaegqlyrpqjd@tcwlx.com", nc.color_pair(1))
    message_window.addstr(3, 3, "Via 10minutemail.com")
    message_window.refresh()

    mails_window_width = nc.COLS - 4
    mails_window_height = nc.LINES - (message_window_y + message_window_height) - 1

    mails_window_y = message_window_y + message_window_height
    mails_window_x = X_START

    mails_window = nc.newwin(mails_window_height, mails_window_width, mails_window_y, mails_window_x)
    mails_window.border()
    mails_window.refresh()

    emails_num = 4
    one_email_window_width = mails_window_width - 2
    one_email_window_height = (mails_window_height - 1) // emails_num
    one_email_window_x = 1

    emails_windows = []
    for i in range(emails_num):
        one_email_window_y = 1 + i*one_email_window_height
        one_email_window = mails_window.derwin(one_email_window_height, one_email_window_width, one_email_window_y, one_email_window_x)
        one_email_window.border()

        one_email_content_window = one_email_window.derwin(one_email_window_height - 2, one_email_window_width - 2, 1, 1)

        one_email_content_window.addstr(0, 0, f"Mail #{i+1}")
        one_email_content_window.addstr(1, 0, "From: Stephen Hawking")
        one_email_content_window.addstr(3, 0, "Nihil necessitatibus fugit voluptas accusantium. Blanditiis neque labore voluptatem. Aspernatur quia porro ducimus id est mollitia nihil architecto. Ipsam excepturi aut autem beatae sed. Ipsam est dicta assumenda dolores tenetur ut fuga nisi. At eligendi iure mollitia laboriosam.")

        one_email_content_window.refresh()
        one_email_window.refresh()
        emails_windows.append(one_email_window)

    stdscr.nodelay(False)
    stdscr.refresh()
    stdscr.getkey()
    exit()

    # message_window.addstr(3, 3, "Colored!", nc.color_pair(1))

    message_window.refresh()

def show_logo(window):

    logo = \
"""
                      _ _ 
 _ __ _  _ _ __  __ _(_) |
| '_ \ || | '  \/ _` | | |
| .__/\_, |_|_|_\__,_|_|_|
|_|   |__/                
"""

    logo = logo.splitlines()
    logo_width = max([len(line) for line in logo])

    logo_y = 0
    logo_x = X_START

    for row in range(len(logo)):
        window.addstr(logo_y + row, logo_x, logo[row])

    return logo_y + len(logo)

if __name__ == "__main__":
    
    nc.wrapper(main)
