# Projeto: Sistema de Identificação de Golpes Digitais

## Descrição

Este projeto tem como objetivo desenvolver um site para ajudar pessoas a identificar sinais de golpes digitais, especialmente aqueles relacionados a links suspeitos, mensagens fraudulentas, conversas de WhatsApp, pedidos de PIX e outros tipos de fraude por engenharia social.

A solução visa fornecer uma análise simples e acessível, alertando o usuário antes que ele clique em um link, envie dinheiro ou compartilhe dados pessoais.

---

## Problema

Muitas pessoas caem em golpes por:
- clicar em links falsos;
- receber mensagens urgentes pedindo PIX;
- interagir com perfis ou contas suspeitas;
- aceitar promessas impossíveis de dinheiro ou benefício;
- compartilhar dados pessoais sem verificar a origem da mensagem.

O projeto busca reduzir esse risco por meio de uma ferramenta que analisa o conteúdo recebido e indica se ele parece fraudulento.

---

## Objetivo

Criar um MVP funcional de um site que permita:
- analisar links suspeitos;
- verificar mensagens e conversas;
- detectar sinais de phishing e fraude;
- indicar nível de risco;
- explicar em linguagem simples por que o conteúdo pode ser perigoso;
- orientar o usuário a agir com segurança.

---

## Público-alvo

- usuários comuns da internet;
- pessoas que usam redes sociais e aplicativos de mensagens;
- pessoas vulneráveis a golpes financeiros;
- pessoas com pouco conhecimento em segurança digital;
- consumidores que recebem pedidos de PIX, links ou mensagens suspeitas;
- qualquer pessoa que queira verificar se um conteúdo é confiável antes de agir.

---

## Funcionalidades do MVP

### 1. Análise de links
O usuário pode inserir um link e o sistema verifica se ele tem características suspeitas.

### 2. Análise de mensagem
O usuário pode colar um texto ou mensagem para identificar se há indícios de golpe.

### 3. Análise de conversa ou print
O usuário pode enviar uma imagem ou print de conversa para o sistema analisar.

### 4. Classificação de risco
O sistema pode indicar:
- baixo risco;
- risco moderado;
- alto risco;
- provável golpe.

### 5. Explicação em linguagem simples
A resposta deve ser clara e acessível, explicando o porquê do alerta.

### 6. Recomendações de segurança
O sistema pode orientar o usuário sobre ações seguras, como:
- confirmar a fonte;
- não clicar em links duvidosos;
- não enviar PIX sem confirmação;
- não compartilhar dados pessoais.

---

## Arquitetura proposta

O projeto pode ser estruturado em camadas:

### Frontend
- interface web para inserir links, mensagens e imagens;
- páginas de análise e resultados;
- responsividade para celular e desktop.

### Backend
- API para receber entradas do usuário;
- processamento da análise;
- lógica de regras e classificação;
- retorno dos resultados ao frontend.

### Módulo de análise
- regras heurísticas para detectar sinais de fraude;
- uso de IA para interpretar contexto e explicar o risco;
- combinação de regras e inteligência artificial.

### Persistência
- armazenamento de históricos e logs;
- uso de banco de dados leve para MVP.

---

## Tecnologias sugeridas

### Frontend
- HTML
- CSS
- JavaScript
- React (opcional)

### Backend
- Python
- Flask ou FastAPI

### Banco de dados
- SQLite para MVP
- PostgreSQL em evolução

### IA
- APIs de modelos de linguagem para análise de texto e explicação do risco
- OCR para leitura de imagens e prints

---

## Fluxo de uso

1. O usuário acessa a plataforma.
2. Escolhe o tipo de análise: link, mensagem ou print.
3. Envia o conteúdo suspeito.
4. O sistema analisa o texto ou link.
5. O sistema classifica o risco.
6. O usuário recebe um alerta com justificativa e orientações de segurança.

---

## Objetivo do MVP

O MVP deve validar a proposta do projeto com uma solução útil, simples e funcional, focada em:
- detecção de golpes;
- prevenção de fraudes;
- educação digital;
- apoio prático para pessoas comuns.

---

## Entregáveis previstos

- interface web funcional;
- backend com endpoints de análise;
- módulo de análise de links e mensagens;
- classificação de risco;
- explicação do alerta em linguagem simples;
- documentação básica do projeto.

---

## Status do projeto

Este repositório contém a documentação inicial e o contexto do projeto, incluindo:
- visão geral do problema;
- objetivo do MVP;
- arquitetura proposta;
- planejamento por sprints;
- contexto do desenvolvimento.

---

## Próximos passos

- desenvolver a interface inicial;
- implementar o backend;
- criar a lógica de regras de análise;
- integrar IA para interpretação contextual;
- validar o MVP com casos reais de fraude;
- melhorar a experiência do usuário.

---

## Licença

Este projeto pode ser distribuído e utilizado conforme a licença adotada no repositório.

---

## Conclusão

Este projeto tem grande potencial para ajudar pessoas a reconhecerem golpes digitais antes que elas ajam por impulso, evitando perdas financeiras e reduzindo riscos de fraude. A proposta combina tecnologia, segurança digital e educação, tornando a internet mais segura para o usuário comum.
