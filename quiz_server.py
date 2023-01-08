import socket
from threading import Thread
import random


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port_number = 8800

server.bind((ip_address,port_number))
server.listen()
print("server has started")
clients = []

questions = [
    " What is the Italian word for PIE? \n a.Mozarella\n b.Pasty\n c.Patty\n d.Pizza",
    " Water boils at 212 Units at which scale? \n a.Fahrenheit\n b.Celsius\n c.Rankine\n d.Kelvin",
    " Which sea creature has three hearts? \n a.Dolphin\n b.Octopus\n c.Walrus\n d.Seal",
    " Who was the character famous in our childhood rhymes associated with a lamb? \n a.Mary\n b.Jack\n c.Johnny\n d.Mukesh",
    " How many bones does an adult human have? \n a.206\n b.208\n c.201\n d.196",
    " How many wonders are there in the world? \n a.7\n b.8\n c.10\n d.4",
    " What element does not exist? \n a.Xf\n b.Re\n c.Si\n d.Pa",
    " How many states are there in India? \n a.24\n b.29\n c.30\n d.31",
    " Who invented the telephone? \n a.A.G Bell\n b.John Wick\n c.Thomas Edison\n d.G Marconi", 
    " Who is Loki? \n a.God of Thunder\n b.God of Dwarves\n c.God of Mischief\n d.God of Gods", 
    " Who was the first Indian female astronaut ? \n a.Sunita Williams\n b.Kalpana Chawla\n c.None of them\n d.Both of them ", 
    " What is the smallest continent? \n a.Asia\n b.Antarctic\n c.Africa\n d.Australia", 
    " The beaver is the national embelem of which country? \n a.Zimbabwe\n b.Iceland\n c.Argentina\n d.Canada", 
    " How many players are on the field in baseball? \n a.6\n b.7\n c.9\n d."
]

answers = ['d', 'a', 'b', 'a', 'a', 'a', 'a', 'b', 'a', 'c', 'b', 'd', 'd', 'c', 'a', 'b', 'a']

def remove(conn):
    if(conn not in clients):
        clients.remove(conn)

def remove_questions(index):
    questions.pop(index)
    answers.pop(index)

def clientThread(conn):
    score = 0
    conn.send("Welcome to this quiz game!".encode('utf-8'))
    conn.send("You will recieve a question. The answer to the question should be one of a,b,c,d or d\n".encode('utf-8'))
    conn.send("Good luck! \n\n".encode('utf-8'))
    index,question,answer = get_random_question_answer(conn)
    while True:
        try:
            msg = conn.recv(2048).decode('utf-8')
            if(msg):
                if(msg.lower()==answer):
                    score = score+1
                    conn.send(f'your score is{score}'.encode('utf-8'))
                else:
                    conn.send(f'your answer is incorrect'.encode('utf-8'))
                remove_questions(index)
                index,question,answer=get_random_question_answer(conn)
            else:
                remove(conn)
        except:
            continue
def get_random_question_answer(conn):
  index =  random.randint(0,len(questions))
  question = questions[index]
  answer = answers[index]
  conn.send(question.encode('utf-8'))
  return index,question,answer

while True: 
    conn,addr = server.accept()
    clients.append(conn)
    print(conn,addr)
    print(addr[0]+"connected")
    new_thread = Thread(target=clientThread, args=(conn))
    new_thread.start()
