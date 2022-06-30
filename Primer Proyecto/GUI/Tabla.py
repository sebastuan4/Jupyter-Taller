from tkinter import *

import tksheet #pip install tksheets

root = Tk()

sheet = tksheet.Sheet(root)

sheet.grid()

sheet.set_sheet_data([[f"{ri+cj}" for cj in range(4)] for ri in range(1)])

# table enable choices listed below:

sheet.enable_bindings(("single_select",

                       "row_select",

                       "column_width_resize",

                       "arrowkeys",

                       "right_click_popup_menu",

                       "rc_select",

                       "rc_insert_row",

                       "rc_delete_row",

                       "copy",

                       "cut",

                       "paste",

                       "delete",

                       "undo",

                       "edit_cell"))

root.mainloop()