var needle = require("needle");
var os = require("os");
var fs = require("fs");
var digitalOceanClient = require("./digitalOceanClient.js").digitalOceanClient;




//Comment out when completed. ONLY RUN ONCE!!!!!
//Write down/copy droplet id.

var name = "dtmoore3"+os.hostname();
var region = "nyc2";
var image = "docker";
var size = "4gb"; 


digitalOceanClient.createDroplet(name, region, image, size, function(err, resp, body) {
    console.log(body);
    // StatusCode 202 - Means server accepted request.
    if(!err && resp.statusCode == 202) {
        console.log( JSON.stringify( body, null, 4 ) );
        var createdDroplet = body.droplet;
        fs.writeFile("./droplet.json", JSON.stringify( body, null, 3 ), function(err) {
            if(err) {
                console.log("Error writing file: " + err);
            }

            console.log("File saved!");
        })
    }
});

