from ui import render_ui
from utils import gen_report
from logic.from_lines_to_report import transgres as tg_standart_input
from constants import (
    simantic_chei_tg_table,
    anti_simantic_chei_tg_table,
    info_RNA_tg_table,
)

funcs = dict()
# funcs["reports_gen"] = gen_report
funcs["смысловая цепь"] = lambda x: tg_standart_input(x, simantic_chei_tg_table)
funcs["анти смысловая цепь"] = lambda x: tg_standart_input(
    x, anti_simantic_chei_tg_table
)

funcs["И РНК"] = lambda x: tg_standart_input(x, info_RNA_tg_table)
# funcs['цепь белков'] = lambda x:tg_standart_input(x,{"Ц":"0","Г":"1","Т":"2","А":"3"})


render_ui(funcs)
