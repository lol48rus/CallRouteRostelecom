// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("LineStuckedBarChart");
var myStackedBurChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["SG_FIrstLine", "SG_1LTP", "SG_2LTP", "SG_DigitalEconomy", "SG_DigitalEconomy2", "SG_KKFU"],
        datasets: [{
                label: 'RouterQeueCalls',
                data: [200, 580, 555, 800, 900, 1200, 1700],
                fill: false, // заливка. это не столб, \то линия!
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                type: 'line'
            },
            {
                label: "RouterAband",
                backgroundColor: "rgba(2,117,216,1)",
                borderColor: "rgba(2,117,216,1)",
                data: [421, 501, 625, 784, 982, 1498],
            },
            {
                label: "RouterQeueCalls",
                backgroundColor: "rgba(6,117,26,1)",
                borderColor: "rgba(6,117,26,1)",
                data: [670, 350, 670, 900, 130, 600],
            }
        ],
    },
    options: {
        scales: {
            xAxes: [
                {
                time: {
                    unit: 'month'
                },
                gridLines: {
                    display: false
                },
                ticks: {
                    maxTicksLimit: 6
                },
                stacked: true
            }],
            yAxes: [{
                ticks: {
                    min: 0,
                    max: 1800,
                    maxTicksLimit: 5
                },
                stacked: true,
                gridLines: {
                    display: true
                }
            }],
        },
        legend: {
            display: true
        }
    }
});