import tkinter as tk
from tkinter import messagebox

def buscar_usuario(nome_buscado, caminho_arquivo):
    resultados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            
            for linha in linhas:
                linha = linha.strip()
                dados = [dado.strip() for dado in linha.split(';')]
                
                if len(dados) == 3:
                    nome, idade, profissao = dados
                    if nome_buscado.lower() in nome.lower().split():
                        resultados.append((nome, idade, profissao, linha))
        
        return resultados
    except FileNotFoundError:
        return None

def realizar_busca():
    nome_buscado = entry_nome.get().strip()
    if not nome_buscado:
        messagebox.showwarning("Entrada inválida", "Por favor, insira um nome para buscar.")
        return
    caminho_arquivo = "Usuario.txt"  # Use o nome exato do arquivo
    resultados = buscar_usuario(nome_buscado, caminho_arquivo)
    for widget in frame_resultados.winfo_children():
        widget.destroy()
    if resultados:
        for i, (nome, idade, profissao, linha) in enumerate(resultados):
            tk.Label(frame_resultados, text=f"Nome: {nome}").grid(row=i, column=0, sticky='w', padx=10, pady=5)
            tk.Label(frame_resultados, text=f"Idade: {idade}").grid(row=i, column=1, sticky='w', padx=10, pady=5)
            tk.Label(frame_resultados, text=f"Profissão: {profissao}").grid(row=i, column=2, sticky='w', padx=10, pady=5)
            tk.Button(frame_resultados, text="Excluir", command=lambda linha=linha: excluir_usuario(linha)).grid(row=i, column=3, padx=10, pady=5)
    else:
        messagebox.showinfo("Resultado", f'Nenhum usuário encontrado com o nome "{nome_buscado}".')

def excluir_usuario(linha):
    if messagebox.askyesno("Confirmar exclusão", f"Você tem certeza que deseja excluir o usuário:\n{linha}"):
        try:
            with open("Usuario.txt", 'r', encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()
            with open("Usuario.txt", 'w', encoding='utf-8') as arquivo:
                for linha_arquivo in linhas:
                    if linha_arquivo.strip() != linha.strip():
                        arquivo.write(linha_arquivo)
            realizar_busca()  # Atualiza a lista de resultados
            messagebox.showinfo("Sucesso", "Usuário excluído com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível excluir o usuário: {e}")

def abrir_janela_cadastro():
    janela_cadastro = tk.Toplevel(root)
    janela_cadastro.title("Cadastro de Novo Usuário")
    
    tk.Label(janela_cadastro, text="Nome:").pack(padx=10, pady=5)
    entry_nome_cadastro = tk.Entry(janela_cadastro, width=50)
    entry_nome_cadastro.pack(padx=10, pady=5)
    
    tk.Label(janela_cadastro, text="Idade:").pack(padx=10, pady=5)
    entry_idade_cadastro = tk.Entry(janela_cadastro, width=50)
    entry_idade_cadastro.pack(padx=10, pady=5)
    
    tk.Label(janela_cadastro, text="Profissão:").pack(padx=10, pady=5)
    entry_profissao_cadastro = tk.Entry(janela_cadastro, width=50)
    entry_profissao_cadastro.pack(padx=10, pady=5)
    
    def salvar_usuario():
        nome = entry_nome_cadastro.get().strip()
        idade = entry_idade_cadastro.get().strip()
        profissao = entry_profissao_cadastro.get().strip()
        
        if not nome or not idade or not profissao:
            messagebox.showwarning("Entrada inválida", "Todos os campos devem ser preenchidos.")
            return
        
        try:
            with open("Usuario.txt", 'a', encoding='utf-8') as arquivo:
                arquivo.write(f"{nome};{idade};{profissao}\n")
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso.")
            janela_cadastro.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o usuário: {e}")
    
    tk.Button(janela_cadastro, text="Salvar", command=salvar_usuario).pack(pady=10)

# Criar a janela principal
root = tk.Tk()
root.title("Busca de Usuário")

# Criar e posicionar os widgets
tk.Label(root, text="Digite o primeiro nome ou sobrenome do usuário:").pack(padx=10, pady=5)

entry_nome = tk.Entry(root, width=50)
entry_nome.pack(padx=10, pady=5)

tk.Button(root, text="Buscar", command=realizar_busca).pack(padx=10, pady=5)

frame_resultados = tk.Frame(root)
frame_resultados.pack(padx=10, pady=5)

tk.Button(root, text="Cadastrar Novo Usuário", command=abrir_janela_cadastro).pack(padx=10, pady=5)

root.mainloop()
