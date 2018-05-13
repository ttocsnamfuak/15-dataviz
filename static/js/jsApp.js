
var globalResponse;
console.log("RUnning the JS");

function loadOption(){
    console.log("Build Options");
    var select = document.getElementById("selDataset");
    for(var i = 0; i < globalResponse.length; i++) {
        var opt = globalResponse[i];
        var el = document.createElement("option");
        el.textContent = opt;
        el.value = opt;
        select.appendChild(el);
    }​    
}


function buildButton() {
    /* data route */
    var url = "/names";
    Plotly.d3.json(url, function (error, response) {
        if (error) throw error;
        console.log(response);
        var data = response;
        globalResponse = response;
    })
    loadOption();
    // var select = document.getElementById("selDataset");
    // for(var i = 0; i < globalResponse.length; i++) {
    //     var opt = globalResponse[i];
    //     var el = document.createElement("option");
    //     el.textContent = opt;
    //     el.value = opt;
    //     select.appendChild(el);
    // }​      
}





buildButton();


// var select = document.getElementById("selDataset");
// for(var i = 0; i < globalResponse.length; i++) {
//         var opt = globalResponse[i];
//         var el = document.createElement("option");
//         el.textContent = opt;
//         el.value = opt;
//         select.appendChild(el);
//     }


// function renderButton() {
//     tbody.innerHTML = "";
//     for (var i = 0; i < filteredAddresses.length; i++) {
//       // Get get the current address object and its fields
//       var address = filteredAddresses[i];
//       var fields = Object.keys(address);
//       // Create a new row in the tbody, set the index to be i + startingIndex
//       var row = tbody.insertRow(i);
//       for (var j = 0; j < fields.length; j++) {
//         // For every field in the address object, create a new cell at set its inner text to be the current value at the current address's field
//         var field = fields[j];
//         var cell = row.insertCell(j);
//         cell.innerText = address[field];
//       }
//     }
//   }
// var select = document.getElementById("selectNumber"); 
// var options = ["1", "2", "3", "4", "5"]; 

// for(var i = 0; i < options.length; i++) {
//     var opt = options[i];
//     var el = document.createElement("option");
//     el.textContent = opt;
//     el.value = opt;
//     select.appendChild(el);
// }​