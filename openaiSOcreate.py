import sys
import os
import requests
import re
import csv
from openai import OpenAI

def request_generation(messages, temperature):
    # API_KEY must be set in an environment variable called OPENAI_API_KEY"
    # export OPENAI_API_KEY=<<your-key>>
    client = OpenAI()

    completion = client.chat.completions.create(
      #model="gpt-3.5-turbo",
      model="gpt-4o-mini",
      #model="gpt-4o",
      #model="gpt-4-turbo",
      temperature=temperature,
      messages=messages
    )

    content = completion.choices[0].message.content

    print(f"Request successful\n")
    return content

# Geração inicial
def generate(text, temperature):
    
    messages = [
        {"role": "system", "content": "Você é um profissional que trabalha em uma fábrica e é responsável por montar as Ordens de Serviços de manutenção das máquinas"},
        {"role": "user", "content": f"Você recebeu um audio de seu supervisor, que está transcrito aqui:\n {text}\n\n Interprete esse texto e retorne em tópicos o que deve ser feito pela equipe de manutenção. Responda apenas com os tópicos das tarefas que devem ser feitas com o máximo de detalhes possível."}
    ]
    generated_answer = request_generation(messages, temperature)
    return generated_answer, messages

# Filtragem do ´´´ gerado pelo gpt
def extract_code(code, only_code):
    code_blocks = []
    is_code = only_code

    lines = code.split("\n")
    for line in lines:
        if "```" in line:
            is_code = not is_code
        elif is_code:
            code_blocks.append(line)
    
    extracted_code = "\n".join(code_blocks)
    return extracted_code

def remove_noise(code):
    if "```" in code:
        return extract_code(code, False)
    else:
        return extract_code(code, True)

# Re-geração no formato json
def generate_SO(context, modelo, conteudocsv, temperature):
    
    messages = [
        {"role": "user", "content": f"Considere o contexto de mensagens:\n {context}\n\n, retorne essas tarefas no formato de diversas ordens de serviço, utilize o formato deste json para estruturar as ordens de serviço:\n {modelo}\n\n. Retorne apenas o conteudo do json. Não invente informações, o que você não tiver de informação deverá ser deixado em branco. Considere também as informações relacionadas a itens de reparo e EPIs utilizadas no reparo:\n {conteudocsv}\n\n Não invente códigos para coisas que não estão na lista. O status de todas as atividades deve ser 'aprovado'. O id de cada máquina é a sequencia de letras e numeros fornecida nas instruções, ex: A1,B2."}
    ]
    generated_answer = request_generation(messages, temperature)
    generated_answer = remove_noise(generated_answer)
    return generated_answer, messages

###########################################

with open("teste3/textoexemplo3.txt", "r") as file:
    text = file.read()

generated_answer, messages = generate(text, 0.5)
print(generated_answer)

with open("teste3/resposta3.txt", "w") as file:
    file.write(generated_answer)

###########################################

with open("documentos/codigosSAP.csv", mode="r", newline="") as file:
        leitor_csv = csv.reader(file)
        conteudocsv = list(leitor_csv)

###########################################

with open("osmodelo.txt", "r") as file:
    modelo = file.read()    

generated_answer, messages = generate_SO(messages, modelo, conteudocsv, 0.5)
with open("teste3/respostaSO3.json", "w") as file:
    file.write(generated_answer)