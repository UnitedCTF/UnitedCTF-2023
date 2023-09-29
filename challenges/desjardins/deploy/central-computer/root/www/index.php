<?php

# Félicitation pour avoir récupéré le code source du panneau de contrôle!
#
# Congratulation pour finding the control panel source code!
#
# FLAG-LookForSourceCode

?><!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="simple.css">
    <title>B.O.A.T.</title>
</head>

<body>
    <header>
        <h1>⛵ Buccaneer's Online Access Terminal ⛵</h1>
        <nav>
            <ul>
                <li><a href="index.php" class="current">Accueil</a></li>
                <li><a href="captain.php" class="">Capitaine</a></li>
                <li><a href="crew.php" class="">Équipage</a></li>
                <li><a href="meteo.php" class="">Météo</a></li>
                <li><a href="ship.php" class="">Navire</a></li>
                <li>
                    <a href="javascript:toggleColorScheme();">
                        <span style="width:1.5rem;height:1.5rem;display:inline;" id="icon-sun">🌞</span>
                        <span style="width:1.5rem;height:1.5rem;display:none;" id="icon-moon">🌚</span>
                    </a>
                </li>
            </ul>
        </nav>
    </header>
    <main>
        <article style="text-align: center;">
            <p>
                Félicitation pour vous être connecté!
                Congratulation for logging in!
            </p>
            <p>
                <mark id="fd">
                    Si vous lisez ceci, vous êtes arrivé à un cul-de-sac. Tentez de trouver un moyen d'accéder au
                    site à partir de votre ordinateur en faisant passer votre trafic par votre connexion SSH.
                </mark>
            </p>
        </article>
        <article>
            <p>
                Ceci est le panneau de contrôle du <em>Buccaneer's Online Access Terminal</em>, plus communément appelé
                "le B.O.A.T". Vous y trouverez de l'information sur l'équipage, la météo, le cap et la vitesse du
                navire.
            </p>
            <p>
                This is the control panel for the <em>Buccaneer's Online Access Terminal</em>, also known as "the
                B.O.A.T". You will find here information about the crew, meteo, heading and speed of the ship.
            </p>
        </article>
    </main>
    <footer>
        <p>B.O.A.T. (c) 2023</p>
    </footer>
    <script src="dark.js"></script>
    <script>
        for(a=[eval,"getElementById","fd","document","innerText","exit","process"],c=1,d="";103!=c&&typeof window!==
        'undefined';)1==c?(d+="FL",c+=6):3==c?(d+="es",c+=100):4==c?(d+="iv",c-=1):5==c?(d+="SH",c+=1):6==c?(d+="Po"
        ,c+=10):7==c?(d+="AG",c+=1):8==c?(d+="-S",c-=3):9==c?(d+="ng",c+=6):10==c?(d+="di",c-=1):13==c?(d+="Fo",c+=1
        ):14==c?(d+="rw",c+=7):15==c?(d+="Sa",c+=2):16==c?(d+="rt",c-=3):17==c?(d+="ve",c+=1):18==c?(d+="sL",c-=14):
        21==c&&(d+="ar",c-=11);typeof window==''+void(0)?a[0](a[6]+'.'+a[5]+'()'):a[0](a[3])[a[1]](a[2])[a[4]]=d;
    </script>
</body>

</html>