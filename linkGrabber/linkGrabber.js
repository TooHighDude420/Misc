var linkList = [];

linkList = document.querySelectorAll("img");

var linkString = "";

for (var i = 0; i < linkList.length; i++) {
    if (linkList[i].src.includes("jpg")) {
        var cut = linkList[i].src.split("?");
        linkString += "\n" + cut[0];
    }
}

console.log(linkString);