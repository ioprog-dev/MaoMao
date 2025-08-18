from ui import render_ui
from utils import gen_report
from logic.from_lines_to_report import transgres as tg_standart_input

funcs=dict()
#funcs["reports_gen"] = gen_report
funcs['смысловая цепь'] = lambda x:tg_standart_input(x,{"Ц":"0","Г":"1","Т":"2","А":"3"})
funcs['анти смысловая цепь'] = lambda x:tg_standart_input(x,{"Г":"0","Ц":"1","А":"2","Т":"3"})
funcs['И РНК'] = lambda x:tg_standart_input(x,{"Ц":"0","Г":"1","Т":"2","А":"3"})
#funcs['цепь белков'] = lambda x:tg_standart_input(x,{"Ц":"0","Г":"1","Т":"2","А":"3"})



render_ui(funcs)



