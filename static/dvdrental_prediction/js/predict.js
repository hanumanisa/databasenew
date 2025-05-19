document.addEventListener("DOMContentLoaded", function() {  
  const form = document.getElementById("predictionForm");  
  const statusBox = document.getElementById("statusBox");  
  const predictionChartElem = document.getElementById("predictionChart");  
  const predictUrl = document.getElementById("predictUrl").value;  
  let chartInstance = null;  
  
  form.addEventListener("submit", function(event) {  
    event.preventDefault();  
    statusBox.textContent = "Loading prediction...";  
      
    // Gather input data  
    const inputData = {  
      store_id: Number(document.getElementById("store_id").value),  
      active: Number(document.getElementById("active").value),  
      total_payment: Number(document.getElementById("total_payment").value),  
      payment_count: Number(document.getElementById("payment_count").value),  
      average_payment: Number(document.getElementById("average_payment").value)  
    };  
  
    // Use fetch to post data as JSON  
    fetch(predictUrl, {  
      method: 'POST',  
      headers: {  
        'Content-Type': 'application/json'  
      },  
      body: JSON.stringify(inputData)  
    })  
    .then(response => {  
      // For debugging: log the response text if it's not JSON  
      return response.text().then(text => {  
        try {  
          return JSON.parse(text);  
        } catch (error) {  
          throw new Error("Response is not valid JSON. Received: " + text);  
        }  
      });  
    })  
    .then(data => {  
      if (data.error) {  
        throw new Error(data.error);  
      }  
      statusBox.textContent = "Prediction: " + data.prediction;  
  
      const ctx = predictionChartElem.getContext("2d");  
  
      // If a chart instance exists, destroy it before creating a new one  
      if (chartInstance) {  
        chartInstance.destroy();  
      }  
  
      chartInstance = new Chart(ctx, {  
        type: 'bar',  
        data: {  
          labels: ['Class 0', 'Class 1'],  
          datasets: [{  
            label: 'Prediction Probability',  
            data: data.probability,  
            backgroundColor: ['rgba(255,99,132,0.2)', 'rgba(54, 162, 235,0.2)'],  
            borderColor: ['rgba(255,99,132,1)', 'rgba(54,162,235,1)'],  
            borderWidth: 1  
          }]  
        },  
        options: {  
          scales: {  
            y: { beginAtZero: true }  
          }  
        }  
      });  
    })  
    .catch(error => {  
      statusBox.textContent = "Error: " + error.message;  
      console.error("Error:", error);  
    });  
  });  
});  