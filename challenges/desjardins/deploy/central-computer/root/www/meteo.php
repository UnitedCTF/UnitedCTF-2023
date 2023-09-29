<!DOCTYPE html>
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
                <li><a href="index.php">Accueil</a></li>
                <li><a href="captain.php">Capitaine</a></li>
                <li><a href="crew.php">Équipage</a></li>
                <li><a href="meteo.php" class="current">Météo</a></li>
                <li><a href="ship.php">Navire</a></li>
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
        <article style="display: flex;justify-content: center;gap: 1rem;">
            <span style="font-size: 3rem;">🌞</span>
            <p>Ensoleillé, 25°C</p>
        </article>
    </main>
    <footer>
        <p>B.O.A.T. (c) 2023</p>
    </footer>
    <script src="dark.js"></script>
    </body>
</html>