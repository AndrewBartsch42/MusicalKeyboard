import pygame # https://www.pygame.org/news
import winsound
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
previousKey = None # used to track the previous key that is pressed in order to change inital note
bTime = 100 # used to universally control how long the beep time is for 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                previousKey = "q"
                #print("Q was pressed") #used to test for correct handling of inputs
                #print(previousKey) #used to test for correct handling of inputs
            elif event.key == pygame.K_w:
                previousKey = "w"
                #print("W was pressed") #used to test for correct handling of inputs
            elif event.key == pygame.K_e:
                previousKey = "e"
                #print("E was pressed") #used to test for correct handling of inputs
            elif event.key == pygame.K_r:
                previousKey = "r"
                #print("R was pressed") #used to test for correct handling of inputs

            elif event.key == pygame.K_u:
                #print("u was pressed") #used to test for correct handling of inputs
                if previousKey == "q":
                    #print("g string time") #used to test for correct handling of inputs
                    winsound.Beep(196, bTime)
                elif previousKey == "w":
                    winsound.Beep(293, bTime)
                elif previousKey == "e":
                    winsound.Beep(440, bTime)
                elif previousKey == "r":
                    winsound.Beep(659, bTime)
            elif event.key == pygame.K_i:
                #print("i was pressed") #used to test for correct handling of inputs
                if previousKey == "q":
                    winsound.Beep(220, bTime)
                elif previousKey == "w":
                    winsound.Beep(329, bTime)
                elif previousKey == "e":
                    winsound.Beep(493, bTime)
                elif previousKey == "r":
                    winsound.Beep(698, bTime)
            elif event.key == pygame.K_o:
                #print("o was pressed") #used to test for correct handling of inputs
                if previousKey == "q":
                    winsound.Beep(246, bTime)
                elif previousKey == "w":
                    winsound.Beep(349, bTime)
                elif previousKey == "e":
                    winsound.Beep(523, bTime)
                elif previousKey == "r":
                    winsound.Beep(784, bTime)
            elif event.key == pygame.K_p:
                #print("p was pressed") #used to test for correct handling of inputs
                if previousKey == "q":
                    winsound.Beep(261, bTime)
                elif previousKey == "w":
                    winsound.Beep(392, bTime)
                elif previousKey == "e":
                    winsound.Beep(587, bTime)
                elif previousKey == "r":
                    winsound.Beep(880, bTime)
                
pygame.quit()