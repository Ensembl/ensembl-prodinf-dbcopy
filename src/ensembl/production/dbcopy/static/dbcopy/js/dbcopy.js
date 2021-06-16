/*jshint esversion: 6 */

(function ($) {
    "use strict";

    let SrcHostDetails;
    let TgtHostsDetails;
    let DBNames = [];
    let TableNames = [];

    $(document).ready(function () {
        $(".field-wipe_target").hide();
        $(".field-convert_innodb").hide();
        $(".field-dry_run").hide();
        let trs = $("#changelist-form tr");
        trs.has("td.field-overall_status div.Complete").addClass('Complete');
        trs.has("td.field-overall_status div.Running").addClass('Running');
        trs.has("td.field-overall_status div.Incomplete").addClass('Incomplete');
        trs.has("td.field-overall_status div.Submitted").addClass('Submitted');
        trs.has("td.field-overall_status div.Scheduled").addClass('Scheduled');
        trs.has("td.field-overall_status div.Failed").addClass('Failed');
        let tds = $("#changelist-form tr td.field-overall_status");
        tds.has("div.Complete").addClass('Complete');
        tds.has("div.Running").addClass('Running');
        tds.has("div.Incomplete").addClass('Incomplete');
        tds.has("div.Submitted").addClass('Submitted');
        tds.has("div.Scheduled").addClass('Scheduled');
        tds.has("div.Failed").addClass('Failed');
        let srcHostElem = $("#id_src_host");
        let tgtHostElem = $("#id_tgt_host");

        /*if (srcHostElem.val() && tgtHostElem.val()) {
            SrcHostDetails = hostStringToDetails(srcHostElem.val());
            TgtHostsDetails = getHostsDetails(tgtHostElem.val());
            updateAlerts();
        }*/
       // $("#id_src_host").dispatchEvent(change);
        $("#requestjob_form").find(':input').each(function(){
            $(this).on('change', function(){
                checkHostsTargets();
            });
        });
        $('#requestjob_form .nav-tabs a[href="#transferlogs-tab"]').on('shown.bs.tab', function(e) {
            $('#transferlogs-tab .paginator a.page-link').each(function (index) {
                $(this).attr('href', $(this).attr('href') + "#transferlogs-tab");
            });
        });
    });


    // Commented until Wipe target feature is enabled by DBAs
    //
    function checkWipeTarget() {
        const sourceDBNames = $("#id_src_incl_db").val();
        const targetDBNames = $("#id_tgt_db_name").val();
        if (!(sourceDBNames.length || targetDBNames.length)) {
            $("#id_wipe_target").prop("disabled", "true");
        } else {
            $("#id_wipe_target").removeAttr("disabled");
        }
    }

    function mapMessages(messages, title){
        return $.map(messages, function (value, key) {
            return '<li class="request-messages">'+title+': [' + key + ']<ul class="sub-list">' +
                value.map(function(v){
                    return '<li>' + v + '</li>';
                }).join('') + '</ul></li>';
        }).join('');
    }

    function displayAlert(object, error=false){
        $(object.html()).insertBefore($('div.submit-row')).attr('id', object.attr('id') + "Box");
        if (error) {
            $('div.submit-row').find(':input').each(function(){
                $(this).prop('disabled', true);
            });
        }
    }

    function checkHostsTargets() {
        var formData = $("#requestjob_form").serializeArray();
        $.post({
            url: `/dbcopy/jobschecks/dbnames/`,
            dataType: "json",
            data: formData,
            success: function (data) {
                $('#dbnamesAlertBox').remove();
                $('#dbtableAlertBox').remove();
                $('#blockingAlertBox').remove();
                $('div.submit-row').find(':input').each(function(){
                    $(this).removeAttr('disabled');
                });
            },
            error: function (xhr, status, error) {
                $('#dbnamesAlertBox').remove();
                $('#dbtablesAlertBox').remove();
                $('#blockingAlertBox').remove();
                $('div.submit-row').find(':input').each(function(){
                    $(this).removeAttr('disabled');
                });
                console.log('error', Object.keys(xhr.responseJSON.dberrors).length);
                if (Object.keys(xhr.responseJSON.dberrors).length > 0){
                    $('#blockingAlert div ul').html(mapMessages(xhr.responseJSON.dberrors, 'Host'));
                    displayAlert($('#blockingAlert'), true);
                }
                if (Object.keys(xhr.responseJSON.dbwarnings).length > 0) {
                    $('#dbnamesAlert div ul').html(mapMessages(xhr.responseJSON.dbwarnings, 'Host'));
                    displayAlert( $('#dbnamesAlert'));
                }
                if (Object.keys(xhr.responseJSON.tableerrors).length > 0){
                    $('#blockingAlert div ul').html(mapMessages(xhr.responseJSON.tableerrors, 'Database'));
                    displayAlert($('#blockingAlert'), true);
                }
                if (Object.keys(xhr.responseJSON.tablewarnings).length > 0) {
                    $('#dbtablesAlert div ul').html(mapMessages(xhr.responseJSON.tablewarnings, 'Database'));
                    displayAlert($('#dbtablesAlert'));
                }
            }
        });
    }
})(jQuery || django.jQuery);
