$(document).ready(
	function()
	{
		// enable all bootstrap tooltips
	    $('[data-toggle="tooltip"]').tooltip();

	    // hide the phase 1 div
	    $('#phase1').hide();

	    $("#toggle_phase1").click(
	    	function() 
	    	{
	    		toggleDiv("phase1")
	    	});
	}
);

function toggleDiv(divId)
{
	$("#" + divId).slideToggle("fast");
}
