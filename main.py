from print_color import *

def presentation():
    print_slow(color("Bonjour...", "\033[32m"))
    print_slow(color("Quel est votre nom ?", "\033[32m"))
    name = input(color("Votre nom : ", "\033[32m"))
    print_slow(color("Bienvenue", "\033[32m")+color(f" {name}", "\033[31m")+color(" !", "\033[32m"))
    return name

def menu(name):
    a = input("\033[32m" + f'''
Que voulez vous faire {name}?
[1] Lancer le quiz?
[2] Quitter
Votre choix :''' + "\033[0m")

    if a == '1': quizz(name)
    elif a == '2': exit()
    else: 
        print("\033[31m" + "Votre choix n'est pas valide !" + "\033[0m")
        menu(name)

def quizz(name):
    print("_________________________________________")
    print()
    print_slow(color("\nBienvenue dans le quiz!", "\033[32m"))
    print_slow(color(f"\nBonne chance {name}!", "\033[32m"))

    with open("questions.txt", "r") as f:
        questions = f.readlines()

    for i in range(len(questions)):
        questions[i] = questions[i].strip().split("|")

    num = 1
    for question,answer in questions:
        print("_________________________________________")
        print()

        while True:
            print_slow(f"\033[34m" + f"Question {num} : " + "\033[0m")
            print_green(question)
            u_input = input(color("Votre réponse :", "\033[32m"))

            if u_input.lower() == answer.lower():
                print_slow("\033[32m" + "Bonne réponse! ✅" + "\033[0m")
                break
            else:
                print_slow("\033[31m" + "Mauvaise réponse! ❌" + "\033[0m")
                print(f"\033[31m" + """
    ███████╗ █████╗ ██╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗███████╗    ███████╗████████╗███████╗███████╗    ██████╗ ███████╗████████╗███████╗███████╗
    ██╔════╝██╔══██╗██║   ██║╚██╗██╔╝    ██║   ██║██╔═══██╗██║   ██║██╔════╝    ██╔════╝╚══██╔══╝██╔════╝██╔════╝    ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝
    █████╗  ███████║██║   ██║ ╚███╔╝     ██║   ██║██║   ██║██║   ██║███████╗    █████╗     ██║   █████╗  ███████╗    ██████╔╝█████╗     ██║   █████╗  ███████╗
    ██╔══╝  ██╔══██║██║   ██║ ██╔██╗     ╚██╗ ██╔╝██║   ██║██║   ██║╚════██║    ██╔══╝     ██║   ██╔══╝  ╚════██║    ██╔══██╗██╔══╝     ██║   ██╔══╝  ╚════██║
    ██║     ██║  ██║╚██████╔╝██╔╝ ██╗     ╚████╔╝ ╚██████╔╝╚██████╔╝███████║    ███████╗   ██║   ███████╗███████║    ██████╔╝███████╗   ██║   ███████╗███████║
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝      ╚═══╝   ╚═════╝  ╚═════╝ ╚══════╝    ╚══════╝   ╚═╝   ╚══════╝╚══════╝    ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚══════╝                                                                                                                                          
    """ + "\033[0m")
                print_slow("\033[31m" + "Il faudra réessayer!" + "\033[0m")
                print()

        num += 1

    #pour arriver ici toute les reponses doivent être correctes
    print()
    print_slow("\033[32m" + "🎉 Bravo! 🎉" + "\033[0m")
    print_slow("\033[32m" + "Vous avez réussi le quiz!" + "\033[0m")
    print_slow("\033[32m" + "La suite du jeu se déroulle à..." + "\033[0m")
    print_slow("\033[32m" + "..." + "\033[0m")
    print_slow("\033[32m" + "..." + "\033[0m")

    print_purple("""
██████   ██████  ██    ██ ██ ██      ██       ██████  ███    ██ 
██   ██ ██    ██ ██    ██ ██ ██      ██      ██    ██ ████   ██ 
██████  ██    ██ ██    ██ ██ ██      ██      ██    ██ ██ ██  ██ 
██   ██ ██    ██ ██    ██ ██ ██      ██      ██    ██ ██  ██ ██ 
██████   ██████   ██████  ██ ███████ ███████  ██████  ██   ████                                                            
""")

    exit()
    

if __name__ == "__main__":
    name = presentation()
    menu(name)