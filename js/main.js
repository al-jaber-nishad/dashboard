// Toogle Button 
let btn = document.querySelector("#toggle-btn");
let sideBar = document.querySelector(".sidebar");

btn.onclick = function () {
  sideBar.classList.toggle("inactive");
}

const skipped = (ctx, value) => ctx.p0.skip || ctx.p1.skip ? value : undefined;
const down = (ctx, value) => ctx.p0.parsed.y > ctx.p1.parsed.y ? value : undefined;

const ctx = document.getElementById('myChart').getContext('2d');

const myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12AM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM', '12PM'],
    datasets: [{
      label: 'Temperature',
      data: [65, 59, 43, 48, 56, 57, 40, 55, 43, 61, 18, 36, 77, 40, 65, 59, 32, 18, 26, 17, 70,95, 9, 22, 48, 56, 57, 40],
      borderColor: 'rgb(75, 192, 192)',
      segment: {
        borderColor: ctx => skipped(ctx, 'rgb(0,0,0,0.2)') || down(ctx, 'rgb(192,75,75)'),
        borderDash: ctx => skipped(ctx, [6, 6]),
      },
      spanGaps: true
    }]
  },
  options: {
    fill: false,
    interaction: {
      intersect: false
    },
    radius: 0,
  }
});



