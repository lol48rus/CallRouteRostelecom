// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example
var ctx = document.getElementById("IndexLineChart");
var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["Mar 1", "Mar 2", "Mar 3", "Mar 4", "Mar 5", "Mar 6"],
        fill: false,
        datasets: [{
                label: "Sessions",
                fill: false,
                lineTension: 0.3,
                backgroundColor: "rgba(2,117,216,0.2)",
                borderColor: "#dc3545",
                pointRadius: 0,
                pointBackgroundColor: "#dc3545",
                pointBorderColor: "rgba(255,255,255,0.8)",
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "#dc3545",
                pointHitRadius: 50,
                pointBorderWidth: 2,
                data: [3, 6, 4.5, 9, 3.3, 6.5, 6.3],
            },
            {
                label: "Sessions2",
                fill: false,
                lineTension: 0.3,
                backgroundColor: "rgba(255,255,255,0.8)",
                borderColor: "#198754",
                pointRadius: 0,
                pointBackgroundColor: "#198754",
                pointBorderColor: "rgba(255,255,255,0.8)",
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "#198754",
                pointHitRadius: 50,
                pointBorderWidth: 2,
                data: [1, 7, 2.5, 6, 4.3, 3.1, 8.1],
            }
        ]
    },
    options: {
        tooltips: {
            enabled: false
        },
        scales: {
            xAxes: [{
                time: {
                    unit: 'date'
                },
                gridLines: {
                    display: false
                },
                display: false, // hides the vertical scale
                ticks: {
                    maxTicksLimit: 7
                }
            }],
            yAxes: [{
                ticks: {
                    min: 0,
                    max: 10,
                    maxTicksLimit: 8
                },
                display: false, // hides the vertical scale
                gridLines: {
                    color: "rgba(0, 0, 0, .125)",
                }
            }],
        },
        legend: {
            display: false
        }
    }
});