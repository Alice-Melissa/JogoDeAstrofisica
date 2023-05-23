import pygame
import sys

# Definir a classe de pergunta
class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

# Criar a lista de perguntas
questions = [
    Question("Quantos planetas existem no sistema solar?", ["8", "9", "7"], 0),
    Question("Qual das opções não é um planeta do sistema solar?", ["Plutão", "Vênus", "Marte"], 0),
    Question("Quem são os planetas gasosos?", ["Terra, Marte e Vênus", "Júpiter, Saturno, Urano e Netuno", "Júpiter, Saturno, Urano e Vênus"], 1),
    Question("Quem são os planetas rochosos?", ["Saturno, Urano e Terra", "Mercúrio, Vênus, Terra e Marte", "Saturno, Vênus, Terra e Marte"], 1),
    Question("Qual o planeta mais próximo do Sol?", ["Marte", "Mercúrio", "Vênus"], 1),
    Question("Qual o nome do movimento da terra em torno do sol?", ["Translação", "Nutação", "Rotação"], 0),
    Question("Qual é o nome da galáxia mais próxima da nossa?", ["Via Láctea", "Andrômeda", "Triângulo"], 1),
    Question("De qual galáxia é a foto do buraco negro?", ["Via Láctea", "Messier 87", "Andrômeda"], 1),
    Question("Qual é o formato da nossa galáxia?", ["Espiral", "Elíptica", "Irregular"], 0),
    Question("Quanto tempo demora para a luz do sol chegar na Terra?", ["8 minutos e 18 segundos", "9 minutos e 17 segundos", "7 minutos e 20 segundos"], 0),
    Question("O que é uma supernova?", ["Um buraco negro em formação", "A explosão de uma estrela", "Uma chuva de meteoros"], 1),
    Question("O que é a matéria escura?", ["Matéria que não emite luz", "Matéria que absorve a luz", "Matéria que reflete a luz"], 0),
    Question("O que é a radiação cósmica de fundo?", ["Radiação emitida pelo Sol", "Radiação emitida pela Terra", "Radiação emitida pela explosão do Big Bang"], 2),
    Question("Qual é a temperatura média do Sol?", ["5800 K", "8000 K", "12000 K"], 0),
    Question("O que é um pulsar?", ["Uma estrela que emite pulsos regulares de radiação", "Um planeta com atmosfera pulsante", "Uma região de poeira no espaço"], 0)
]

# Inicializar o Pygame
pygame.init()

# Criar a janela
screen = pygame.display.set_mode((800, 700))

# Iniciar o contador de pontos
score = 0
erros = 0

# Definir as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir a fonte
font = pygame.font.Font(None, 36)

# Definir a posição y das opções de resposta
option_y = 150

# Loop principal do jogo
current_question_index = 0
current_question = questions[current_question_index]
score = 0
answered = False  # Flag para verificar se uma opção foi selecionada

while True:
    screen.fill(BLACK)

    # Exibir a pergunta na tela
    question_text_surface = font.render(current_question.question_text, True, WHITE)
    screen.blit(question_text_surface, (50, 50))

    # Exibir as opções de resposta na tela
    option_y = 150
    for option_text in current_question.options:
        option_text_surface = font.render(option_text, True, WHITE)
        screen.blit(option_text_surface, (50, option_y))
        option_y += 50

    # Exibir a pontuação atual na tela
    score_text_surface = font.render("Acertos: " + str(score), True, WHITE)
    screen.blit(score_text_surface, (600, 15))
    erros_text_surface = font.render("Erros: " + str(erros), True, WHITE)
    screen.blit(erros_text_surface, (500, 15))

    pygame.display.flip()

    # Esperar pela entrada do usuário
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        # Verificar se a resposta está correta
        mouse_pos = pygame.mouse.get_pos()
        option_index = (mouse_pos[1] - 150) // 50

        if 0 <= option_index < len(current_question.options):
            answered = True

            if option_index == current_question.correct_answer:
                score += 1
            else:
                erros += 1

        # Se ainda houver perguntas, exibir a próxima pergunta
        if answered:
            answered = False  # Reiniciar a flag de resposta
            current_question_index += 1
            if current_question_index < len(questions):
                current_question = questions[current_question_index]

    # Se não houver mais perguntas, exibir a pontuação final
    if current_question_index == len(questions):
        screen.fill(BLACK)
        final_score_text_surface = font.render("A sua pontuação final é de " + str(score) + " acertos de 15 perguntas.", True, WHITE)
        screen.blit(final_score_text_surface, (75, 200))
        if score >= 7:
            texto_text_surface = font.render("Parabéns!", True, WHITE)
            screen.blit(texto_text_surface, (75, 300))
        else:
            texto1_text_surface = font.render("Estude mais!", True, WHITE)
            screen.blit(texto1_text_surface, (75, 300))
        pygame.display.flip()
        pygame.time.wait(9000)
        pygame.quit()
        sys.exit()


    pygame.display.flip()
