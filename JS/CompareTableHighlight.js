comparisonTable = document.querySelector('.cmp-comparison-table__body')
allRows = comparisonTable.querySelectorAll('tr')
allRows.forEach(row => {
    cols = row.querySelectorAll('td')

    let firstCol = true
    let prevColVal = ''
    cols.forEach(col => {
        colVal = col.textContent
        console.log(colVal)
        if(!firstCol && prevColVal != colVal){
            col.style.color = 'RED'
        }
        prevColVal = colVal
        firstCol = false
    })
});