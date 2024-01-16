
var ctx = document.getElementById("HorizonthalChart").getContext('2d');;
var myChart = new Chart(ctx, {
  type: "horizontalBar",
  data: {
    datasets: [
      {
        label: "Clients Signed",
        backgroundColor: "rgba(150,150,150,0.8)",
        data: [12, 0, 3, 5, 1, 3, 6, 5, 3, 10],
        // barThickness: 9, //<---- here important
      }
    ],
    labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  },
  options: {
    responsive: false,
    // barPercentage: 1.0,
    // categoryPercentage: 1.0,
    // maintainAspectRatio: false,//<---- here important
    scales: {
      yAxes: [
        {
          ticks: {
            // display: display,
            // padding: -4,
            // fontColor: "#000",
            //mirror: true
          }
        }
      ]
    }
  }
});






// var ctx = document.getElementById('HorizonthalChart').getContext('2d');
// var chart = new Chart(ctx, {
//   type: 'horizontalBar', // <-- instead of 'bar'
//   data: {
//     labels: ['A', 'B', 'C'],
//     datasets: [{
//       label: 'Easy as',
//       data: [1, 2, 3],
//     }],
//   },
//   options: {
//     responsive: true
//   }
// });