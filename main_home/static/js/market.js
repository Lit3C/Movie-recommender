const trafficSourcesElement = document.getElementById('traffic-sources');

const trafficSourcesChart = new Chart(trafficSourcesElement, {
    type: 'pie',
    data: {
        labels: ['Couples avec enfants', 'Couples sans enfant', 'Femme seule', 'Famille monoparentale', 'Homme seul'],
        datasets: [{
            label: 'Type de ménage',
            data: [40000, 35000, 13000, 11000, 11000],
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        // Pour afficher le pourcentage dans les infobulles display en hover
        plugins: {
            tooltip: {
                callbacks: {
                    label: function(context) {
                        var label = context.label || '';
                        var value = context.dataset.data[context.dataIndex] || 0;
                        var dataset = context.dataset || {};
                        var total = dataset.data.reduce((a, b) => a + b, 0);
                        var percentage = ((value / total) * 100).toFixed(2);
                        return label + ': ' + value + ' (' + percentage + '%)';
                    }
                }
            }
        }
    }
});
    