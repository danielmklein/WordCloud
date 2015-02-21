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

	   	$('#phase5').hide();
	    $('#toggle_phase5').hide();

	   	$('#phase6').hide();
	    $('#toggle_phase6').hide();

	   	$('#phase7').hide();
	    $('#toggle_phase7').hide();

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

	  	$("#toggle_phase5").click(
	    	function ()
	    	{
	    		togglePhase("5")
	    	});

	  	$("#toggle_phase6").click(
	    	function ()
	    	{
	    		togglePhase("6")
	    	});

	  	$("#toggle_phase7").click(
	    	function ()
	    	{
	    		togglePhase("7")
	    	});
	}
);

function togglePhase(phaseNum)
{
	// first of all, toggle the phase div itself
	$("#phase" + phaseNum).slideToggle("fast");

	// if we just showed the phase, change the button text to "Hide",
	// and switch the button color from green to red
    if ($.trim($("#toggle_phase" + phaseNum).text()) === 'Show Phase ' + phaseNum) 
	{
		$("#toggle_phase" + phaseNum).text('Hide Phase ' + phaseNum);
		$("#toggle_phase" + phaseNum).removeClass("btn-success");
		$("#toggle_phase" + phaseNum).addClass("btn-danger");

	} else // otherwise change button to "Show" and switch from red to green 
	{
		$("#toggle_phase" + phaseNum).text('Show Phase ' + phaseNum);
		$("#toggle_phase" + phaseNum).removeClass("btn-danger");
		$("#toggle_phase" + phaseNum).addClass("btn-success");        
	}

	// disable the previous phase's button if we just Showed, and 
	// enable it if we just did a Hide
	var prev_phase_btn = $("#toggle_phase"+(parseInt(phaseNum)-1).toString());
	if (prev_phase_btn.prop("disabled"))
	{
		prev_phase_btn.prop("disabled", false);
	} else
	{
		prev_phase_btn.prop("disabled", true);
	}

	// finally, toggle the Show/Hide button itself
	$("#toggle_phase" + (parseInt(phaseNum)+1).toString()).slideToggle("fast");
}
