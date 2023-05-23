import pygame
import sys
from Questoes import Question

pygame.init()

screen = pygame.display.set_mode((900, 700))
questions = [
            Question("Qual é a estrela mais próxima da Terra?", ["Alfa Centauri", "Sirius", "Vega"], 0),
            Question("Qual é o planeta mais denso do sistema solar?", ["Terra", "Vênus", "Marte"], 0),
            Question("O que é um buraco negro?",
                     ["Uma estrela morta", "Um objeto cósmico que engole tudo", "Um tipo de galáxia"], 1),
            Question("Qual é o nome da teoria que descreve a expansão do universo?", ["Teoria da relatividade", "Teoria do Big Bang", "Teoria das cordas"], 1),
            Question("Quantas luas tem o planeta Saturno?", ["9", "27", "62"], 1),
            Question("Qual é o tipo mais comum de estrela na Via Láctea?", ["Anã vermelha", "Gigante vermelha", "Estrela de nêutrons"], 0),
            Question("O que é uma supernova?", ["Um buraco negro em formação", "A explosão de uma estrela", "Uma chuva de meteoros"], 1),
            Question("Qual é o nome da galáxia mais próxima da nossa?", ["Via Láctea", "Andrômeda", "Triângulo"], 1),
            Question("Defina gravitação:", ["É o respectivo ângulo (a partir da reta N) no qual um feixe de luz provém de uma face espelhada", "É o ponto em que um raio de luz toca uma superficie", "Fenômeno que causa a distorção da luz em torno de objetos com grande massa"], 2),
            Question("O que é um pulsar?", ["Uma estrela que emite pulsos regulares de radiação", "Um planeta com atmosfera pulsante", "Uma região de poeira no espaço"], 0),
            Question("Qual é a temperatura média do Sol?", ["5800 K", "8000 K", "12000 K"], 0),
            Question("Qual é a unidade de medida usada para medir as distâncias no universo?", ["Ano-luz", "Kilômetro", "Metro"], 0),
            Question("O que é a matéria escura?", ["Matéria que não emite luz", "Matéria que absorve a luz", "Matéria que reflete a luz"], 0),
            Question("O que é a radiação cósmica de fundo?", ["Radiação emitida pelo Sol", "Radiação emitida pela Terra", "Radiação emitida pela explosão do Big Bang"], 2),
            Question("Qual é o nome da nave da NASA que realizou a primeira missão tripulada à Lua?", ["Apollo 11", "Apollo 13", "Apollo 17"], 0)
]
current_question_index = 0
current_question = questions[current_question_index]
index = 0
clock = pygame.time.Clock()

# Exibir a pergunta na tela
font = pygame.font.Font(None, 36)
question_text_surface = font.render(current_question.question_text, True, (255, 255, 255))
screen.blit(question_text_surface, (50, 100))
score = 0
score_text_surface = font.render("Pontuação: " + str(score), True, (255, 255, 255))
screen.blit(score_text_surface, (735, 50))

# Exibir as opções de resposta na tela
option_y = 250
for option_text in current_question.options:
    option_text_surface = font.render(option_text, True, (255, 255, 255))
    screen.blit(option_text_surface, (50, option_y))
    option_y += 50

pygame.display.flip()

while True:
    clock.tick(60)
    # Esperar pela entrada do usuário
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        # Verificar se a resposta está correta
        mouse_pos = pygame.mouse.get_pos()

        option_index = (mouse_pos[1] - 150) // 50
        if option_index == current_question.correct_answer:
            print("Resposta correta!")
            score += 1
        else:
            print("Resposta incorreta!")
            score -= 1

        screen.fill((0, 0, 0))
        score_text_surface = font.render("Pontuação: " + str(score), True, (255, 255, 255))
        screen.blit(score_text_surface, (735, 50))

        # Passar para a próxima pergunta
        current_question_index += 1
        if current_question_index < len(questions):
            current_question = questions[current_question_index]

            # Exibir a pergunta na tela
            question_text_surface = font.render(current_question.question_text, True, (255, 255, 255))
            screen.blit(question_text_surface, (50, 100))

            # Exibir as opções de resposta na tela
            option_y = 250
            for option_text in current_question.options:
                option_text_surface = font.render(option_text, True, (255, 255, 255))
                screen.blit(option_text_surface, (50, option_y))
                option_y += 50

            pygame.display.flip()

            # Se não houver mais perguntas, exibir a pontuação final
        else:
            final_score_text_surface = font.render("Pontuação final: " + str(score), True, (255, 255, 255))
            screen.blit(final_score_text_surface, (735, 50))
            pygame.display.flip()
            pygame.time.wait(5000)
            pygame.quit()
            sys.exit()


        pygame.display.flip()
