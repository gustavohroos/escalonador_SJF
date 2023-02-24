import sys

class Tarefa:
    def __init__(self, nome, tempo):
        self.nome = nome
        self.tempo = tempo
        self.tempo_inicial = 0
        self.tempo_final = 0

    def __str__(self):
        return f"{self.nome};{self.tempo_inicial};{self.tempo_final}\n"
    
class Processador:
    def __init__(self, numero=0):
        self.numero = numero
        self.tarefas = []
        self.tempo_atual = 0

    def __str__(self):
        tarefas_str = "".join([str(tarefa) for tarefa in self.tarefas])
        return f"Processador_{self.numero}:\n{tarefas_str}\n"

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        tarefa.tempo_inicial = self.tempo_atual
        tarefa.tempo_final = self.tempo_atual + tarefa.tempo
        self.tempo_atual += tarefa.tempo

class Escalonador:
    def __init__(self, num_processadores=1, algoritmo="SJF"):
        self.num_processadores = num_processadores
        self.algoritmo = algoritmo
        self.processadores = [Processador(i) for i in range(num_processadores)]

    def escalonar(self, tarefas):
        if self.algoritmo == "SJF":
            tarefas.sort(key=lambda tarefa: tarefa.tempo)
        
        processador_atual = 0
        for tarefa in tarefas:
            self.processadores[processador_atual].adicionar_tarefa(tarefa)

            processador_atual = (processador_atual + 1) % self.num_processadores
        
    def exportar(self, arquivo="saida.txt"):
        with open(arquivo, "w") as f:
            for processador in self.processadores:
                f.write(str(processador))
            
def ler_tarefas(arquivo):
    tarefas = []
    with open(arquivo, "r") as f:
        for linha in f:
            nome, tempo = linha.split()
            tarefas.append(Tarefa(nome, int(tempo)))
    return tarefas

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python escalonador.py arquivo_de_entrada.txt num_processadores arquivo_de_saida.txt ex: python escalonador.py tarefas.txt 2 saida.txt")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    num_processadores = int(sys.argv[2])

    escalonador = Escalonador(num_processadores=num_processadores, algoritmo="SJF")
    tarefas = ler_tarefas(nome_arquivo)
    escalonador.escalonar(tarefas)
    escalonador.exportar(sys.argv[3])
