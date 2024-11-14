#lembrai

from datetime import datetime, timedelta

task = input ("Digite a tarefa que você precisa fazer: ")
#Armazena a tarefa.
task_date_str = input ("Digite a data e hora para o lembrete (formato: DD/MM/AAAA HH:MM)")
#armazena a data e a hora.
task_date = datetime.strptime(task_date_str, "%d/%m/%Y %H:%M")
#o metodo strptime interpreta a string do que jeito que você informar.
now = datetime.now()
time_left = task_date - now 

print(f"faltam{time_left.days} dias e {time_left.seconds // 3600} horas para a tarefa:{task}")





#input é a função que coleta o texto digitado e armazena numa vareavel.
# ex: nome + input ("Qual é o seu nome? ")
#print (f"Olá, {nome}!") 
# o print mostra a mensgae na tela, e o f antes das aspas, permite colocar variaveis dentro da string usando {}.
#o datatime.strptime converte ua string, para um objeto de data e hora.
#o datatime.now() pega o momento exato em que o codigo é executado.
# o strftime() formata um objeto datatime para string. %A retorna o nome do dia da semana.
#quando fazemos time_left = task_date - now o python calcula a diferença entre as duas.




