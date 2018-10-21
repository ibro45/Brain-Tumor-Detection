var inputList = [];

function clearInput(){
	document.getElementById("uploadButton").value = "";
	while (document.getElementById("fileList").firstChild) {
    	document.getElementById("fileList").removeChild(document.getElementById("fileList").firstChild);
	}
}

function listFiles() {
  	var files = document.getElementById("uploadButton").files;
  	for (var i = 0; i < files.length; i++) {
      inputList.push(files[i].name);
  		var li = document.createElement('li');
  		var itemText = document.createTextNode(files[i].name);
    	li.appendChild(itemText);
    	document.getElementById("fileList").appendChild(li);
  	}
}