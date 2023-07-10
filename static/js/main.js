
/*document.addEventListener("DOMContentLoaded", function() {
    var xInput = document.getElementById('x-input');
    var yInput = document.getElementById('y-input');
  
    var initialXValues = xInput.value.split(',').map(Number);
    var initialYValues = yInput.value.split(',').map(Number);
  
    var trace = {
      x: initialXValues,
      y: initialYValues,
      type: 'scatter'
    };
  
    var layout = {
      title: 'Data Visualization',
      font: {
        family: 'Times New Roman, serif',
        size: 14
      }
    };
    
  
    var config = {
      responsive: true
    };
  
    Plotly.newPlot('visualization', [trace], layout, config);
  
    function updatePlot() {
      var xValues = xInput.value.split(',').map(Number);
      var yValues = yInput.value.split(',').map(Number);
    
      trace.x = xValues;
      trace.y = yValues;
    
      // Update the bounds of the x and y axes
      layout.xaxis.range = [Math.min(...xValues), Math.max(...xValues)];
      layout.yaxis.range = [Math.min(...yValues), Math.max(...yValues)];
    
      Plotly.update('visualization', [trace], layout);
    }
    
    
    xInput.addEventListener('input', updatePlot);
    yInput.addEventListener('input', updatePlot);
});*/
