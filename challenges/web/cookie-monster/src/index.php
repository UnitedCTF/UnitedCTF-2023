<?php

$default_role = 'nautae';
$role = isset($_COOKIE['role']) ? $_COOKIE['role'] : $default_role;

$want_role = array('coquere', 'coquus');

if (!in_array($role, $want_role)) {
    $role = $default_role;
}

setcookie('role', $role, time() + (86400 * 30), '/');
?>

<!DOCTYPE html>
<html>
<head>
    <title>Cookie monster</title>

    <style>
        html { background: azure; }

        body {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .flex {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        img { max-width: 300px; }
    </style>
</head>
<body>
    <div class='flex'>
        <h1><?php echo $role; ?></h1>

        <img src='./cookie_monster.png' alt='cookie monster'/>

        <?php 
        if ($role !== $default_role) {
            echo '<span>synt-P0000bBbxXXxxv111vvvr3rr3rrr</span>';
        } else {
            echo '<img src="https://media.tenor.com/hPBD2uEb0x8AAAAC/cry-sad.gif" />';
        }?>
    </div>

    <script>
        document.addEventListener('copy', function(e) {
            e.preventDefault();
            document.cookie = "role=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            location.reload();
        });
    </script>
</body>
</html>

