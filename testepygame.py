import pygame

#Inicializando o Pygame e criando a Janela
pygame.init()

print("Iniciando jogo...")

display = pygame.display.set_mode([840, 480]) #Tamanho da janela
pygame.display.set_caption("Estruturas de dados") #Nome da janela

def draw():
    display.fill("white")


gameLoop = True
isPressingW = False

if __name__ == "__main__": #Configuração de teclas de atalho
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    isPressingW = True
                    print("Tecla W pressionada")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    isPressingW = False
                    print("Tecla W soltada")

        draw() 
        pygame.display.update()

print("Fechando jogo...")