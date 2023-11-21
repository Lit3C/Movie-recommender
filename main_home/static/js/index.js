const totalViewChart = document.getElementById('total-views-chart');
const revenueChart = document.getElementById('revenue-chart');
const growthRateChart = document.getElementById('growth-rate-chart');
const subscriberCountChart = document.getElementById('subscriber-count');
const trafficSourcesElement = document.getElementById('traffic-sources');
const datatable = document.getElementById('datatable');

new Chart(totalViewChart, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
            labels: '# of votes',
            data: [12545, 19512, 37897, 54574, 29564, 44547],
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const estimatedRevenueChart = new Chart(revenueChart, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
            labels: '# of votes',
            data: [255, 280, 290, 179, 512, 580],
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const subscriberCount = new Chart(subscriberCountChart, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [
      {
          label: '# of People voted',
          data: [12, 19, 3, 5, 2, 3],
          backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(255, 159, 64, 0.2)',
          'rgba(255, 205, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(201, 203, 207, 0.2)'
          ],
          borderColor: [
          'rgb(255, 99, 132)',
          'rgb(255, 159, 64)',
          'rgb(255, 205, 86)',
          'rgb(75, 192, 192)',
          'rgb(54, 162, 235)',
          'rgb(153, 102, 255)',
          'rgb(201, 203, 207)'
          ],
          borderWidth: 1
      },
      {
          label: '# of People not voted',
          data: [1, 5, 3, 5, 2, 3],
          backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(255, 159, 64, 0.6)',
          'rgba(255, 205, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(153, 102, 255, 0.6)',
          'rgba(201, 203, 207, 0.6)'
          ],
          borderColor: [
          'rgb(255, 99, 132)',
          'rgb(255, 159, 64)',
          'rgb(255, 205, 86)',
          'rgb(75, 192, 192)',
          'rgb(54, 162, 235)',
          'rgb(153, 102, 255)',
          'rgb(201, 203, 207)'
          ],
          borderWidth: 1
      }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

const trafficSourcesChart = new Chart(trafficSourcesElement, {
    type: 'pie',
    data: {
        labels: ['Youtube', 'Facebook', 'Snapchat', 'Google', 'FireFox', 'Opera'],
        datasets: [{
            labels: '# shares',
            data: [12, 19, 3, 5, 2, 3],
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
})

// Initialize datatable
const dataTable = new simpleDatatables.DataTable("#datatable",{
    searchable: true,
    fixedHeight: true,
    data : {
        headings: ['Video Title', 'Published Date', 'Views Count'],
    }
});
let newRows = [
    ['Video Title 1', '2021-06-01', 12545],
    ['Video Title 2', '2021-06-02', 19512],
    ['Video Title 3', '2021-06-03', 37897],
    ['#############', '2021-06-04', 54574],
    ['Video Title 5', '2021-06-05', 29564],
    ['#############', '2021-06-04', 54574],
    ['#############', '2021-06-04', 54574],
    ['#############', '2021-06-04', 54574],
    ['#############', '2021-06-04', 54574],
    ['#############', '2021-06-04', 54574],
    ['#############', '2021-06-04', 54574],
    ['#############', '2021-06-04', 54574]
];
dataTable.insert({data: newRows})


