from pathlib import Path

from tkinter import *
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1080x600")
window.configure(bg="#FFFFFF")


user_image = ImageTk.PhotoImage(Image.open(
    relative_to_assets("User Photo.png")))
home_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("home .png")).resize((15, 15), Image.ANTIALIAS))
prepare_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("prepare.png")).resize((15, 15), Image.ANTIALIAS))
process_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("process.png")).resize((15, 15), Image.ANTIALIAS))
review_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("review.png")).resize((15, 15), Image.ANTIALIAS))
logout_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("logout.png")).resize((15, 15), Image.ANTIALIAS))
standard_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("standard.png")).resize((15, 15), Image.ANTIALIAS))
floating_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("floating.png")).resize((15, 15), Image.ANTIALIAS))
new_temp_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("new_temp.png")).resize((15, 15), Image.ANTIALIAS))
search_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("search.png")).resize((15, 15), Image.ANTIALIAS))
upload_file_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("upload_file.png")).resize((80, 80), Image.ANTIALIAS))
pdf_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("pdf.png")).resize((50, 50), Image.ANTIALIAS))
xls_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("xls.png")).resize((50, 50), Image.ANTIALIAS))
docs_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("docs.png")).resize((50, 50), Image.ANTIALIAS))
export_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("export.png")).resize((25, 25), Image.ANTIALIAS))
create_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("create.png")).resize((25, 25), Image.ANTIALIAS))
import_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("import.png")).resize((25, 25), Image.ANTIALIAS))
save_icon = ImageTk.PhotoImage(Image.open(
    relative_to_assets("save.png")).resize((25, 25), Image.ANTIALIAS))

menu_frame = Frame(window, width=200, height=600, bg="#FFFFFF")
menu_frame.place(x=0, y=0)
container_frame = Frame(window, width=880, height=600, bg="#F3F3FB")
container_frame.place(x=200, y=0)

prepare_flag = True


def home():
    clear_frame(container_frame)
    dashboard_frame = Frame(container_frame, width=600,
                            height=300, bg="#C4C4C4")
    dashboard_frame.place(x=140, y=150)
    Label(dashboard_frame, text="Dashboard Components", bg='#C4C4C4',
          font=("Times", 42, "bold")).place(x=10, y=110)


def clear_frame(frames):
    for widgets in frames.winfo_children():
        widgets.destroy()


def menu(y):
    clear_frame(menu_frame)
    top_menu = Frame(menu_frame, width=180, height=540, bg="#FFFFFF")
    top_menu.place(x=10, y=30)
    Label(top_menu, image=user_image, bg="white", ).place(x=40, y=0)
    Label(top_menu, text="User Name", bg="white", font=(
        "Times", "10", "bold")).place(x=60, y=100)
    Button(top_menu, image=home_icon, bg="white",
           text='   HOME', font=('Helvetica', 8, 'bold'), bd=0, activebackground='white', compound=LEFT, command=home).place(x=20, y=150)
    Button(top_menu, image=prepare_icon, bg="white",
           text='   PREPARE', font=('Helvetica', 8, 'bold'), bd=0, activebackground='white', compound=LEFT, command=prepare).place(x=20, y=180)
    Button(top_menu, image=process_icon, bg="white",
           text='   PROCESS', font=('Helvetica', 8, 'bold'), bd=0, activebackground='white', compound=LEFT, command=process).place(x=20, y=210+y)
    Button(top_menu, image=review_icon, bg="white",
           text='   REVIEW', font=('Helvetica', 8, 'bold'), bd=0, activebackground='white', compound=LEFT, command=review).place(x=20, y=240+y)
    Button(top_menu, image=logout_icon, bg="white",
           text='  LOG OUT', font=('Helvetica', 10, 'bold'), bd=0, activebackground='white', compound=LEFT).place(x=20, y=520)


def prepare():
    global prepare_flag
    if prepare_flag:
        clear_frame(menu_frame)
        menu(60)
        top_menu = list(menu_frame.winfo_children())[0]
        Button(top_menu, image=standard_icon, bg="white",
               text='   STANDARD', font=('Helvetica', 8, 'bold'), bd=0, activebackground='white', compound=LEFT, command=standard).place(x=40, y=210)
        Button(top_menu, image=floating_icon, bg="white",
               text='   FLOAT', font=('Helvetica', 8, 'bold'), bd=0, activebackground='white', compound=LEFT, command=floating).place(x=40, y=240)
        prepare_flag = False
    else:
        clear_frame(menu_frame)
        menu(0)
        prepare_flag = True


def stand_new_template():
    clear_frame(container_frame)
    canvas = Canvas(container_frame, bg='white', width=450,
                    height=540)
    canvas.place(x=40, y=30)
    Canvas(container_frame, bg='white', width=300,
           height=540).place(x=540, y=30)
    Button(canvas, image=create_icon, bd=0).place(x=420, y=430)
    Button(canvas, image=import_icon, bd=0).place(x=420, y=470)
    Button(canvas, image=save_icon, bd=0).place(x=420, y=510)


def standard():
    clear_frame(container_frame)
    containt_frame = Frame(container_frame, width=800,
                           height=540, bg="#F3F3FB")
    containt_frame.place(x=40, y=30)
    templates_types = ["Recent Templates",
                       "Save Templates", "Deleted Templetes"]
    variable = StringVar()
    variable.set(templates_types[1])
    templates_types_dropdown = OptionMenu(
        containt_frame, variable, *templates_types)
    templates_types_dropdown.place(x=0, y=50)
    templates_types_dropdown.config(width=20)
    templates_types_dropdown.config(bd=0)
    templates_types_dropdown.config(bg='#F3F3FB')
    Button(containt_frame, bg='#7CB8F7',
           text='    New Templates', image=new_temp_icon, compound=LEFT, bd=0, fg='white', font=('Times', 13), height=30, command=stand).place(x=660, y=10)
    search_frame = Frame(containt_frame, width=300, height=30, bg='#ffffff')
    search_frame.place(x=500, y=50)
    Label(search_frame, image=search_icon, bg='#ffffff').place(x=5, y=7)
    Button(search_frame, bd=0, bg='#7CB8F7',
           fg='white', text='Templates').place(x=240, y=4)
    Text(search_frame, width=20, height=1, bd=0).place(x=30, y=5)
    template_1 = Frame(containt_frame, bg='white', height=120, width=350)
    template_1.place(x=0, y=100)
    template_2 = Frame(containt_frame, bg='white', height=120, width=350)
    template_2.place(x=450, y=100)
    template_3 = Frame(containt_frame, bg='white', height=120, width=350)
    template_3.place(x=0, y=250)
    template_4 = Frame(containt_frame, bg='white', height=120, width=350)
    template_4.place(x=450, y=250)
    template_5 = Frame(containt_frame, bg='white', height=120, width=350)
    template_5.place(x=0, y=400)
    template_6 = Frame(containt_frame, bg='white', height=120, width=350)
    template_6.place(x=450, y=400)
    temp_list = [template_1, template_2, template_3,
                 template_4, template_5, template_6]

    for i in range(6):
        l1 = Label(temp_list[i], text="Template-"+str(i+1),
                   font=('Times', 15, 'bold'), bg='white')
        l1.place(x=0, y=5)
        text = "Most of its text is made up from sections 1.10.32–3 of Cicero's\nDe finibus bonorum et malorum (On the Boundaries of \nGoods and Evils; finibus may also be translated as purposes)."
        l2 = Label(temp_list[i], text=text, font=(
            'Arials', 9), bg='white')
        l2.place(x=0, y=50)
        Label(temp_list[i], text='1 minute ago', font=(
            'Helvetica', 6), bg='white', fg='#707C97').place(x=270, y=5)


def float_new_template():
    clear_frame(container_frame)
    Canvas(container_frame, bg='white', width=450,
           height=540).place(x=40, y=30)
    Canvas(container_frame, bg='white', width=300,
           height=540).place(x=540, y=30)


def floating():
    clear_frame(container_frame)
    containt_frame = Frame(container_frame, width=800,
                           height=540, bg="#F3F3FB")
    containt_frame.place(x=40, y=30)
    templates_types = ["Recent Templates",
                       "Save Templates", "Deleted Templetes"]
    variable = StringVar()
    variable.set(templates_types[1])
    templates_types_dropdown = OptionMenu(
        containt_frame, variable, *templates_types)
    templates_types_dropdown.place(x=0, y=50)
    templates_types_dropdown.config(width=20)
    templates_types_dropdown.config(bd=0)
    templates_types_dropdown.config(bg='#F3F3FB')
    Button(containt_frame, bg='#7CB8F7',
           text='    New Templates', image=new_temp_icon, compound=LEFT, bd=0, fg='white', font=('Times', 13), height=30, command=floats).place(x=660, y=10)
    search_frame = Frame(containt_frame, width=300, height=30, bg='#ffffff')
    search_frame.place(x=500, y=50)
    Label(search_frame, image=search_icon, bg='#ffffff').place(x=5, y=7)
    Button(search_frame, bd=0, bg='#7CB8F7',
           fg='white', text='Templates').place(x=240, y=4)
    Text(search_frame, width=20, height=1, bd=0).place(x=30, y=5)
    template_1 = Frame(containt_frame, bg='white', height=120, width=350)
    template_1.place(x=0, y=100)
    template_2 = Frame(containt_frame, bg='white', height=120, width=350)
    template_2.place(x=450, y=100)
    template_3 = Frame(containt_frame, bg='white', height=120, width=350)
    template_3.place(x=0, y=250)
    template_4 = Frame(containt_frame, bg='white', height=120, width=350)
    template_4.place(x=450, y=250)
    template_5 = Frame(containt_frame, bg='white', height=120, width=350)
    template_5.place(x=0, y=400)
    template_6 = Frame(containt_frame, bg='white', height=120, width=350)
    template_6.place(x=450, y=400)
    temp_list = [template_1, template_2, template_3,
                 template_4, template_5, template_6]

    for i in range(6):
        l1 = Label(temp_list[i], text="Template-"+str(i+1),
                   font=('Times', 15, 'bold'), bg='white')
        l1.place(x=0, y=5)
        text = "Most of its text is made up from sections 1.10.32–3 of Cicero's\nDe finibus bonorum et malorum (On the Boundaries of \nGoods and Evils; finibus may also be translated as purposes)."
        l2 = Label(temp_list[i], text=text, font=(
            'Arials', 9), bg='white')
        l2.place(x=0, y=50)
        Label(temp_list[i], text='1 minute ago', font=(
            'Helvetica', 6), bg='white', fg='#707C97').place(x=270, y=5)


def process():
    clear_frame(container_frame)
    containt_frame = Frame(container_frame, width=800,
                           height=540, bg="#F3F3FB")
    containt_frame.place(x=40, y=30)
    Label(containt_frame, text="Upload Documents",
          font=('Arials', 15, 'bold'), bg='#F3F3FB').place(x=5, y=5)
    upload_frame_1 = Frame(containt_frame, width=350, height=250, bg='white')
    upload_frame_1.place(x=5, y=50)
    Label(upload_frame_1, image=upload_file_icon, bg='white').place(x=130, y=60)
    Label(upload_frame_1, text='Drag and Drop Files',
          bg='white', fg='#707C97').place(x=120, y=145)
    upload_frame_2 = Frame(containt_frame, width=350, height=250, bg='white')
    upload_frame_2.place(x=405, y=50)
    Label(upload_frame_2, image=upload_file_icon, bg='white').place(x=130, y=60)
    Label(upload_frame_2, text='Drag and Drop Files',
          bg='white', fg='#707C97').place(x=120, y=145)

    Label(containt_frame, text="Export Result as", font=(
        'Arials', 12, 'bold')).place(x=160, y=350)
    Label(containt_frame, image=pdf_icon, bg='#F3F3FB').place(x=300, y=340)
    Label(containt_frame, image=docs_icon, bg='#F3F3FB').place(x=360, y=340)
    Label(containt_frame, image=xls_icon, bg='#F3F3FB').place(x=420, y=340)
    Button(containt_frame, text="   Export", image=export_icon, font=(
        'Arials', 15, 'bold'), compound=LEFT, bd=0, bg='#707C97', fg='white', width=140).place(x=320, y=420)


def review():
    clear_frame(container_frame)
    containt_frame = Frame(container_frame, width=800,
                           height=540, bg="#F3F3FB")
    containt_frame.place(x=40, y=30)
    Label(containt_frame, text="Export History",
          font=('Times', 15, 'bold')).place(x=5, y=5)
    Frame(containt_frame, width=790, height=480, bg="white").place(x=5, y=40)


menu(0)
home()
# window.resizable(False, False)
window.mainloop()
