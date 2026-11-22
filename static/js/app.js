document.addEventListener('DOMContentLoaded',()=>{
 const range=document.getElementById('areaRange'), output=document.getElementById('areaValue');
 if(range&&output){range.addEventListener('input',()=>output.value=range.value);}
 if(window.farmguardCharts&&window.Chart){
  const palette=['#5eaa7d','#e4bd57','#df9658','#cf6864','#9ebea7'];
  const cropCanvas=document.getElementById('cropChart');
  if(cropCanvas){new Chart(cropCanvas,{type:'doughnut',data:{labels:window.farmguardCharts.cropLabels,datasets:[{data:window.farmguardCharts.cropValues,backgroundColor:palette,borderWidth:3,borderColor:'#fff',hoverOffset:4}]},options:{responsive:true,maintainAspectRatio:false,cutout:'70%',plugins:{legend:{display:false},tooltip:{backgroundColor:'#203b2b',padding:10}}}});
   const legend=document.getElementById('cropLegend'); if(legend){legend.innerHTML=window.farmguardCharts.cropLabels.map((label,i)=>`<div class="legend-item"><i style="background:${palette[i%palette.length]}"></i>${label}<b>${window.farmguardCharts.cropValues[i]}</b></div>`).join('');}}
  const severityCanvas=document.getElementById('severityChart');
  if(severityCanvas){new Chart(severityCanvas,{type:'bar',data:{labels:window.farmguardCharts.severityLabels,datasets:[{data:window.farmguardCharts.severityValues,backgroundColor:['#6eb78b','#e4bd57','#df9658','#cf6864'],borderRadius:5,maxBarThickness:34}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false},ticks:{font:{size:9}}},y:{beginAtZero:true,ticks:{precision:0,font:{size:9}},grid:{color:'#f0f3f0'}}}}});}
 }
});
