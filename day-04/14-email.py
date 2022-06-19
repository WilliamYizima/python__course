#!/usr/bin/.venv python3
"""Exemplos de envio de email

"""
import smtplib
SERVER = "localhost"
PORT = 8025

FROM = "william.yizima@hotmail.com"
TO = ["william.yizima@hotmail.com"]
SUBJECT = "teste de envio"
TEXT="""\
Este é o meu e-mail enviado pelo Python
<b>Olá mundo</b>
"""

message = f"""\
From:{FROM}
To: {",".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER,  port=PORT) as server:
    server.sendmail(FROM, TO, message.encode('utf-8'))

"""
rodando o servidor em outro temrinal:
python -m smtpd -c DebuggingServer -n localhost:8025
"""