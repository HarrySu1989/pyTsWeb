/* globals Chart:false */

(() => {
    'use strict'

    // Graphs
    const ctx = document.getElementById('myChart1')
    var table = document.getElementById('tb1')


    //               window.alert("表格第" + rowIndex + "的内容为: " + text);
    var i;
    var labels = new Array();
    var data = new Array();
    for (i = 0; i < table.rows.length - 1; i++)
    {

        labels.push(table.rows[i + 1].cells[0].innerHTML)
        data.push(table.rows[i + 1].cells[1].innerHTML)
        //  list.push(i)s
    }

    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                lineTension: 0,
                backgroundColor: 'transparent',
                borderColor: '#007bff',
                borderWidth: 4,
                pointBackgroundColor: '#007bff'
            }]
        },
        options: {
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    boxPadding: 3
                }
            }
        }
    })
})()
