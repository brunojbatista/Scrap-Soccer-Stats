from Library_v1.Driver.ChromeDriver import ChromeDriver
from Library_v1.Driver.DriverActions import DriverActions
import re

from Library_v1.Utils.string import (
    slug_name,
    default_space,
)

from Exceptions.StatReadingError import StatReadingError
from Exceptions.StatNotFoundError import StatNotFoundError
from Exceptions.StatWritingError import StatWritingError

from ReadingMatches import ReadingMatches

import sys

c = ChromeDriver()


r = ReadingMatches(c)

r.addTypeReading('5 jogos', 'Casa/Visitante')
# r.addTypeReading('5 jogos', 'Global')
r.addTypeReading('10 jogos', 'Casa/Visitante')
# r.addTypeReading('10 jogos', 'Global')
# r.addTypeReading('20 jogos', 'Casa/Visitante')
# r.addTypeReading('20 jogos', 'Global')


r.addStatReading('Médias e Dispersões', 'Over', '1º Gol', '+ 2 Gols')


script = sys.argv[0]
try:
    step = sys.argv[1]
except IndexError:
    step = None

# print(f"script: {script}")
# print(f"step: {step}")
r.execute(step)
    


