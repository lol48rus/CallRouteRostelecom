Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("IndexBarChart");
var myLineChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["January", "February", "March", "April", "May", "June"],
        datasets: [{
                label: 'Line Dataset',
                data: [2, 4.7, 4.9, 7.7, 2.8, 4.9, 8.6],
                lineTension: 0.1,
                fill: false,
                pointRadius: 3,
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                type: 'line'
            },
            {
                label: "Revenue",
                backgroundColor: "rgba(2,117,216,1)",
                borderColor: "rgba(2,117,216,1)",
                data: [3, 6, 4.5, 9, 3.3, 6.5],
            }
        ],
    },
    options: {
        tooltips: {
            enabled: false
        },
        scales: {
            xAxes: [{
                gridLines: {
                    display: false
                },
                display: false, // hides the vertical scale
                ticks: {
                    maxTicksLimit: 6
                }
            }],
            yAxes: [{
                ticks: {
                    min: 0,
                    max: 10,
                    maxTicksLimit: 5
                },
                display: false, // hides the vertical scale
                gridLines: {
                    display: false
                }
            }],
        },
        legend: {
            display: false
        }
    }
});