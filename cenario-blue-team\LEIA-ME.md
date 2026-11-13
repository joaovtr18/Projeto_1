# Cenário Blue Team — "Plantão na madrugada da Compra Certa"

Exercício 1 · Normas, Padrões e Melhores Práticas · Segurança da Informação
**Cenário 100% fictício, para uso em sala.** Empresa, pessoas, IPs e senhas são inventados.

## Situação

Você entrou hoje na equipe de segurança (**Blue Team**) da **Compra Certa**, a loja online
que estamos estudando no Módulo 2.

Às **02:21** da madrugada de **22/10/2026**, o monitoramento de rede mandou um e-mail de
alerta (`docs/alerta-monitoramento.txt`). Ninguém viu. Às 08:47, o gerente de TI, **Paulo
Mendes**, leu o alerta, juntou os arquivos desta pasta e chamou você:

> "O monitoramento disparou um alerta estranho de madrugada. Não sei se fomos
> atacados ou se é alarme falso. Preciso saber até o fim do dia: **o que aconteceu,
> quem fez, o que vazou, se o atacante ainda tem acesso e o que a gente corrige primeiro**.
> Se tiver dado pessoal envolvido, a Luciana (nossa DPO) precisa saber."

Você vai investigar com a ajuda do agente de IA do **Google Antigravity**.

## O que tem nesta pasta

| Arquivo | O que é |
|---|---|
| `docs/alerta-monitoramento.txt` | o e-mail de alerta que começou tudo |
| `docs/inventario-ativos.md` | a lista oficial de equipamentos, sistemas e contas da empresa (desatualizada?) |
| `logs/access.log` | log do servidor web: cada linha é um acesso a uma página da loja (horário de Brasília) |
| `logs/app-painel.log` | log do painel administrativo: logins, mudanças e exportações (horário **UTC**) |
| `logs/auth.log` | log de acesso remoto (SSH) ao servidor (horário de Brasília) |
| `app/loja_login.py` | código do login do painel administrativo |
| `app/config.env` | configuração da loja em produção (publicada no site como `/.env`) |
| `infra/nginx.conf` | configuração do servidor web, o "porteiro" do site |
| `entregas/RELATORIO-INCIDENTE.md` | modelo do relatório que você vai preencher e entregar |

## Regras do exercício

1. **Tudo acontece só nesta pasta.** Não peça ao agente para acessar sites, IPs ou
   sistemas de verdade. Os IPs dos logs são de faixas reservadas para documentação e
   não pertencem a ninguém.
2. **Desconfie da IA.** Para cada conclusão, peça a **linha exata do log** ou do código
   que prova aquilo. Conclusão sem evidência não vale no relatório.
3. **Leia antes de aprovar.** Quando o agente pedir para rodar um comando ou alterar um
   arquivo, leia o que ele vai fazer antes de aceitar.
4. Se o código for alterado e ficar ruim, sem problema: o professor tem a versão original.

## Missões

0. **Preparação:** abrir a pasta e entender o que tem em cada arquivo.
1. **Entender o alerta e o inventário** (Identificar).
2. **Investigar o servidor web** no `access.log` (Detectar).
3. **Investigar o acesso remoto** no `auth.log` (Detectar).
4. **Cruzar com o log do painel** no `app-painel.log` (Detectar), atenção ao fuso horário.
5. **Corrigir as falhas** do código, da configuração e do servidor web (Proteger).
6. **Responder:** montar o relatório e o plano de ação (Responder e Recuperar).

O passo a passo de cada missão, com explicações e prompts sugeridos, está no caderno do
Exercício 1.
