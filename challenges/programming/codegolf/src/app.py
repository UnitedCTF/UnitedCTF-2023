import io
import sys
import signal
import threading

TIMEOUT = 60 * 5

allowed = {
    "__builtins__": {
        "abs": abs,
        "print": print,
        "range": range,
        "len": len,
        "set": set,
        "map": map,
        "str": str,
        "list": list,
        "Array": ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"],
        "N": 2,
        "Words": ["radar", "kayak", "voiture", "rotor", "table"],
        "toWords": ["toto", "tomate", "romarin"],
        "MultiArray": ["a", "a", "b", "c", "c"]
    }
}

def print_menu():
    texte = [
        "========== Menu ==========",
        "Voici la liste des exercices:",
        "1 - Dictionaire",
        "2 - Conditions",
        "3 - Listes",
        "4 - Tableaux",
        "5 - Standardisation",
        "6 - Unicité",
        "7 Pour quitter"
    ]

    while True:
        for ligne in texte:
            print(ligne)

        choix = input("Entre le numéro de l'exercice que tu souhaites faire :")
        if choix.isdigit():
            nombre = int(choix)
            if 1 <= nombre <= 7:
                break

        print("Erreur : Veuillez entrer un nombre entre 1 et 7.")
    if nombre != 7:
        print("Vous avez choisi l'exercice", texte[nombre + 1], ": ")
    return nombre


def ask_to_restart():
    while True:
        response = input("Voulez-vous recommencer ? (Y/N) ")
        if response.upper() == "Y":
            return True
        elif response.upper() == "N":
            return False
        else:
            print("Réponse invalide. Veuillez répondre avec Y pour oui ou N pour non.")


def display_statement(data):
    print("*", "=" * 30, "*")
    print(" " * 10, data["title"], " " * 10)
    print("*", "=" * 30, "*")
    print("Consigne :", data["statement"])
    print("Limite de caractères :", data["limit"])
    print("Code d'exemple :")
    print(data["example"])
    print("\nEntre ta réponse ci-dessous :")


def get_response():
    contents = []
    while True:
        try:
            line = input()
            if line == "":
                break
        except EOFError:
            break
        contents.append(line)
    return "\n".join(contents)


def eval_response(code):
    output = io.StringIO()
    sys.stdout = output
    exec(code, allowed)
    printed_output = output.getvalue()
    sys.stdout = sys.__stdout__
    return printed_output

def display_and_eval_stmt(title: str, statement: str, limit: int, example: str,code_test:str, expected_output: str, flag: str) -> None:
    while True:
        display_statement({
            "title": title,
            "statement": statement,
            "limit": limit,
            "example": example
        })

        resp = get_response()
        if len(resp) <= limit:
            codetotest = code_test + resp
            output = eval_response(codetotest)
            print(output)
            if output.rstrip().strip() == expected_output:
                print(f"Bravo !!! Tu as réussi , moussaillon ! Voici ta récompense {flag}")
                return
            else:
                print("Dommage ton code est asse court mais il ne remplie pas sa mission à la perfection.")
                if not ask_to_restart():
                    return
        else:
            print("La réponse dépasse la limite de caractère autorisé.", 'red')
            if not ask_to_restart():
                return

def exo_un():
    title = "Dictionnaire"
    stmt = "Afficher les 7 premiers éléments d'une liste de chaînes de caractères nommée \"Array\" sous forme d'une chaîne de caractères en séparant chaque élément par un espace."
    limit = 22
    example = """print(Array[0] + " " + Array[1] + " " + Array[2] + " " + Array[3] + " " + Array[4] + " " + Array[5] + " " + Array[6])"""
    expected_output = "Lundi Mardi Mercredi Jeudi Vendredi Samedi Dimanche"
    flag = "flag-dico-run-0193747315584"

    display_and_eval_stmt(title, stmt, limit, example,"", expected_output, flag)


def exo_deux():
    title = "Conditions"
    stmt = "Afficher une chaîne de caractères qui suit le format suivant : \"x : Paire\" ou \"x : Impaire\" en remplaçant x par le numéro passé en paramètre nommé \"N\"."
    limit = 42
    example = """
print(N, end=" : ")
if N % 2 == 0: 
    print("Paire")
else:
    print("Impaire")
"""
    code_test = """for N in range(10):\n\t"""
    expected_output = "0 : Paire\n1 : Impaire\n2 : Paire\n3 : Impaire\n4 : Paire\n5 : Impaire\n6 : Paire\n7 : Impaire\n8 : Paire\n9 : Impaire"
    flag = "flag-condition-799614805872988"

    display_and_eval_stmt(title, stmt, limit, example,code_test, expected_output, flag)

def exo_trois():
    title = "Listes"
    stmt = "Afficher dans une chaîne de caractères la table de multiplication d'un nombre N donné en paramètre. La fonction doit afficher du multiplicateur 0 au multiplicateur 10 (inclus)."
    limit = 41
    example = """
Table = []
Table.append(0 * N)
Table.append(1 * N)
Table.append(2 * N)
Table.append(3 * N)
Table.append(4 * N)
Table.append(5 * N)
Table.append(6 * N)
Table.append(7 * N)
Table.append(8 * N)
Table.append(9 * N)
Table.append(10 * N)
print(" ".join(map(str, Table)))
"""
    expected_output = "0 2 4 6 8 10 12 14 16 18 20"
    flag = "flag-comprehension-list-97421365486525"

    display_and_eval_stmt(title, stmt, limit, example,"", expected_output, flag)



def exo_quatre():
    title = "Tableaux"
    stmt = "Afficher \"true\" ou \"false\" selon si le mot \"Word\" donné en paramètre est un palindrome."
    limit = 43
    example = """
reversed_string = ""
for i in range(len(Word)-1, -1, -1):
    reversed_string += Word[i]
print("true" if Word == reversed_string else "false")
"""
    code_test = """for Word in Words:\n\t"""
    expected_output = "true\ntrue\nfalse\ntrue\nfalse"
    flag = "flag-reverse-array-984233315633063"

    display_and_eval_stmt(title, stmt, limit, example, code_test, expected_output, flag)



def exo_cinq():
    title = "Standardisation"
    stmt = "Afficher le nombre d'apparitions de la chaîne de caractères \"to\" dans le mot \"Word\" passé en paramètre."
    limit = 23
    example = """
count = 0
i = 0
while i < len(Word):
    if Word[i:i+len("to")] == "to":
        count += 1
        i += len("to")
    else:
        i += 1
print(count)
"""
    code_test = """for Word in toWords:\n\t"""
    expected_output = "2\n1\n0"
    flag = "flag-func-standard-3348912236750"

    display_and_eval_stmt(title, stmt, limit, example, code_test, expected_output, flag)



def exo_six():
    title = "Unicité"
    stmt = "Afficher tous les éléments du tableau \"MultiArray\" une seule fois. Les éléments dupliqués ne doivent pas être réaffichés."
    limit = 29
    example = """
result = []
for element in MultiArray:
    if element not in result:
        result.append(element)
        print(element)
"""
    expected_output = "a\nb\nc"  # The expected output may vary based on the order
    flag = "flag-set-unique-712980012765345"

    display_and_eval_stmt(title, stmt, limit, example,"", expected_output, flag)



def print_header():
    print("*", "=" * 30, "*")
    print("Bienvenue dans l'épreuve Pacific-Golfing moussaillon !")
    print("Pour chaque exercice à venir, tu vas devoir écrire un")
    print("code qui a le même résultat que le code d'exemple, mais")
    print("en utilisant le moins de caractères possible. Pour envoyer")
    print("tes réponses, tu dois envoyer une ligne vide afin de signaler")
    print("au programme que ton code est terminé.")

def main():
    exercises = {
        1: exo_un,
        2: exo_deux,
        3: exo_trois,
        4: exo_quatre,
        5: exo_cinq,
        6: exo_six
    }

    print_header()
    while True:
        exo = print_menu()

        if exo == 7:
            print("Merci pour ton aide moussaillon ! Hâte de te revoir !")
            break
        elif exo in exercises:
            exercises[exo]()
            print("Retour au menu...")
        else:
            print("Numéro d'exercice invalide. Réessaie !")

def timeout_handler(signum, frame):
    print("Trop lent !")
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(TIMEOUT)
    main()
