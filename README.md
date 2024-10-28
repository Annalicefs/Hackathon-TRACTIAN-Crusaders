# Crusaders - Hackathon Tractian

### Descrição do Projeto

A equipe Crusaders desenvolveu uma solução que utiliza a API da OpenAI para transformar informações imprecisas, fornecidas por supervisores, em ordens de serviço (OS) detalhadas, formatadas e ordenadas por prioridade. Essa abordagem visa garantir que os funcionários recebam instruções claras e precisas, otimizando o fluxo de trabalho e minimizando erros na execução de tarefas.

### Objetivo

O objetivo do projeto é facilitar o processo de criação e padronização das ordens de serviço, utilizando inteligência artificial para melhorar a comunicação entre supervisores e operadores. Com isso, espera-se uma melhora na eficiência operacional e uma redução na quantidade de erros na produção.

Além disto, também foi criado um sistema de priorização de OSs, ordenados por nível de urgencia, disponibilidade de funcionários no dia e ferramentas disponíveis no almoxarifado.

## Arquitetura do Projeto
### Componentes Principais

API OpenAI (openaiSOcreate.py): O arquivo principal que processa as informações fornecidas pelos supervisores, transformando-as em ordens de serviço detalhadas. A IA extrai o máximo de detalhes para uma estrutura precisa e compreensível.

Banco de Dados MongoDB: Utilizando pyMongo, o projeto mantém um banco de dados robusto com:

- Informações dos funcionários (habilidades, turnos, entre outros dados relevantes).

- Dados das linhas de montagem da fábrica.

- Inventário das ferramentas disponíveis no almoxarifado.

### Tecnologias

- Python: Linguagem principal utilizada na implementação.
- API da OpenAI: Para processamento de linguagem natural e formatação das OS.
- PyMongo: Para a integração com o banco de dados MongoDB.
