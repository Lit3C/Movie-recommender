
const datatable = document.getElementById('cast-datatable');
// Initialize datatable
const dataTable = new simpleDatatables.DataTable("#cast-datatable",{
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