from Part import Part
from Ship import Ship
from RacingShip import RacingShip
import time
import tkinter as tk
import pygame

historique = []
info = 0

def menu(ship:Ship) : 
    running = True
    historique = []
    is_hist = False
    while running :
        if not is_hist :
            ship.display_state()
        choice = input("\np : Modifier une pièce du navire |h : Historique\nm : Modifier un matériau | q : Quitter  ")
        match choice :
            case "p" :
                part_name = input("Entrez le nom de la pièce à changer : ")
                new_part_name = input("Entrez le nom de la nouvelle pièce : ")
                new_material = input("Entrez le nom du matériau de la nouvelle pièce : ")
                ship.replace_part(part_name, Part(new_part_name, new_material))
                historique.append(f"Remplacement de {part_name} par {new_part_name} en {new_material}")
                is_hist = False
            case "m" : 
                part_name = input("Entrez le nom de la pièce à modifier : ")
                new_material = input("Entrez le nom du matériau de la nouvelle pièce : ")
                ship.change_part(part_name, new_material)
                historique.append(f"Changement de matériaux de {part_name} en {new_material}")
                is_hist = False

            case "h" :
                if historique == [] :
                    print("\nPas d'historique enregister")
                else :
                    for action in historique :
                        print(action)
                is_hist = True
            case "q" :
                running = False 
        time.sleep(1)

def list_color(ship:Ship) :
    colors = {}
    for part in ship.get_parts().values() :
        match part.material :
            case "bois" :
                colors[part.name] = "saddlebrown"
            case "ebene" :
                colors[part.name] = "black"
            case "bouleau" :
                colors[part.name] = "tan"
            case "pierre" :
                colors[part.name] = "grey"
    return colors


def display_ship(ship:Ship, canvas) :
    # Efface tout le contenu du canvas avant de redessiner
    canvas.delete("all")
    
    colors = list_color(ship)

    # Mer
    canvas.create_line(0, 450, 600, 450, width=200, fill='navy')
    canvas.create_arc(0, 340, 80, 360, start=0, extent=180, outline='navy', width=10)
    canvas.create_arc(70, 340, 150, 360, start=0, extent=180, outline='navy', width=10)
    canvas.create_arc(140, 340, 220, 360, start=0, extent=180, outline='navy', width=10)
    canvas.create_arc(210, 340, 290, 360, start=0, extent=180, outline='navy', width=10)
    canvas.create_arc(280, 340, 360, 360, start=0, extent=180, outline='navy', width=10)
    canvas.create_arc(350, 340, 430, 360, start=0, extent=180, outline='navy', width=10)
    canvas.create_arc(420, 340, 500, 360, start=0, extent=180, outline='navy', width=10)
    canvas.create_arc(490, 340, 570, 360, start=0, extent=180, outline='navy', width=10)
    canvas.create_arc(560, 340, 595, 360, start=0, extent=180, outline='navy', width=10)

    # Coque principale (grande)
    if "coque" in ship.get_parts() :
        canvas.create_polygon(150, 280, 450, 280, 420, 350, 180, 350, fill=colors["coque"], outline='black', width=2)

        # Hublots coque
        for i in range(8):
            canvas.create_oval(200 + i*30, 300, 210 + i*30, 310, fill='darkgoldenrod', outline='black')

    # Pont inférieur
    if "pont" in ship.get_parts() :
        canvas.create_rectangle(180, 250, 420, 280, fill=colors["pont"], outline='black', width=2)

    # cabine arrière
    if "cabine" in ship.get_parts() :
        canvas.create_rectangle(350, 220, 430, 250, fill=colors["cabine"], outline='black', width=2)
        canvas.create_rectangle(360, 190, 420, 220, fill=colors["cabine"], outline='black', width=2)
        canvas.create_rectangle(370, 160, 410, 190, fill=colors["cabine"], outline='black', width=2)

        # cabine avant
        canvas.create_rectangle(170, 230, 230, 250, fill=colors["cabine"], outline='black', width=2)

        # Hublots cabine arrière
        for i in range(3):
            canvas.create_oval(365 + i*20, 200, 375 + i*20, 210, fill='gold', outline='black')

    if "mat" in ship.get_parts() :
        # Mât arrière
        canvas.create_line(390, 220, 390, 100, width=4, fill=colors["mat"])
        canvas.create_polygon(390, 120, 440, 150, 390, 180, fill='ivory', outline='black')

        # Mât central
        canvas.create_line(300, 250, 300, 80, width=5, fill=colors["mat"])
        canvas.create_polygon(300, 100, 360, 140, 300, 180, fill='white', outline='black')
        canvas.create_polygon(300, 140, 350, 170, 300, 200, fill='white', outline='black')

        # Mât avant
        canvas.create_line(210, 240, 210, 120, width=4, fill=colors["mat"])
        canvas.create_polygon(210, 140, 260, 170, 210, 200, fill='ivory', outline='black')

        # Drapeaux
        canvas.create_polygon(390, 100, 390, 85, 410, 92, fill='red', outline='black')
        canvas.create_polygon(300, 80, 300, 60, 325, 70, fill='red', outline='black')

    if "proue" in ship.get_parts() :
        # proue
        canvas.create_line(180, 240, 120, 200, width=3, fill=colors["proue"])
        canvas.create_polygon(120, 200, 150, 215, 160, 230, fill='white', outline='black')

#met a jour le label d'info
def update_info_label(info_label):
    global historique
    if info == 0 :
        info_text = f"=== Historique des modifications ===\n\n"
        if historique:
            for i, action in enumerate(historique, 1):
                info_text += f"{i}. {action}\n"
        else:
            info_text += "Aucune modification effectuée"
        info_label.config(text=info_text)
    else :
        info_text = f"=== Etat du navire ===\n\n"
        info_text += ship.display_state()
        print(info_text)
        info_label.config(text=info_text)



def on_replace(ship, canvas, entry_part_name, entry_part_new_name, entry_material, info_label):
    global historique
    part_name = entry_part_name.get()
    new_name = entry_part_new_name.get()
    new_mat = entry_material.get()
    ship.replace_part(part_name, Part(new_name, new_mat))
    display_ship(ship, canvas)
    historique.append(f"Remplacement de {part_name} par {new_name} en {new_mat}")
    update_info_label(info_label)


def on_change(ship, canvas, entry_part_name, entry_material, info_label):
    global historique
    part_name = entry_part_name.get()
    new_mat = entry_material.get()
    ship.change_part(part_name, new_mat)
    display_ship(ship, canvas)
    historique.append(f"Changement de matériau de {part_name} en {new_mat}")
    update_info_label(info_label)

def change_info(info_label) :
    global info
    info += 1
    info = info % 2
    update_info_label(info_label)
    print(info)


def display_menu(ship, root, canvas):
    # Création d'un frame principal
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Frame de gauche pour les entrées et boutons
    left_frame = tk.Frame(main_frame, width=300)
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Frame de droite pour le label d'information
    right_frame = tk.Frame(main_frame, width=300)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # === Partie gauche : formulaire ===
    # Nom du Part cible
    label_part_name = tk.Label(left_frame, text="Pièce à modifier :")
    label_part_name.pack(anchor='w')
    entry_part_name = tk.Entry(left_frame)
    entry_part_name.pack(pady=5, fill=tk.X)
    
    # Nom du nouveau Part
    label_part_new_name = tk.Label(left_frame, text="Nouvelle pièce :")
    label_part_new_name.pack(anchor='w')
    entry_part_new_name = tk.Entry(left_frame)
    entry_part_new_name.pack(pady=5, fill=tk.X)
    
    # Materiau du nouveau Part
    label_material = tk.Label(left_frame, text="Nouveau matériau :")
    label_material.pack(anchor='w')
    entry_material = tk.Entry(left_frame)
    entry_material.pack(pady=5, fill=tk.X)
    
    # === Partie droite : label d'information ===
    info_label = tk.Label(right_frame, text="", justify=tk.LEFT, anchor='nw', 
                         relief=tk.SUNKEN, bg='white', padx=10, pady=10, font=('Arial', 10))
    info_label.pack(fill=tk.BOTH, expand=True)
    
    # Boutons avec les callbacks (utilisation de lambda pour passer les paramètres)
    btn_replace = tk.Button(left_frame, text="Remplacer une pièce", 
                           command=lambda: on_replace(ship, canvas, entry_part_name, entry_part_new_name, entry_material, info_label))
    btn_replace.pack(pady=5, fill=tk.X)
    
    btn_change = tk.Button(left_frame, text="Changer le materiau", 
                          command=lambda: on_change(ship, canvas, entry_part_name, entry_material, info_label))
    btn_change.pack(pady=5, fill=tk.X)

    btn_info = tk.Button(right_frame, text="Changer les infos", command=lambda: change_info(info_label))
    btn_info.pack(pady=5, fill=tk.X)
    
    # Affichage initial
    update_info_label(info_label)

pygame.mixer.init()
son = pygame.mixer.music.load("son.mp3")
pygame.mixer.music.play(-1)


list_parts = {
    "mat" : Part("mat", "bois"),
    "coque" :  Part("coque", "bois"),
    "cabine" : Part("cabine" , "bois"),
    "pont" : Part("pont", "bois"),
    "quille" : Part("quille", "bois"), 
    "proue" : Part("proue", "bois")
}


# Création du navire
ship = Ship("Santa Maria", list_parts)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Ship")

# Création du canvas (une seule fois)
canvas = tk.Canvas(root, width=600, height=500, bg='lightblue')
canvas.pack()

# Affichage initial du navire
display_ship(ship, canvas)

# Création du menu
display_menu(ship, root, canvas)

# Lancement de la boucle principale (une seule fois, à la fin)
root.mainloop()