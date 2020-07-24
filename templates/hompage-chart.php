<?php
$chartData = simplexml_load_file("./data-cache/homepage-chart.xml") or die("Error: Cannot create object");
$pills = [$chartData->pills->adverts;, $chartData->pills->averagePrice;]
?>
<script>
window.onload = function () {
var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	exportEnabled: true,
	theme: "light1", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "Simple Column Chart with Index Labels"
	},
	data: [{
		type: "column", //change type to bar, line, area, pie, etc
		//indexLabel: "{y}", //Shows y value on all Data Points
		indexLabelFontColor: "#5A5757",
      	indexLabelFontSize: 16,
		indexLabelPlacement: "outside",
		dataPoints: [
			{ x: 10, y: <?php echo $pills[0] ?>, indexLabel: "\f484 Pills" }
			]
	}]
});
var chart1 = new CanvasJS.Chart("chartContainer1", {
	animationEnabled: true,
	exportEnabled: true,
	theme: "light1", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "Simple Column Chart with Index Labels"
	},
	data: [{
		type: "column", //change type to bar, line, area, pie, etc
		//indexLabel: "{y}", //Shows y value on all Data Points
		indexLabelFontColor: "#5A5757",
      	indexLabelFontSize: 16,
		indexLabelPlacement: "outside",
		dataPoints: [
			{ x: 10, y: <?php echo $pills[1] ?>, indexLabel: "\f484 Pills" }
			]
	}]
});
chart.render();
chart1.render();
}
</script>
<div id="chartContainer" style="height: 370px; width: 100%;"></div>
<div id="chartContainer1" style="height: 370px; width: 100%;"></div>