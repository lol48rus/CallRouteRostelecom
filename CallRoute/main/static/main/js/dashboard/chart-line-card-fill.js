
  var ctx = document.getElementById('ChartLineCardFill');

 new Chart(ctx, {
		type : 'line',
		data : {
			labels : [ 1500, 1600, 1700, 1750, 1800, 1850,
					1900, 1950, 1999, 2050 ],
			datasets : [
					{
						data : [ 186, 205, 1321, 1516, 2107,
								2191, 3133, 3221, 4783, 5478 ],
						label : "America",
						borderColor : "#0B9EF2",
						fill : true,
						backgroundColor: "#EFF8FE",
						tension: 0.3
					}]
		},
		options : {
			title : {
				display : true,
				text : 'Chart JS Line Chart Example'
			}
		}
	});