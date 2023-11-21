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
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
            labels: '# of votes',
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


