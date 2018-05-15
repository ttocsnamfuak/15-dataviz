
var globalResponse;
var globalButton
console.log("RUnning the JS");

function buildButton() {
    /* data route */
    console.log("RUnning BuildButton");
    var url = "/names";
    Plotly.d3.json(url, function (error, response) {
        if (error) throw error;
        // console.log(response);
        var data = response;
        // console.log(data);
        globalButton = response;
        var buttonLen = response.length;
        // console.log("Button Length: " + buttonLen);
        var select = document.getElementById("selDataset");
        for ( var index = 0; index < response.length; index++){
            // console.log("in the for");
            // console.log(index);
            var opt = response[index];
            // console.log(response[index]);
            var el = document.createElement("option");
            el.textContent = opt;
            el.value = opt;
            select.appendChild(el);
        }
        init(response[0]);
    })  
}


//Build the initial tables to display and the selections
function init(data) {
    console.log("RUnning init");
    //Call the route to retrieve the data for pie chart
    var belly = data;
    var url = "/samples/" + belly;
    console.log(url);
    Plotly.d3.json(url, function (error, response) {
        if (error) throw error;
        console.log("The returned data " + response);
        console.log(response);
        console.log("Just the otu ID's " + response.otu_ids);
        var data = response;
        globalResponse = response;
        var data = [{
            values: globalResponse[0].sample_values, //sample_values
            labels: globalResponse[0].otu_ids, //otu_ids
            type: "pie"
          }]; 
          console.log(data);
          var layout = {
            height: 600,
            width: 800
          };
          var PIE = document.getElementById("pie");
          Plotly.plot(PIE, data, layout);
    })
    //build the data for the chart
  
    // globalResponse.forEach(function (data) {
    //     data.sample_values = +sample_values;
    //     data.otu_ids = +otu_ids;
    //   });

    //build the data for the chart
    // var data = [{
    //     values: globalResponse[0].sample_values, //sample_values
    //     labels: globalResponse[0].otu_ids, //otu_ids
    //     type: "pie"
    //   }];
    
    //   globalResponse[0].samples_values[1]

    //   console.log(data);
    
    // var layout = {
    //   height: 600,
    //   width: 800
    // };
    // var PIE = document.getElementById("pie");
    // Plotly.plot(PIE, data, layout);
  }
  
  function initModify(newdata) {
    var PIE = document.getElementById("pie");
    Plotly.restyle(PIE, "values", [newdata]);
  }
  
  function getData(data) {
    // var data = [];
    // switch (dataset) {
    // case "dataset1":
    //   data = [1, 2, 3, 39];
    //   break;
    // case "dataset2":
    //   data = [10, 20, 30, 37];
    //   break;
    // case "dataset3":
    //   data = [100, 200, 300, 23];
    //   break;
    // default:
    //   data = [30, 30, 30, 11];
    // }
    initModify(data);
  }
  
//   init();
  buildButton();


// Code Pile
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