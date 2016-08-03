#!/usr/bin/python2

data=open("results.bin","rb").read();

print """	
function getdata() {
	var data = [];
	var dataPoints0 = [];
	var dataPoints1 = [];
	var dataPoints2 = [];
	var dataPoints3 = [];
"""

count=0;
for i in data:
	j=0;
	if i == 'S':
		j=1
	elif i == 'M':
		j=2
	elif i == '\n':
		j=3
	print """	dataPoints"""+str(j)+""".push({
		x: """+str(count)+""",
		y: 0.9+0.1*"""+str(j)+"""
	});"""
	count+=1


print """
	var dataSeries0 = { type: "scatter",legendText:"no hit",showInLegend: true,};
	var dataSeries1 = { type: "scatter",legendText:"hit square",showInLegend: true,};
	var dataSeries2 = { type: "scatter",legendText:"hit multiply",showInLegend: true,};
	var dataSeries3 = { type: "scatter",legendText:"hit barrett",showInLegend: true,};
	dataSeries0.dataPoints = dataPoints0;
	dataSeries1.dataPoints = dataPoints1;
	dataSeries2.dataPoints = dataPoints2;
	dataSeries3.dataPoints = dataPoints3;
	data.push(dataSeries0);
	data.push(dataSeries1);
	data.push(dataSeries2);
	data.push(dataSeries3);
	return data;
}
"""
