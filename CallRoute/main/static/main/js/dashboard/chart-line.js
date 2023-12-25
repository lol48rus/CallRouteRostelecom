
  var ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['1LTP', '2LTP', 'Mincifra', 'Premium', 'Korp', 'VIP'],
      datasets: [{
        label: 'Ready',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      },
      {
        label: 'Queue',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      },
      {
        label: 'Avail',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      },
      {
        label: 'Talking',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        x:{
          stacked: true
        },
        y: {
          beginAtZero: true,
          stacked: true
        }
      }
    }
  });
