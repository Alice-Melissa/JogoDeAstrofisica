isPressingW = False
# para saber se o jogador apertou apertou uma tecla
elif event.type == pygame.KEYDOWN:  # apertar a tecla
if event.key == pygame.K_w:
    isPressingW = True
    print("Apertou!")
elif event.type == pygame.KEYUP:  # soltar a tecla
    if event.key == pygame.K_w:
        isPressingW = False
        print("Soltou!")

if keys[pygame.D_RIGHT]:
    x-= velocidade
elif keys[pygame.E_LEFT]:
    x += velocidade

elif keys[pygame.D_RIGHT]:
    x2 += velocidade
elif keys[pygame.E_LEFT]:
    x2 -= velocidade
elif keys[pygame.W_UP]:
    y2 += velocidade
elif keys[pygame.S_DOWN]:
    y2 -= velocidade