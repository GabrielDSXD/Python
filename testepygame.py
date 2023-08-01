import pygame

#Inicializando o Pygame e criando a Janela
pygame.init()

display = pygame.display.set_mode([840, 480]) #Tamanho da janela
pygame.display.set_caption("Estruturas de dados") #Nome da janela

def draw():
    display.fill("white")


gameLoop = True

if __name__ == "__main__":
    while gameLoop:        
        draw() 
        pygame.display.update()