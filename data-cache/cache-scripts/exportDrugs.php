<?php
/* vars for export */
include('../../config.php');
// database record to be exported
$exp_table = 'Drugs';

// Create connection
$mysqli = new mysqli($hostname, $user, $password, $database);
$mysqli->set_charset("utf8");

if (!$mysqli)
    die("ERROR: Could not connect. " . mysqli_connect_error());

// Create and open new csv file
$csv  = '../' . $exp_table . "_" . date('d-m-Y-his') . '.csv';
$file = fopen($csv, 'w');

// Get the table
if (!$mysqli_result = mysqli_query($mysqli, "SELECT * FROM {$exp_table}"))
    printf("Error: %s\n", $mysqli->error);

    // Get column names
    while ($column = mysqli_fetch_field($mysqli_result)) {
        $column_names[] = $column->name;
    }

    // Write column names in csv file
    if (!fputcsv($file, $column_names))
        die('Can\'t write column names in csv file');

    // Get table rows
    while ($row = mysqli_fetch_row($mysqli_result)) {
        // Write table rows in csv files
        if (!fputcsv($file, $row))
            die('Can\'t write rows in csv file');
    }

fclose($file);

header("Location: " .  $csv);
?>
