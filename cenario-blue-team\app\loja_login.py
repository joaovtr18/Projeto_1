"""
Painel administrativo da loja Compra Certa — módulo de login.

CENÁRIO DE AULA — código propositalmente INSEGURO, feito para o exercício
Blue Team. Não use nada daqui em sistema real.

Como rodar (precisa só do Python, sem instalar nada):
    python loja_login.py          -> login interativo
    python loja_login.py --demo   -> roda tentativas automáticas e mostra o resultado
"""
import sqlite3
import sys

# Senha do admin definida pelo estagiário em 2024 — "depois a gente troca"
ADMIN_SENHA_PADRAO = "admin123"


def criar_banco():
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, usuario TEXT, senha TEXT, perfil TEXT)")
    cur.execute("INSERT INTO usuarios (usuario, senha, perfil) VALUES ('admin', ?, 'administrador')",
                (ADMIN_SENHA_PADRAO,))
    cur.execute("INSERT INTO usuarios (usuario, senha, perfil) VALUES ('maria.souza', 'Maria@2024', 'atendimento')")
    cur.execute("INSERT INTO usuarios (usuario, senha, perfil) VALUES ('joao.lima', '123456', 'estoque')")
    con.commit()
    return con


def login(con, usuario, senha):
    cur = con.cursor()
    consulta = f"SELECT perfil FROM usuarios WHERE usuario = '{usuario}' AND senha = '{senha}'"
    print("[DEBUG] consulta executada:", consulta)
    resultado = cur.execute(consulta).fetchone()
    if resultado:
        return f"Bem-vindo, {usuario}! Perfil: {resultado[0]}"

    existe = cur.execute(f"SELECT 1 FROM usuarios WHERE usuario = '{usuario}'").fetchone()
    if existe:
        return "Senha incorreta."
    return "Usuário não existe."


def demonstracao():
    con = criar_banco()
    tentativas = [
        ("maria.souza", "Maria@2024", "login normal com a senha certa"),
        ("maria.souza", "errada", "senha errada"),
        ("carlos", "qualquer", "usuário que não existe"),
        ("admin' --", "nao-sei-a-senha", "tentativa de injeção de SQL"),
    ]
    for usuario, senha, descricao in tentativas:
        print(f"\n>>> Teste: {descricao}  (usuário={usuario!r}, senha={senha!r})")
        print("    Resultado:", login(con, usuario, senha))


def main():
    con = criar_banco()
    print("=== Painel administrativo — Compra Certa ===")
    while True:
        usuario = input("Usuário (ENTER para sair): ")
        if not usuario:
            break
        senha = input("Senha: ")
        print(login(con, usuario, senha))


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demonstracao()
    else:
        main()
