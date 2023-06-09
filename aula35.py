import datetime

data = datetime.datetime.now()
nasc = datetime.datetime(1986, 5, 4)

print(f"{data.day} / {data.month} / {data.year}")
print(nasc.strftime("%A"))  # passou o dia da data do nasc
print(data.strftime("%W"))


'''
%a txt dia da semana resumido
%A txt dia da semana completo
%w retorna o numero do dia da semana(domingo dia 0)
%d dia do mes
%b txt mes abreviado
%B txt mes
%m num do mes
%y ano 2.f
%Y ano 4.f
%H hora 2.f 00 - 23
%I 00 - 12
%p AM / PM
%M minutos
%S segundos
%f microsegundos
%j dia do ano 001 - 365
%W num da semana do ano
'''
