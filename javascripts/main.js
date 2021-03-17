$(document).ready(function () {
  // Create the datatable from the data.
  var table = $("#datatable").DataTable({
    "deferRender": true,
    "pageLength": 25,
    "dom": 'Bfrtip',
    "buttons": [
      { className: "csvButton", title: "Articles", exportOptions: { columns: [ 1, 2, 3] }, customize: function(csv) {var csvRows = csv.split('\n'); csvRows[0] = csvRows[0].replace('""', "SHA"); return csvRows.join('\n'); } },
      { className: "excelButton", title: "Articles", exportOptions: { columns: [ 1, 2, 3] } } ],
    "ajax": "data/datatable.txt",
    "columns": [
      {
        "className": "details-control",
        "orderable": false,
        "data": null,
        "defaultContent": ""
      },
      { "data": "Title" },
      { "data": "Authors" },
      { "data": "Journal" },
      { "data": "SHA" }
    ],
    "columnDefs": [
      { "width": "40%", "targets": 1 },
      { "width": "20%", "targets": 3 },
      { "targets": [4], "visible": false, "searchable": true },
      { "targets": [0], "orderable": false, "searchable": false }
    ]
  });

    })
// End of ready function

function format(d) {

    // d is the data object of the clicked row
    // We will have one row and two columns

    var div = '<div class="container-fluid"> <div class="row"> ';

    var table = '<div class="col-md-5"> <table id="small_table" class="smallTable" cellpadding="5" cellspacing="0" border="0">'+
      '<tr>' +
          '<td>Paper ID:</td>'+
          '<td>'+ d.SHA + '</td>'+
      '</tr>' +

      '<tr>'+
          '<td>Journal:</td>'+
          '<td>' + d.Journal + '</td>'+
      '</tr>' +

      '<tr>' +
          '<td>Publish Time:</td>'+
          '<td>' + d['Publish Time'] + '</td>'+
      '</tr>'

    return div + table + text;
}
