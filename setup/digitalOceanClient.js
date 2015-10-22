var needle = require("needle");
var fs = require("fs");
var config = JSON.parse(fs.readFileSync("digitalOceanConfig.json", "utf8"));

var headers =
{
    'Content-Type':'application/json',
    'Authorization': 'Bearer ' + config.token
};

exports.digitalOceanClient =
{
    listRegions: function( onResponse )
    {
        needle.get("https://api.digitalocean.com/v2/regions", {headers:headers}, onResponse)
    },

    createDroplet: function (dropletName, region, imageName, size, onResponse)
    {
        var data = 
        {
            "name": dropletName,
            "region":region,
            "size":size,
            "image":imageName,
            "ssh_keys":[1498061, 1503305, 1503299],
            "backups":false,
            "ipv6":false,
            "user_data":null,
            "private_networking":null
        };

        console.log("Attempting to create: "+ JSON.stringify(data) );

        needle.post("https://api.digitalocean.com/v2/droplets", data, {headers:headers,json:true}, onResponse );
    },

    listImages: function ( onResponse )
    {
        needle.get("https://api.digitalocean.com/v2/images", {headers:headers}, onResponse);
    },

    getDroplet: function (dropletId, onResponse)
    {
        needle.get("https://api.digitalocean.com/v2/droplets/" + dropletId, {headers:headers}, onResponse);
    },

    deleteDroplet: function (dropletId, onResponse)
    {
        needle.delete("https://api.digitalocean.com/v2/droplets/" + dropletId, null, {headers:headers}, onResponse);
    }
};