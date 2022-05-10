from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from Grafo import *
import pygame

class App:
    labirintoMatriz = []
    posRato = []
    posSaida = []

    def __init__(self, master):
        frame = Frame(master)
        frame.grid(row = 0, column = 0, sticky = (N, W, E, S))

        self.grupoBotoes = LabelFrame(master, text = "Labirinto do Rato", labelanchor = N)
        self.grupoBotoes.grid(row = 0, column = 0, sticky = (N, S))

        botaoCarregarLabirinto = Button(self.grupoBotoes, text = "Carregar Labirinto", width = 18, command = self.carregarLabirinto)
        botaoCarregarLabirinto.grid(row = 0, column = 0)

        self.botaoInserirPosicoes = Button(self.grupoBotoes, text = "Inserir Posições (Rato e saida)", width = 18, command = self.janelaPosicoes, state = DISABLED)
        self.botaoInserirPosicoes.grid(row = 1, column = 0)

        self.botaoMostrarCaminho = Button(self.grupoBotoes, text = "Mostrar Caminho do Rato", width = 18, command = self.mostrarCaminho, state = DISABLED)
        self.botaoMostrarCaminho.grid(row = 2, column = 0)

    def carregarLabirinto(self):
        arquivo = filedialog.askopenfilename(title = "Selecione o labirinto:", defaultextension = ".csv")

        matriz = converterCSVemMatriz(arquivo)

        self.labirintoMatriz = matriz
        self.posRato = []
        self.posSaida = []
        self.atualizarInformacoes()


    def janelaPosicoes(self):
        if len(self.labirintoMatriz) == 0:
            messagebox.showinfo("Erro", "Labirinto Inválido, carregue outro.")
        else:
            janela = Toplevel(None)
            janela.title("Inserir")

            textoInfo = Message(janela, text = "Insira as posições X e Y: ", width = 150)
            textoInfo.grid(row = 0, column = 0, columnspan = 3, sticky = (E, W))

            textoInfo2 = Message(janela, text = "OBS: Valores padrao pare resoler o problema:       Rato: 2 e 7, Saida: 34 e 1", width = 150)
            textoInfo2.grid(row = 1, column = 0, columnspan = 3, sticky = (E, W))

            textoInfo2 = Message(janela, text = "X            Y")
            textoInfo2.grid(row = 2, column = 1, columnspan = 2, sticky = (E, W))

            textoRato = Message(janela, text = "Rato: ")
            textoRato.grid(row = 3, column = 0, sticky = (E, W))
            
            entradaRatoX = Entry(janela, width = 5)
            entradaRatoX.grid(row = 3, column = 1, sticky = (E, W))
            entradaRatoY = Entry(janela, width = 5)
            entradaRatoY.grid(row = 3, column = 2, sticky = (E, W))

            textoSaida = Message(janela, text = "Saida: ")
            textoSaida.grid(row = 4, column = 0, sticky = (E, W))

            entradaSaidaX = Entry(janela, width = 5)
            entradaSaidaX.grid(row = 4, column = 1, sticky = (E, W))
            entradaSaidaY = Entry(janela, width = 5)
            entradaSaidaY.grid(row = 4, column = 2, sticky = (E, W))

            botaoInserir = Button(janela, text = "Inserir", command = lambda: self.inserirPosicoes(entradaRatoX.get(), entradaRatoY.get(), entradaSaidaX.get(), entradaSaidaY.get()))

            botaoInserir.grid(row = 5, column = 0, columnspan = 3, sticky = (E, W))

    def inserirPosicoes(self, ratoX, ratoY, saidaX, saidaY):
        erro = 0

        try:
            ratoX = int(ratoX)
            ratoY = int(ratoY)
            saidaX = int(saidaX)
            saidaY = int(saidaY)

            if erro == 0:
                messagebox.showinfo("Sucesso!", "Valores inseridos com sucesso.")
                self.posRato = [ratoX - 1, ratoY - 1]
                self.posSaida = [saidaX - 1, saidaY - 1]
            self.atualizarInformacoes()
        except:
            messagebox.showinfo("Erro", "Um ou mais dos valores é inválido.")

    def mostrarCaminho(self):
        grafo = Grafo(converterLabirintoEmGrafo(self.labirintoMatriz))
        rato = grafo.encontrarVerticePorPosicao(self.posRato[0], self.posRato[1])
        saida = grafo.encontrarVerticePorPosicao(self.posSaida[0], self.posSaida[1])
        caminho = grafo.buscaEmLargura(rato, saida)
        if len(caminho) == 0:
            messagebox.showinfo("Erro", "O rato não tem como chegar até a Saida.")
        else:
            caminhoDesenhar = []
            delayAnimacao = 250
            tamanhoCubo = 32
            pygame.init()

            PAREDE    =  (0, 0, 0)
            FUNDO    =  (255, 255, 255)
            RATO     =  (185, 125, 50)
            SAIDA   =  (255, 255, 0)
            CAMINHO  =  (150, 150, 150)
            LINHA    =  (150, 150, 150)

            loop = True
            size = (len(self.labirintoMatriz[0]) * tamanhoCubo + (tamanhoCubo * 2), len(self.labirintoMatriz) * tamanhoCubo + (tamanhoCubo * 2))
            tela = pygame.display.set_mode(size)
            pygame.display.set_caption("Demonstração do Caminho do Rato")

            clock = pygame.time.Clock()
            tickAtual = pygame.time.get_ticks()
            tickTroca = tickAtual + delayAnimacao
            iAnimacao = 1
            loop = True

            while loop:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loop = False

                tela.fill(FUNDO)
                for y in range(len(self.labirintoMatriz)):
                    for x in range(len(self.labirintoMatriz[0])):
                        if self.labirintoMatriz[y][x] == -1:
                            pygame.draw.rect(tela, PAREDE, [tamanhoCubo + (x * tamanhoCubo), tamanhoCubo + (y * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)
                        else:
                            pygame.draw.rect(tela, FUNDO, [tamanhoCubo + (x * tamanhoCubo), tamanhoCubo + (y * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)

                for i in range(len(caminhoDesenhar)):
                    posCaminho = caminhoDesenhar[i].getPosXY()
                    pygame.draw.rect(tela, LINHA, [tamanhoCubo + (posCaminho[0] * tamanhoCubo), tamanhoCubo + (posCaminho[1] * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)

                tickAtual = pygame.time.get_ticks()
                if tickAtual > tickTroca:
                    tickTroca = tickAtual + delayAnimacao
                    caminhoDesenhar.append(caminho[iAnimacao])
                    iAnimacao += 1
                    if iAnimacao == len(caminho):
                        iAnimacao = 1
                        caminhoDesenhar = []

                pygame.draw.rect(tela, RATO, [tamanhoCubo + (rato.getPosXY()[0] * tamanhoCubo), tamanhoCubo + (rato.getPosXY()[1] * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)
                pygame.draw.rect(tela, SAIDA, [tamanhoCubo + (saida.getPosXY()[0] * tamanhoCubo), tamanhoCubo + (saida.getPosXY()[1] * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)

                for i in range(0, len(self.labirintoMatriz[0]) + 1):
                    pygame.draw.line(tela, LINHA, [(i * tamanhoCubo) + tamanhoCubo, tamanhoCubo], [(i * tamanhoCubo) + tamanhoCubo, (len(self.labirintoMatriz) + 1) * tamanhoCubo], 1)

                for i in range(0, len(self.labirintoMatriz) + 1):
                    pygame.draw.line(tela, LINHA, [tamanhoCubo, (i * tamanhoCubo) + tamanhoCubo], [(len(self.labirintoMatriz[0]) + 1) * tamanhoCubo, (i * tamanhoCubo) + tamanhoCubo], 1)
                pygame.display.flip()

                clock.tick(60)
            pygame.quit()

    def atualizarInformacoes(self):
        if len(self.labirintoMatriz) > 0:
            self.botaoInserirPosicoes.config(state = NORMAL)
            if self.posRato != [] and self.posSaida != []:
                self.botaoMostrarCaminho.config(state = NORMAL)
            self.labirintoCarregado.set()
            self.labirintoTamanho.set(str(len(self.labirintoMatriz[0]))+ str(len(self.labirintoMatriz)))

        if len(self.posRato) > 0 and len(self.posSaida) > 0:
            self.stringPosicaoRato.set(str(self.posRato[0] + 1) + str(self.posRato[1] + 1))
            self.stringPosicaoSaida.set(str(self.posSaida[0] + 1) + str(self.posSaida[1] + 1))
