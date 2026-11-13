# Inventário de Ativos de TI — Compra Certa

**Última atualização:** 14/03/2024 · **Responsável:** Equipe de TI
*Cenário de aula: dados fictícios.*

| # | Ativo | Tipo | Onde fica | Dono | Dados que guarda | Classificação | Observação |
|---|---|---|---|---|---|---|---|
| 1 | web01 | servidor | nuvem, IP público | TI / Infra | nenhum (só repassa) | Interno | servidor web da loja (nginx + aplicação) |
| 2 | db01 (10.0.1.20) | banco de dados | rede interna | TI / Infra | clientes, pedidos, usuários do painel | Confidencial | backup diário às 23h |
| 3 | Painel administrativo | aplicação | web01 | Comercial | acesso aos clientes e pedidos | Confidencial | **acesso apenas pela rede interna** |
| 4 | Gateway de pagamento | serviço de terceiro | fornecedor externo | Financeiro | dados de cartão (não ficam na loja) | Restrito | integração por token |
| 5 | Backups do banco | arquivo | armazenamento em nuvem | TI / Infra | cópia completa do db01 | Confidencial | retenção 30 dias, **restauração nunca testada** |
| 6 | Notebook do deploy | estação | escritório (10.0.0.5) | TI / Dev | chave SSH de acesso ao web01 | Interno | usado para publicar novas versões |

## Contas com acesso de administrador ao painel

| Usuário | Pessoa | Setor |
|---|---|---|
| admin | conta compartilhada da TI | TI |
| maria.souza | Maria Souza | Atendimento |

## Contatos para incidente

| Papel | Nome |
|---|---|
| Gerente de TI | Paulo Mendes |
| Encarregado de Dados (DPO) | Luciana Ferraz |
| Responsável pelo gateway | suporte do fornecedor |
