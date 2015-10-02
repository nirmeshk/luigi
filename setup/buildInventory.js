var digitalOceanClient = require("./digitalOceanClient.js").digitalOceanClient;
var fs = require("fs");

var hostsPath = "./hosts";
try {
    console.log("Deleting existing 'hosts' file.")
    fs.unlinkSync(hostsPath);
} 
catch (e) {
    console.log("No 'hosts' file exists.");
}

var droplet = JSON.parse(fs.readFileSync("droplet.json", "utf8")).droplet;

digitalOceanClient.getDroplet(droplet.id, function(error, response) {
    var data = response.body;

    if( data.droplet ) {
        var dropletHost = "[droplet]\n" + data.droplet.networks.v4[0].ip_address + " ansible_ssh_user=root\n\n";
        fs.appendFile(hostsPath, dropletHost, function(err) {
            if(err) {
                console.log("Error saving droplet ip to file, err: " + err);
            }

            console.log("Appended digital ocean host");
        });
    }
});