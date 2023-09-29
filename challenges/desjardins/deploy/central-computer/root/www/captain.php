<?php

$servername = "localhost";
$username = "wellerman";
$password = "FLAG-ThereOnceWasAShipThatPutToSea";
$dbname = "boatdb";

$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) die("Connection failed: " . mysqli_connect_error());

$sql = "SELECT id, name, nickname FROM crew WHERE id = (SELECT id FROM roles WHERE role = 'Captain')";
$result = mysqli_query($conn, $sql);

$captain = mysqli_fetch_assoc($result);

mysqli_close($conn);

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
                <li><a href="index.php">Accueil</a></li>
                <li><a href="captain.php" class="current">Capitaine</a></li>
                <li><a href="crew.php">Équipage</a></li>
                <li><a href="meteo.php">Météo</a></li>
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
        <article style="text-align: center;">
            <img src="/img/<?php echo $captain["name"]; ?>.png" />
            <p>
                Notre capitaine est <?php echo $captain["name"]; ?>, mieux connu sous le nom de <?php echo $captain["nickname"]; ?> !
            </p>
        </article>
    </main>
    <footer>
        <p>B.O.A.T. (c) 2023</p>
    </footer>
    <script src="dark.js"></script>
</body>

</html>