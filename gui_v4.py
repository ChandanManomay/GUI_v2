from operator import index
from pathlib import Path
from pydoc import pager

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
from pandastable import Table
import matplotlib.pyplot as plt
from functools import partial

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Main Window
window = Tk()
window.geometry("1080x600")
window.configure(bg="#FFFFFF")

# Loading image
user_image = ImageTk.PhotoImage(
    Image.open(relative_to_assets("User Photo.png")))
home_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("home .png")).resize(
        (15, 15), Image.ANTIALIAS)
)
prepare_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("prepare.png")
               ).resize((15, 15), Image.ANTIALIAS)
)
process_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("process.png")
               ).resize((15, 15), Image.ANTIALIAS)
)
review_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("review.png")).resize(
        (15, 15), Image.ANTIALIAS)
)
logout_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("logout.png")).resize(
        (15, 15), Image.ANTIALIAS)
)
standard_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("standard.png")
               ).resize((15, 15), Image.ANTIALIAS)
)
floating_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("floating.png")
               ).resize((15, 15), Image.ANTIALIAS)
)
new_temp_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("new_temp.png")
               ).resize((15, 15), Image.ANTIALIAS)
)
search_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("search.png")).resize(
        (15, 15), Image.ANTIALIAS)
)
upload_file_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("upload_file.png")
               ).resize((30, 30), Image.ANTIALIAS)
)
pdf_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("pdf.png")).resize((50, 50), Image.ANTIALIAS)
)
xls_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("xls.png")).resize((50, 50), Image.ANTIALIAS)
)
docs_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("docs.png")).resize(
        (50, 50), Image.ANTIALIAS)
)
export_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("export.png")).resize(
        (25, 25), Image.ANTIALIAS)
)
create_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("create.png")).resize(
        (25, 25), Image.ANTIALIAS)
)
import_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("import.png")).resize(
        (25, 25), Image.ANTIALIAS)
)
save_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("save.png")).resize(
        (25, 25), Image.ANTIALIAS)
)

droupdown_icon = ImageTk.PhotoImage(
    Image.open(relative_to_assets("arrow.png")).resize(
        (15, 15), Image.ANTIALIAS)
)


# Two Frames one for Menu and other for Content
menu_frame = Frame(window, width=200, height=600, bg="#FFFFFF")
menu_frame.place(relx=0.02, rely=0, relheight=1, relwidth=0.18519)
container_frame = Frame(window, width=880, height=600, bg="#F3F3FB")
container_frame.place(relx=0.18519, rely=0, relheight=1, relwidth=0.81481)

prepare_flag = True


def home():
    clear_frame(container_frame)
    dashboard_frame = Frame(container_frame, width=600,
                            height=300, bg="#C4C4C4")
    dashboard_frame.place(relx=0.15, rely=0.25, relheight=0.5, relwidth=0.6812)
    Label(
        dashboard_frame,
        text="Dashboard Components",
        bg="#C4C4C4",
        font=("Times", 42, "bold"),
    ).place(relx=0.0167, rely=0.367, relheight=0.3, relwidth=1)


def clear_frame(frames):
    for widgets in frames.winfo_children():
        widgets.destroy()


def menu(y):
    clear_frame(menu_frame)
    top_menu = Frame(menu_frame, width=180, height=540, bg="#FFFFFF")
    top_menu.place(relx=0.00926, rely=0.05, relheight=0.9, relwidth=0.9)
    Label(top_menu, image=user_image, bg="white",).place(
        relx=0.2, rely=0, relheight=0.2, relwidth=0.6
    )
    Label(top_menu, text="User Name", bg="white", font=("Times", "10", "bold")).place(
        relx=0, rely=0.2, relheight=0.03, relwidth=1
    )
    Button(
        top_menu,
        image=home_icon,
        bg="white",
        text="   HOME",
        font=("Helvetica", 8, "bold"),
        bd=0,
        activebackground="white",
        compound=LEFT,
        command=home,
    ).place(relx=0, rely=0.25, relheight=0.05, relwidth=0.5)
    Button(
        top_menu,
        image=prepare_icon,
        bg="white",
        text="   PREPARE",
        font=("Helvetica", 8, "bold"),
        bd=0,
        activebackground="white",
        compound=LEFT,
        command=prepare,
    ).place(relx=0, rely=0.3, relheight=0.05, relwidth=0.6)
    Button(
        top_menu,
        image=process_icon,
        bg="white",
        text="   PROCESS",
        font=("Helvetica", 8, "bold"),
        bd=0,
        activebackground="white",
        compound=LEFT,
        command=process,
    ).place(relx=0, rely=0.35 + y, relheight=0.05, relwidth=0.61)
    Button(
        top_menu,
        image=review_icon,
        bg="white",
        text="   REVIEW",
        font=("Helvetica", 8, "bold"),
        bd=0,
        activebackground="white",
        compound=LEFT,
        command=review,
    ).place(relx=0, rely=0.4 + y, relheight=0.05, relwidth=0.55)
    Button(
        top_menu,
        image=logout_icon,
        bg="white",
        text="  LOG OUT",
        font=("Helvetica", 10, "bold"),
        bd=0,
        activebackground="white",
        compound=LEFT,
    ).place(relx=0.111, rely=0.963)


def prepare():
    global prepare_flag
    if prepare_flag:
        clear_frame(menu_frame)
        menu(0.1)
        top_menu = list(menu_frame.winfo_children())[0]
        Button(
            top_menu,
            image=standard_icon,
            bg="white",
            text="   STANDARD",
            font=("Helvetica", 8, "bold"),
            bd=0,
            activebackground="white",
            compound=LEFT,
            command=standard,
        ).place(relx=0.25, rely=0.35, relheight=0.05, relwidth=0.61)
        Button(
            top_menu,
            image=floating_icon,
            bg="white",
            text="   FLOAT",
            font=("Helvetica", 8, "bold"),
            bd=0,
            activebackground="white",
            compound=LEFT,
            command=floating,
        ).place(relx=0.25, rely=0.4, relheight=0.05, relwidth=0.5)
        prepare_flag = False
    else:
        clear_frame(menu_frame)
        menu(0)
        prepare_flag = True


def stand_new_template():
    clear_frame(container_frame)
    canvas = Canvas(container_frame, bg="white", width=450, height=540)
    canvas.place(relx=0.05, rely=0.0555, relheight=0.9, relwidth=0.5114)
    Canvas(container_frame, bg="white", width=300, height=540).place(
        relx=0.614, rely=0.0555, relheight=0.9, relwidth=0.341
    )
    Button(canvas, image=create_icon, bd=0,
           bg="white").place(relx=0.934, rely=0.7963)
    Button(canvas, image=import_icon, bd=0,
           bg="white").place(relx=0.934, rely=0.8704)
    Button(canvas, image=save_icon, bd=0, bg="white").place(
        relx=0.934, rely=0.9444)


def standard():
    clear_frame(container_frame)
    containt_frame = Frame(container_frame, width=800,
                           height=540, bg="#F3F3FB")
    containt_frame.place(relx=0.05, rely=0.0555,
                         relheight=0.9, relwidth=0.9091)
    templates_types = ["Recent Templates",
                       "Save Templates", "Deleted Templetes"]
    variable = StringVar()
    variable.set(templates_types[1])
    templates_types_dropdown = OptionMenu(
        containt_frame, variable, *templates_types)
    templates_types_dropdown.place(
        relx=0, rely=0.1, relheight=0.07, relwidth=0.2)
    # templates_types_dropdown.config(width=20)
    templates_types_dropdown.config(bd=0)
    templates_types_dropdown.config(bg="#F3F3FB")
    Button(
        containt_frame,
        bg="#7CB8F7",
        text="    New Templates",
        image=new_temp_icon,
        compound=LEFT,
        bd=0,
        fg="white",
        font=("Times", 13),
        height=30,
        command=stand_new_template,
    ).place(relx=0.8, rely=0.0185, relheight=0.07, relwidth=0.2)
    search_frame = Frame(containt_frame, width=300, height=30, bg="#ffffff")
    search_frame.place(relx=0.6, rely=0.1, relheight=0.07, relwidth=0.4)
    Label(search_frame, image=search_icon, bg="#ffffff").place(
        relx=0.001, rely=0, relheight=1, relwidth=0.1
    )
    Button(search_frame, bd=0, bg="#7CB8F7", fg="white", text="Templates").place(
        relx=0.7, rely=0, relheight=1, relwidth=0.3
    )
    Text(search_frame, width=20, height=1, bd=0).place(relx=0.09, rely=0.3)
    template_1 = Frame(containt_frame, bg="white", height=120, width=350)
    template_1.place(relx=0, rely=0.23, relheight=0.23, relwidth=0.4375)
    template_2 = Frame(containt_frame, bg="white", height=120, width=350)
    template_2.place(relx=0.5625, rely=0.23, relheight=0.23, relwidth=0.4375)
    template_3 = Frame(containt_frame, bg="white", height=120, width=350)
    template_3.place(relx=0, rely=0.48, relheight=0.23, relwidth=0.4375)
    template_4 = Frame(containt_frame, bg="white", height=120, width=350)
    template_4.place(relx=0.5625, rely=0.48, relheight=0.23, relwidth=0.4375)
    template_5 = Frame(containt_frame, bg="white", height=120, width=350)
    template_5.place(relx=0, rely=0.73, relheight=0.23, relwidth=0.4375)
    template_6 = Frame(containt_frame, bg="white", height=120, width=350)
    template_6.place(relx=0.5625, rely=0.73, relheight=0.23, relwidth=0.4375)
    temp_list = [template_1, template_2, template_3,
                 template_4, template_5, template_6]
    for i in range(6):
        l1 = Label(
            temp_list[i],
            text="Template-" + str(i + 1),
            font=("Times", 15, "bold"),
            bg="white",
        )
        l1.place(relx=0, rely=0, relheight=0.2, relwidth=0.3)
        text = "Most of its text is made up from sections 1.10.32–3 of Cicero's\nDe finibus bonorum et malorum (On the Boundaries of \nGoods and Evils; finibus may also be translated as purposes)."
        l2 = Label(temp_list[i], text=text, font=("Arials", 9), bg="white")
        l2.place(relx=0, rely=0.15, relheight=0.659, relwidth=1)
        Label(
            temp_list[i],
            text="1 minute ago",
            font=("Helvetica", 6),
            bg="white",
            fg="#707C97",
        ).place(relx=0.77, rely=0, relwidth=0.33)


def float_new_template():
    clear_frame(container_frame)
    canvas = Canvas(container_frame, bg="white", width=450, height=540)
    canvas.place(relx=0.088, rely=0.0555, relheight=0.9, relwidth=0.5114)
    Canvas(container_frame, bg="white", width=300, height=540).place(
        relx=0.614, rely=0.0555, relheight=0.9, relwidth=0.341
    )
    Button(canvas, image=create_icon, bd=0,
           bg="white").place(relx=0.934, rely=0.7963)
    Button(canvas, image=import_icon, bd=0,
           bg="white").place(relx=0.934, rely=0.8704)
    Button(canvas, image=save_icon, bd=0, bg="white").place(
        relx=0.934, rely=0.9444)


def floating():
    clear_frame(container_frame)
    containt_frame = Frame(container_frame, width=800,
                           height=540, bg="#F3F3FB")
    containt_frame.place(relx=0.05, rely=0.0555,
                         relheight=0.9, relwidth=0.9091)
    templates_types = ["Recent Templates",
                       "Save Templates", "Deleted Templetes"]
    variable = StringVar()
    variable.set(templates_types[1])
    templates_types_dropdown = OptionMenu(
        containt_frame, variable, *templates_types)
    templates_types_dropdown.place(
        relx=0, rely=0.1, relheight=0.07, relwidth=0.2)
    # templates_types_dropdown.config(width=20)
    templates_types_dropdown.config(bd=0)
    templates_types_dropdown.config(bg="#F3F3FB")
    Button(
        containt_frame,
        bg="#7CB8F7",
        text="    New Templates",
        image=new_temp_icon,
        compound=LEFT,
        bd=0,
        fg="white",
        font=("Times", 13),
        height=30,
        command=float_new_template,
    ).place(relx=0.8, rely=0.0185, relheight=0.07, relwidth=0.2)
    search_frame = Frame(containt_frame, width=300, height=30, bg="#ffffff")
    search_frame.place(relx=0.6, rely=0.1, relheight=0.07, relwidth=0.4)
    Label(search_frame, image=search_icon, bg="#ffffff").place(
        relx=0.001, rely=0, relheight=1, relwidth=0.1
    )
    Button(search_frame, bd=0, bg="#7CB8F7", fg="white", text="Templates").place(
        relx=0.7, rely=0, relheight=1, relwidth=0.3
    )
    Text(search_frame, width=20, height=1, bd=0).place(relx=0.09, rely=0.3)
    template_1 = Frame(containt_frame, bg="white", height=120, width=350)
    template_1.place(relx=0, rely=0.23, relheight=0.23, relwidth=0.4375)
    template_2 = Frame(containt_frame, bg="white", height=120, width=350)
    template_2.place(relx=0.5625, rely=0.23, relheight=0.23, relwidth=0.4375)
    template_3 = Frame(containt_frame, bg="white", height=120, width=350)
    template_3.place(relx=0, rely=0.48, relheight=0.23, relwidth=0.4375)
    template_4 = Frame(containt_frame, bg="white", height=120, width=350)
    template_4.place(relx=0.5625, rely=0.48, relheight=0.23, relwidth=0.4375)
    template_5 = Frame(containt_frame, bg="white", height=120, width=350)
    template_5.place(relx=0, rely=0.73, relheight=0.23, relwidth=0.4375)
    template_6 = Frame(containt_frame, bg="white", height=120, width=350)
    template_6.place(relx=0.5625, rely=0.73, relheight=0.23, relwidth=0.4375)
    temp_list = [template_1, template_2, template_3,
                 template_4, template_5, template_6]

    for i in range(6):
        l1 = Label(
            temp_list[i],
            text="Template-" + str(i + 1),
            font=("Times", 15, "bold"),
            bg="white",
        )
        l1.place(relx=0, rely=0, relheight=0.2, relwidth=0.3)
        text = "Most of its text is made up from sections 1.10.32–3 of Cicero's\nDe finibus bonorum et malorum (On the Boundaries of \nGoods and Evils; finibus may also be translated as purposes)."
        l2 = Label(temp_list[i], text=text, font=("Arials", 9), bg="white")
        l2.place(relx=0, rely=0.15, relheight=0.659, relwidth=1)
        Label(
            temp_list[i],
            text="1 minute ago",
            font=("Helvetica", 6),
            bg="white",
            fg="#707C97",
        ).place(relx=0.77, rely=0, relwidth=0.33)


def process():
    clear_frame(container_frame)
    containt_frame = Frame(container_frame, width=800,
                           height=540, bg="#F3F3FB")
    containt_frame.place(relx=0.05, rely=0.0555,
                         relheight=0.9, relwidth=0.9091)
    Label(
        containt_frame,
        text="Upload Documents",
        font=("Arials", 15, "bold"),
        bg="#F3F3FB",
    ).place(relx=0.4, rely=0.00926)
    upload_frame = Frame(containt_frame, bg="white")
    upload_frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
    upload_button_frame_1 = Frame(upload_frame)
    upload_button_frame_1.place(
        relx=0.1, rely=0.1, relheight=0.15, relwidth=0.8)
    Label(upload_button_frame_1, image=upload_file_icon).place(
        relx=0.5, rely=0, relheight=0.8, relwidth=0.1
    )
    Label(upload_button_frame_1, text="Drag and Drop Files", fg="#707C97").place(
        relx=0.44, rely=0.7, relheight=0.2
    )
    upload_button_frame_2 = Frame(upload_frame)
    upload_button_frame_2.place(
        relx=0.1, rely=0.3, relheight=0.15, relwidth=0.8)
    Label(upload_button_frame_2, image=upload_file_icon).place(
        relx=0.5, rely=0, relheight=0.8, relwidth=0.1
    )
    Label(upload_button_frame_2, text="Drag and Drop Files", fg="#707C97").place(
        relx=0.44, rely=0.7, relheight=0.2
    )
    Label(
        upload_frame, text="Export Result as", font=("Arials", 12, "bold"), bg="white",
    ).place(relx=0.3, rely=0.55, relheight=0.1)
    Label(upload_frame, image=pdf_icon, bg="white").place(
        relx=0.475, rely=0.545, relheight=0.1
    )
    Label(upload_frame, image=docs_icon, bg="white").place(
        relx=0.55, rely=0.545, relheight=0.1
    )
    Label(upload_frame, image=xls_icon, bg="white").place(
        relx=0.625, rely=0.545, relheight=0.1
    )
    Button(
        upload_frame,
        text="   Export",
        image=export_icon,
        font=("Arials", 15, "bold"),
        compound=LEFT,
        bd=0,
        bg="#7CB8F7",
        fg="white",
        width=140,
    ).place(relx=0.3, rely=0.7, relheight=0.1, relwidth=0.4)


def bar_chart(df, col):
    if col.get() != "":
        col = list(map(int, col.get().split()))
        df = df.iloc[:, col]
    df.plot.bar()
    plt.show()


def review():
    clear_frame(container_frame)
    containt_frame = Frame(container_frame, width=800,
                           height=540, bg="#F3F3FB")
    containt_frame.place(relx=0.05, rely=0.0555,
                         relheight=0.9, relwidth=0.9091)
    Label(containt_frame, text="Export History", font=("Times", 18, "bold"), bg='#F3F3FB').place(
        relx=0.05, rely=0
    )
    table_container_frame = Frame(
        containt_frame, width=790, height=480, bg="white")
    table_container_frame.place(
        relx=0.05, rely=0.08, relheight=0.85, relwidth=0.9)
    table_frame = Frame(table_container_frame, bg="white")
    table_frame.place(relx=0, rely=0, relheight=0.85, relwidth=1)
    Canvas(table_frame, bg='#E5E5E5', height=30).place(
        relx=0, rely=0, relwidth=1)
    df = pd.read_csv("DashboardView.csv", index_col=None)
    for col in df.columns:
        Label(table_frame, text=col, font=("Helvetica 10 bold"), bg='#E5E5E5').grid(
            row=0, column=list(df.columns).index(col), padx=5, pady=5)

        i = 1
        for row in df[col]:
            Label(table_frame, text=row, bg='white', font=("Helvetica 10")).grid(row=i,
                                                                                 column=list(df.columns).index(col), pady=15)
            i += 1

    page_frame = Frame(table_container_frame, bg='white')
    page_frame.place(relx=0, rely=0.85, relheight=0.12, relwidth=1)

    page_frame_droupdown = Frame(page_frame, bg='white')
    page_frame_droupdown.place(relx=0.05, relheight=1, relwidth=.2, rely=.5)

    Label(page_frame_droupdown, text="Rows per page:",
          bg='white').grid(row=0, column=0)
    pages = list(range(1, 12))
    variable = IntVar()
    variable.set(pages[10])
    page_dropdown = OptionMenu(page_frame_droupdown, variable, *pages)
    page_dropdown.grid(row=0, column=1)
    page_dropdown.config(indicatoron=0, image=droupdown_icon,
                         compound='right', bg='white', bd=0)

    page_frame_itemcount = Frame(page_frame, bg='white')
    page_frame_itemcount.place(relx=0.83, relheight=1, relwidth=.2, rely=.5)
    Label(page_frame_itemcount, text='1-10 of 30 items',
          bg='white').grid(row=0, column=0)
    Button(page_frame_itemcount, text='<',
           bg='white', bd=0).grid(row=0, column=1)
    Button(page_frame_itemcount, text='>',
           bg='white', bd=0).grid(row=0, column=2)


menu(0)
home()
# window.resizable(False, False)
window.mainloop()
