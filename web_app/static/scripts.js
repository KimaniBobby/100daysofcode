// static/scripts.js

$(document).ready(function() {
    // Initialize the date picker
    $('#date').datepicker({
        format: 'yyyy-mm',
        minViewMode: 'months'
    });

    // Handle form submission
    $('#earnings-form').submit(function(event) {
        event.preventDefault();
        const form = $(this);
        const url = form.attr('action');
        const formData = form.serialize();

        // Send the form data to the server using AJAX
        $.ajax({
            type: 'POST',
            url: url,
            data: formData,
            dataType: 'json',
            success: function(response) {
                alert(response.message);
                form.trigger('reset'); // Reset the form fields
                fetchEarningsTable(); // Update the earnings table
                fetchReports(); // Update the weekly and monthly reports
            },
            error: function(error) {
                alert(error.responseJSON.error);
            }
        });
    });

    // Fetch and update the earnings table and reports on page load
    fetchEarningsTable();
    fetchReports();
});

// Function to fetch and update the earnings table
function fetchEarningsTable() {
    $.ajax({
        type: 'GET',
        url: '/get_earnings_table',
        dataType: 'json',
        success: function(response) {
            const earningsTable = response;
            const tableBody = $('#earnings-table tbody');
            tableBody.empty();

            earningsTable.forEach(function(row) {
                const date = row.date;
                const earnings = row.earnings;
                const newRow = `<tr><td>${date}</td><td>${earnings}</td></tr>`;
                tableBody.append(newRow);
            });
        },
        error: function(error) {
            alert('Error fetching earnings table.');
        }
    });
}

// Function to fetch and update the weekly and monthly reports
function fetchReports() {
    $.ajax({
        type: 'GET',
        url: '/generate_reports',
        dataType: 'json',
        success: function(response) {
            const weeklyReport = response.weekly_report;
            const monthlyReport = response.monthly_report;

            updateReportTable('#weekly-report', weeklyReport, 'Year', 'Week');
            updateReportTable('#monthly-report', monthlyReport, 'Year', 'Month');
        },
        error: function(error) {
            alert('Error generating reports.');
        }
    });
}

// Function to update the report tables (weekly and monthly)
function updateReportTable(tableId, reportData, yearLabel, timeLabel) {
    const tableBody = $(`${tableId} tbody`);
    tableBody.empty();

    reportData.forEach(function(row) {
        const year = row.year;
        const time = row[timeLabel.toLowerCase()];
        const earnings = row.earnings;
        const newRow = `<tr><td>${year}</td><td>${time}</td><td>${earnings}</td></tr>`;
        tableBody.append(newRow);
    });
}
