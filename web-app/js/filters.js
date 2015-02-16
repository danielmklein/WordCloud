$(document).ready(
	function()
	{
		// enable all bootstrap tooltips
	    $('[data-toggle="tooltip"]').tooltip();

	    // hide the phase divs
	    $('#phase1').hide();

	    $('#phase2').hide();
	    $('#toggle_phase2').hide();

	   	$('#phase3').hide();
	    $('#toggle_phase3').hide();

	    $('#phase4').hide();
	    $('#toggle_phase4').hide();

	    // click handler for showing/hiding phase 1
	    $("#toggle_phase1").click(
	    	function ()
	    	{
	    		togglePhase("1")

	    	});

	    $("#toggle_phase2").click(
	    	function ()
	    	{
	    		togglePhase("2")
	    	});
	    	    
	    $("#toggle_phase3").click(
	    	function ()
	    	{
	    		togglePhase("3")
	    	});

	  	$("#toggle_phase4").click(
	    	function ()
	    	{
	    		togglePhase("4")
	    	});
	}
);

function togglePhase(phaseNum)
{
	$("#phase" + phaseNum).slideToggle("fast");
    if ($.trim($("#toggle_phase" + phaseNum).text()) === 'Show Phase ' + phaseNum) 
	{
		$("#toggle_phase" + phaseNum).text('Hide Phase ' + phaseNum);
	} else 
	{
		$("#toggle_phase" + phaseNum).text('Show Phase ' + phaseNum);        
	}

	var prev_phase_btn = $("#toggle_phase"+(parseInt(phaseNum)-1).toString());
	if (prev_phase_btn.prop("disabled"))
	{
		prev_phase_btn.prop("disabled", false);
	} else
	{
		//$("#toggle_phase"+(parseInt(phaseNum)-1).toString()).prop("disabled",true);
		prev_phase_btn.prop("disabled", true);
	}

	$("#toggle_phase" + (parseInt(phaseNum)+1).toString()).slideToggle("fast");
}
