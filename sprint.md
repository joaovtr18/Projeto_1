# Plano de Sprints para o MVP: Detecção de Golpes via Links, PIX e Mensagens Suspeitas

## 1. Visão geral

Este documento descreve as fases de implementação do projeto, desde a ideação até a entrega do MVP funcional. O objetivo é transformar a ideia inicial em um produto mínimo útil, com foco em prevenção de golpes digitais, identificação de links suspeitos, mensagens fraudulentas e alertas relevantes para o usuário.

O projeto será desenvolvido em etapas organizadas por sprints, permitindo validar hipótese, reduzir riscos, ajustar requisitos e evoluir de forma incremental.

---

## 2. Objetivo do projeto

Criar um site que ajude pessoas comuns a identificar sinais de golpes em links, mensagens, conversas e solicitações de pagamento, especialmente relacionadas a PIX e fraude digital. O sistema deve ser simples, acessível e útil para qualquer pessoa que queira verificar se uma mensagem ou link é suspeito antes de agir.

---

## 3. Objetivo do MVP

O MVP deve entregar uma solução funcional que permita:
- inserir um link suspeito;
- analisar uma mensagem ou conversa;
- identificar indicadores de risco;
- mostrar alerta com classificação de risco;
- explicar, em linguagem simples, por que o conteúdo foi considerado suspeito;
- fornecer orientação ao usuário com relação ao que evitar.

O principal foco do MVP é validar a proposta de valor, demonstrar utilidade real, e entregar uma aplicação funcional que ajude a reduzir o risco de golpes.

---

## 4. Filosofia do desenvolvimento por sprints

A implementação será dividida em ciclos curtos com objetivos claros. Cada sprint terá:
- objetivo principal;
- entregáveis esperados;
- critérios de aceitação;
- validação e revisão;
- ajustes conforme feedback.

Isso permite evoluir o produto com segurança, sem perder foco na funcionalidade principal.

---

## 5. Sprint 0 – Ideação e definição do problema

### Objetivo
Definir claramente o problema, o público, a proposta de valor e os primeiros requisitos do sistema.

### Atividades
- Revisão da dor do usuário: golpes por links, PIX, mensagens e conversas suspeitas.
- Definição do problema central: "como ajudar pessoas a identificar golpes antes de clicarem ou transferirem dinheiro?"
- Registro do público-alvo: usuários comuns, pessoas vulneráveis a fraudes e usuários com baixa familiaridade em segurança digital.
- Definição da solução proposta: um site para análise de risco.
- Levantamento inicial de requisitos funcionais e não funcionais.
- Criação da visão geral do MVP.
- Definição das regras iniciais de análise.

### Entregáveis
- Documento com a descrição da dor e do problema.
- Definição do público-alvo.
- Lista inicial de funcionalidades.
- Visão geral do produto.

### Critérios de aceitação
- O problema e a proposta de valor ficam claros.
- A ideia do MVP está bem definida.
- Há consenso sobre o escopo inicial.

### Resultado esperado
Base sólida para iniciar o desenvolvimento com foco no problema correto.

---

## 6. Sprint 1 – Levantamento de requisitos e arquitetura inicial

### Objetivo
Estruturar os requisitos e preparar uma arquitetura simples e funcional para o MVP.

### Atividades
- Definição dos casos de uso:
  - análise de link;
  - análise de mensagem;
  - análise de conversa ou print;
  - alerta de risco.
- Definição de requisitos funcionais:
  - receber entrada do usuário;
  - processar conteúdo suspeito;
  - aplicar regras de análise;
  - classificar risco;
  - exibir atenção ao usuário.
- Definição de requisitos não funcionais:
  - simplicidade de uso;
  - resposta rápida;
  - interface clara;
  - segurança básica;
  - acessibilidade.
- Criação da arquitetura do sistema:
  - frontend;
  - backend;
  - módulo de análise;
  - integração com IA;
  - banco de dados.
- Escolha das tecnologias iniciais.

### Entregáveis
- Documento de requisitos.
- Diagrama da arquitetura inicial.
- Definição da stack tecnológica.

### Critérios de aceitação
- As funções essenciais do sistema foram definidas.
- A arquitetura está coerente com o escopo do MVP.
- Há um caminho claro para implementação.

### Resultado esperado
Uma base técnica e funcional pronta para a construção do primeiro protótipo.

---

## 7. Sprint 2 – Prototipação da interface e experiência do usuário

### Objetivo
Desenvolver a primeira versão da interface que permita ao usuário enviar conteúdo e visualizar o resultado da análise.

### Atividades
- Definição da estrutura do site.
- Criação da homepage com foco em experiência de usuário.
- Protótipo de telas:
  - tela inicial;
  - tela de análise de link;
  - tela de análise de mensagem;
  - tela de alerta de risco;
  - tela de histórico ou resultados.
- Definição da linguagem visual:
  - cores;
  - alertas;
  - mensagens de risco;
  - usabilidade mobile-first.
- Validação do fluxo do usuário.

### Entregáveis
- Protótipo visual da interface.
- Fluxo de navegação da aplicação.
- Esqueleto da página inicial e telas principais.

### Critérios de aceitação
- O usuário consegue identificar rapidamente como usar o sistema.
- O fluxo principal é simples e intuitivo.
- O protótipo comunica bem o objetivo do produto.

### Resultado esperado
Interface funcional para servir como base para a implementação do sistema.

---

## 8. Sprint 3 – Estruturação do backend e APIs

### Objetivo
Implementar a base da aplicação no backend para receber dados do front e preparar as rotas de análise.

### Atividades
- Configuração do ambiente do backend.
- Criação da estrutura de pastas da aplicação.
- Implementação das rotas iniciais:
  - POST /analise-link
  - POST /analise-mensagem
  - POST /analise-imagem
- Criação do fluxo de entrada e saída de dados.
- Definição do modelo de resposta da API.
- Estruturação das respostas com campos como:
  - risco;
  - categoria;
  - explicação;
  - recomendações.

### Entregáveis
- API inicial funcionando.
- Estrutura padrão de retorno de análise.
- Endpoints para entrada de dados.

### Critérios de aceitação
- O backend recebe dados do frontend e responde adequadamente.
- As rotas funcionam de forma consistente.
- O formato da resposta está preparado para integração com IA e frontend.

### Resultado esperado
Backend operacional, pronto para receber a lógica de análise e classificação.

---

## 9. Sprint 4 – Módulo de detecção de risco e regras heurísticas

### Objetivo
Criar a lógica inicial de análise para detectar sinais de fraude sem depender totalmente de IA.

### Atividades
- Definição de regras para avaliar links:
  - encurtadores;
  - domínio suspeito;
  - texto de urgência;
  - promessas exageradas;
  - uso de clones ou nomes parecidos.
- Definição de regras para mensagens:
  - pedidos de PIX;
  - gritos de alerta;
  - incentivo à urgência;
  - incentivo para clicar em links sem checagem;
  - tentativa de manipulação emocional.
- Definição de regras para conversas:
  - cargos de pressa;
  - pedidos de dados pessoais;
  - solicitações de senha ou código;
  - promessas de retorno financeiro fácil.
- Criação de pontuação ou classificação por nível de risco.

### Entregáveis
- Módulo de heurísticas funcionando.
- Sistema de classificação de risco.
- Lógica inicial de alerta.

### Critérios de aceitação
- O sistema consegue classificar textos e links com base em sinais de fraude.
- As respostas são coerentes e úteis ao usuário.
- Há uma base que pode evoluir para IA.

### Resultado esperado
Primeira versão da solução de detecção de risco funcional.

---

## 10. Sprint 5 – Integração com IA para análise contextual

### Objetivo
Adicionar inteligência artificial para melhorar a análise de contexto e a explicação do risco.

### Atividades
- Integração com API de IA para analisar texto e mensagens.
- Criação de prompts para detectar sinais de golpe.
- Extração do contexto da mensagem e explicação em linguagem simples.
- Ajuste da análise para responder: "por que isso parece perigoso?"
- Implementação de recomendações práticas, como:
  - não clicar no link;
  - verificar a fonte;
  - não enviar dinheiro sem confirmação;
  - entrar em contato pela via oficial.

### Entregáveis
- Integração com IA funcionando.
- Respostas inteligentes e explicáveis.
- Explicação em linguagem simples para o usuário final.

### Critérios de aceitação
- A IA consegue analisar mensagens e gerar uma explicação útil.
- A resposta ajuda o usuário a entender o risco.
- A proposta de valor do sistema fica clara.

### Resultado esperado
Sistema mais preciso e mais próximo da experiência real do usuário.

---

## 11. Sprint 6 – Suporte a prints e OCR

### Objetivo
Permitir que o usuário envie imagens e o sistema consiga extrair texto para análise.

### Atividades
- Criação do fluxo de upload de imagem.
- Implementação de OCR para extração de texto.
- Processamento de prints de conversas.
- Análise do texto capturado junto com regras de fraude.
- Ajuste da resposta para considerar imagens e conversas.

### Entregáveis
- Fluxo de upload de print.
- OCR funcionando.
- Análise de conteúdo visual convertida em texto para avaliação.

### Critérios de aceitação
- A imagem pode ser enviada.
- O texto extraído é processado corretamente.
- A análise considera o conteúdo do print.

### Resultado esperado
Sistema mais completo e útil para cenários reais.

---

## 12. Sprint 7 – Histórico, persistência e usabilidade

### Objetivo
Dar mais valor ao sistema com persistência de dados e histórico de análises.

### Atividades
- Criação de banco de dados para salvar registros.
- Armazenamento de:
  - tipo de análise;
  - conteúdo enviado;
  - classificação de risco;
  - data e hora;
  - explicação gerada.
- Criação de histórico no painel do usuário.
- Melhorias visuais e de usabilidade.
- Ajustes de layout para mobile.

### Entregáveis
- Histórico de análises.
- Persistência de dados.
- Melhor experiência de uso.

### Critérios de aceitação
- O usuário consegue acompanhar os resultados anteriores.
- O sistema comporta uso real e recorrente.
- A experiência de uso fica mais robusta.

### Resultado esperado
Sistema mais preparado para uso contínuo e validação real.

---

## 13. Sprint 8 – Testes, ajuste de regras e validação do MVP

### Objetivo
Validar se o sistema realmente atende ao propósito do projeto e identificar melhorias necessárias antes da entrega.

### Atividades
- Testes funcionais de todos os fluxos principais.
- Testes de análise de link, mensagem e imagem.
- Teste de casos positivos e negativos.
- Ajuste de regras heurísticas.
- Ajuste de prompts da IA.
- Validação do nível de risco em cenários reais.
- Coleta de feedback de forma simples.

### Entregáveis
- Relatório de testes.
- Ajustes feitos com base em validação.
- Versão estável do MVP.

### Critérios de aceitação
- O sistema responde corretamente em cenários reais de uso.
- Não há falhas graves no fluxo principal.
- O produto cumpre os objetivos do MVP.

### Resultado esperado
MVP validado e pronto para apresentação.

---

## 14. Sprint 9 – Preparação para entrega e apresentação do MVP

### Objetivo
Finalizar a entrega do MVP para demonstração pública ou apresentação acadêmica.

### Atividades
- Revisão final do código.
- Limpeza de bugs e ajustes visuais.
- Organização dos arquivos do projeto.
- Criação do README e documentação básica.
- Preparação de apresentação com:
  - problema;
  - proposta;
  - solução;
  - arquitetura;
  - fluxos implementados;
  - resultados e próximos passos.

### Entregáveis
- MVP finalizado.
- Documentação de uso.
- Apresentação do projeto.

### Critérios de aceitação
- O sistema funciona de ponta a ponta.
- Há documentação básica suficiente para uso e apresentação.
- A proposta de valor do projeto está clara.

### Resultado esperado
Produto mínimo funcional pronto para entrega e validação.

---

## 15. Entregáveis do MVP final

Ao fim da sequência de sprints, o produto deve entregar:
- site funcional para análise de risco;
- entrada de link, mensagem e print;
- classificador de risco;
- respostas em linguagem simples;
- alertas de segurança;
- fluxo de uso intuitivo;
- documentação simples para execução e apresentação.

---

## 16. Próximos passos após o MVP

Depois da entrega do MVP, o projeto pode evoluir para:
- detecção de novos tipos de fraude;
- integração com APIs externas;
- uso de mais modelos de IA;
- análise de domínio e reputação de links;
- aumento do banco de dados de indicadores de fraude;
- painel administrativo para monitorar alertas;
- expansão para comunidades, escolas e organizações.

---

## 17. Conclusão

A implementação do projeto deve seguir uma lógica incremental, focada em validar a ideia com entregas reais em cada sprint. Começando pela dor do usuário e pelo problema central, passando pela arquitetura, interface, backend, regras de análise, IA e testes, o MVP evolui de forma segura até se tornar uma solução prática e útil para a prevenção de golpes digitais.

Esse processo permite que o time aprenda ao longo do desenvolvimento, valide a proposta rapidamente e entregue um produto com valor real para o público-alvo.
