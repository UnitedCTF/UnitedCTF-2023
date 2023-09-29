<?php

$servername = "localhost";
$username = "wellerman";
$password = "FLAG-ThereOnceWasAShipThatPutToSea";
$dbname = "boatdb";

$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) die("Connection failed: " . mysqli_connect_error());

$id = $_GET["id"];
if ($id == null) {
    $id = 1;
}

$sql = "SELECT name, nickname FROM crew WHERE id = " . $id;
$result = mysqli_query($conn, $sql);

$row = mysqli_fetch_assoc($result);
$name = $row["name"];
$nickname = $row["nickname"];

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
                <li><a href="captain.php">Capitaine</a></li>
                <li><a href="crew.php" class="current">Équipage</a></li>
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
            <figure>
                <img style="height: 400px;" src="/img/<?php echo $name; ?>.png" />
                <figcaption><?php echo $name; ?>, A.K.A. <?php echo $nickname; ?></figcaption>
            </figure>
            <div>
<?php if ($id > 1) { ?>
                <a class="button" href="crew.php?id=<?php echo $id-1; ?>">⬅</a>
<?php } if ($id < 5) { ?>
                <a class="button" href="crew.php?id=<?php echo $id+1; ?>">⮕</a>
<?php } ?>
            </div>
        </article>
    </main>
    <footer>
        <p>B.O.A.T. (c) 2023</p>
    </footer>
    <script src="dark.js"></script>
    </body>
</html>