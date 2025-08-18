from typing import Union
from constants import report_gen_qeue


triplets_to_string = lambda triplets: " ".join(triplets)


def genetikcode_generator(raw_str: str):
    """Функция принимает на вход И РНК и возвращает последовательность аминокислот"""
    eliments = raw_str.split()
    tg_table = {
        "УУУ": "Фен",
        "УУЦ": "Фен",
        "УУА": "Лей",
        "УУГ": "Лей",
        "УЦУ": "Сер",
        "УЦЦ": "Сер",
        "УЦА": "Сер",
        "УЦГ": "Сер",
        "УАУ": "Тир",
        "УАЦ": "Тир",
        "УАА": "___",
        "УАГ": "___",
        "УГУ": "Цис",
        "УГЦ": "Цис",
        "УГА": "___",
        "УГГ": "Трп",
        "ЦУУ": "Лей",
        "ЦУЦ": "Лей",
        "ЦУА": "Лей",
        "ЦУГ": "Лей",
        "ЦЦУ": "Про",
        "ЦЦЦ": "Про",
        "ЦЦА": "Про",
        "ЦЦГ": "Про",
        "ЦАУ": "Гис",
        "ЦАЦ": "Гис",
        "ЦАА": "Глн",
        "ЦАГ": "Глн",
        "ЦГУ": "Арг",
        "ЦГЦ": "Арг",
        "ЦГА": "Арг",
        "ЦГГ": "Арг",
        "АУУ": "Иле",
        "АУЦ": "Иле",
        "АУА": "Иле",
        "АУГ": "Мет",
        "АЦУ": "Тре",
        "АЦЦ": "Тре",
        "АЦА": "Тре",
        "АЦГ": "Тре",
        "ААУ": "Асн",
        "ААЦ": "Асн",
        "ААА": "Лиз",
        "ААГ": "Лиз",
        "АГУ": "Сер",
        "АГЦ": "Сер",
        "АГА": "Арг",
        "АГГ": "Арг",
        "ГУУ": "Вал",
        "ГУЦ": "Вал",
        "ГУА": "Вал",
        "ГУГ": "Вал",
        "ГЦУ": "Ала",
        "ГЦЦ": "Ала",
        "ГЦА": "Ала",
        "ГЦГ": "Ала",
        "ГАУ": "Асп",
        "ГАЦ": "Асп",
        "ГАА": "Глу",
        "ГАГ": "Глу",
        "ГГУ": "Гли",
        "ГГЦ": "Гли",
        "ГГА": "Гли",
    }

    for i in range(len(eliments)):
        eliments[i] = tg_table[eliments[i]]
    else:
        return " ".join(eliments)


def replaicer(raw_data, transition_table):
    for key, value in transition_table.items():
        raw_data = raw_data.replace(key, value)
    return raw_data


def trepetize_string(raw_data: str) -> list:
    if (len(raw_data) % 3) == 0:
        triplets = []
        while len(raw_data) > 0:
            triplets.append(raw_data[0:3])
            raw_data = raw_data[3:]
        else:
            return triplets
    else:
        raise Exception("неудалось разделить строку на триплеты")


def gen_report(raw_data: str) -> str:
    report = []
    for i in report_gen_qeue:
        report.append(triplets_to_string(trepetize_string(replaicer(raw_data, i))))
    else:
        report.append(genetikcode_generator(report[-1]))
        return "\n".join(report)


def clean_string(raw_string: str, permited_syms: list) -> str:
    for i in list(set(raw_string) - set(permited_syms)):
        raw_string = raw_string.replace(i, "")
    else:
        return raw_string
