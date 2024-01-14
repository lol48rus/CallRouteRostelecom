

var ctx = document.getElementById("HalfDoughnutChart");
var myChart = new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: ["Red"],
    datasets: [
      {
        label: ["# of Votes"],
        data: [45, 40],
        backgroundColor: ["#ffffff"],
        borderWidth: 1
      }
    ]
  },
  options: {
    maintainAspectRatio: false,
    circumference: Math.PI,
    rotation: -Math.PI,
    cutoutPercentage: 50,
    legend: {
            display: false
        },
    onClick(...args) {
      console.log(args);
    },
    onAnimationProgress: function () {
      const dataset = this.data.datasets[0];
      const model = dataset._meta[Object.keys(dataset._meta)[0]].data[0]._model;

      console.log(model);
      if (!model) {
        return;
      }
      // model.x and model.y is the center of the chart
      this.ctx.fillText("00%", model.x, model.y);
    }
  }
});
