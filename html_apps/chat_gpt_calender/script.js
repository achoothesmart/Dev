document.getElementById('show-calendar').addEventListener('click', showCalendar);

function getDayCell(dayOfMonth = ''){
    class_name = dayOfMonth == "" ? "" : "day-cell";
    return `<td class="${class_name}">${dayOfMonth}</td>`;
}

function showCalendar() {
    const month = parseInt(document.getElementById('month').value);
    const year = parseInt(document.getElementById('year').value);
    const calendarContainer = document.getElementById('calendar-container');

    const daysInMonth = new Date(year, month + 1, 0).getDate();

    const monthNames = [
        'January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
    ];

    let calendarHTML = `
        <h2>${monthNames[month]} ${year}</h2>
        <table>
            <tr>
                <th>Sun</th>
                <th>Mon</th>
                <th>Tue</th>
                <th>Wed</th>
                <th>Thu</th>
                <th>Fri</th>
                <th>Sat</th>
            </tr>
            <tr>`;

    let dayOfMonth = 1;
    const firstDayOfMonth = new Date(year, month, 1).getDay();

    for (let i = 0; i < firstDayOfMonth; i++) {
        calendarHTML += getDayCell();
    }

    for (let i = 0; i < 7 - firstDayOfMonth; i++) {
        calendarHTML += getDayCell(dayOfMonth);
        dayOfMonth++;
    }

    calendarHTML += '</tr>';

    while (dayOfMonth <= daysInMonth) {
        calendarHTML += '<tr>';

        for (let i = 0; i < 7; i++) {
            if (dayOfMonth > daysInMonth) {
                calendarHTML += getDayCell();
            } else {
                calendarHTML += getDayCell(dayOfMonth);
                dayOfMonth++;
            }
        }

        calendarHTML += '</tr>';
    }

    calendarHTML += '</table>';
    calendarContainer.innerHTML = calendarHTML;
}
