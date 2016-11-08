/*
$('#btnRefreshUnlicensed1').on('click', function () {
  var $btn = $(this).button('loading')
  // business logic...
  $(document).ready(function() {
      $.ajax({
          url: "http://rest-service.guides.spring.io/greeting"
      }).then(function(data) {
         $('.greeting-id').append(data.id);
         $('.greeting-content').append(data.content);
      });
  });
  $btn.button('reset')
});
$('#btnRefreshUnlicensed').on('click', function () {
  var $btn = $(this).button('loading')
  // business logic...
  $(document).ready(function() {
      $.ajax({
          url: "https://x0hig56teh.execute-api.us-west-2.amazonaws.com/prod/server/unlicensed&callback=?",
          datatype: "json",
          crossDomain:true
      }).then(function(data) {
        $('#unlicensedtable').bootstrapTable({
           data: data
         });
      });
  });
  $btn.button('reset')
});
*/
var apigClient = apigClientFactory.newClient({
    apiKey: 'API_KEY'
});

function writeUnlicensedTable(array) {
    var tbody = $('#unlicensedbody');
    tbody.empty();
    for (var i = 0; i < array.length; i++) {
        // create an <tr> element, append it to the <tbody> and cache it as a variable:
        var tr = $('<tr/>').appendTo(tbody);
        tr.append('<td>' + array[i].name + '</td>');
        tr.append('<td>' + array[i].site + '</td>');
        tr.append('<td>' + array[i].site_role + '</td>');
    }
}
function getUnlicensedUsers() {
  var $btn = $('#btnRefreshUnlicensed').button('loading');
  $(document).ready(function() {
    apigClient.serverInfoGet({},{},{})
    .then(function(result){
        //This is where you would put a success callback
        //console.log(result);
        writeUnlicensedTable(result.data.unlicensed);
        $('#workbookscount').empty().append(result.data.workbooks);
        $('#usercount').empty().append(result.data.user_count);
        $('#unlicensedusercount').empty().append(result.data.unlicensed_count + ' unlicensed users.');
        $('#product_version').empty().append(result.data.tableau_version);
        $('#api_version').empty().append('REST API '+ result.data.rest_api );
    }).catch( function(result){
        //This is where you would put an error callback
        console.error(result);
    });
    $btn.button('reset')
  });
}


$('#btnRefreshUnlicensed').on('click', function () {
  // business logic...
  getUnlicensedUsers();
});

$('#btnBackgroundUp').on('click', function () {
  var $btn = $(this).button('loading');
  $(document).ready(function() {
    apigClient.serverBackgrounderupGet({},{},{})
    .then(function(result){
        //This is where you would put a success callback
        console.log(result);
    }).catch( function(result){
        console.error(result);
    });
    $btn.button('reset')
  });
});

$('#btnVisqlUp').on('click', function () {
  var $btn = $(this).button('loading');
  $(document).ready(function() {
    apigClient.serverVizqlupGet({},{},{})
    .then(function(result){
        //This is where you would put a success callback
        console.log(result);
    }).catch( function(result){
        console.error(result);
    });
    $btn.button('reset')
  });
});

$('#btnRemoveUnlicensed').on('click', function () {
  var $btn = $(this).button('loading');
  $(document).ready(function() {
    apigClient.serverDeleteunlicensedGet({},{},{})
    .then(function(result){
        //This is where you would put a success callback
        console.log(result);
    }).catch( function(result){
        console.error(result);
    });
    $btn.button('reset')
  });
});

$('#btnSyncArchived').on('click', function () {
  var $btn = $(this).button('loading');
  $(document).ready(function() {
    apigClient.serverArchivesyncGet({},{},{})
    .then(function(result){
        //This is where you would put a success callback
        console.log(result);
    }).catch( function(result){
        console.error(result);
    });
    $btn.button('reset')
  });
});


$('#btnCleanup').on('click', function () {
  var $btn = $(this).button('loading');
  $(document).ready(function() {
    apigClient.serverCleanupGet({},{},{})
    .then(function(result){
        //This is where you would put a success callback
        console.log(result);
    }).catch( function(result){
        console.error(result);
    });
    $btn.button('reset')
  });
});
$('#btnArchive').on('click', function () {
  var $btn = $(this).button('loading');
  $(document).ready(function() {
    apigClient.serverArchiveGet({},{},{})
    .then(function(result){
        //This is where you would put a success callback
        console.log(result);
    }).catch( function(result){
        console.error(result);
    });
    $btn.button('reset')
  });
});


$('#btnBackupServer').on('click', function () {
  var $btn = $(this).button('loading');
  $(document).ready(function() {
    apigClient.serverBackupGet({},{},{})
    .then(function(result){
        //This is where you would put a success callback
        console.log(result);
    }).catch( function(result){
        console.error(result);
    });
    $btn.button('reset')
  });
});

$('#btnRestoreServer').on('click', function () {
  var $btn = $(this).button('loading');
  $(document).ready(function() {
    apigClient.serverRestoreGet({},{},{})
    .then(function(result){
        //This is where you would put a success callback
        console.log(result);
    }).catch( function(result){
        console.error(result);
    });
    $btn.button('reset')
  });
});

$(document).ready(function() {
  getUnlicensedUsers();
});
