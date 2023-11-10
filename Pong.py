import turtle #Le module turtle permet d'avoir des graphismes de base 

#Pour notre pong on a besoin de cree une fenetre

wn = turtle.Screen()
wn.title("Pong by Oliver")
wn.bgcolor("black") #On veut que la couleur du background de la fenetre soit noire.
wn.setup(width=800, height=600) #On precise la taille de la fenetre
wn.tracer(0)

# Raquette 1
paddle_a = turtle.Turtle() #t pour le nom du module et T pour le nom de la classe
paddle_a.speed(0) #Ce n'est pas la vitesse de la raquette mais la rapidite de l'animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup() #pour enlever la trainer en ligne blanche par defaut de turtule lorsque l'element bouge
paddle_a.goto(-350, 0) #C'est l'emplacement de depart de notre raquette

# Raquette 2

# Balle

#Main game loop
while True:
    wn.update() #A chaque fois que la boucle s'active cela update la fenetre
    