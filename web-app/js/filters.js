$(document).ready(
	function()
	{
		// enable all bootstrap tooltips
	    $('[data-tog="tooltip"]').tooltip();

	    // hide the fltr_lvl divs
	    $('#fltr_lvl1').hide();

	    $('#fltr_lvl2').hide();
	    $('#tog_fltr_lvl2').hide();

	   	$('#fltr_lvl3').hide();
	    $('#tog_fltr_lvl3').hide();

	    $('#fltr_lvl4').hide();
	    $('#tog_fltr_lvl4').hide();

	   	$('#fltr_lvl5').hide();
	    $('#tog_fltr_lvl5').hide();

	   	$('#fltr_lvl6').hide();
	    $('#tog_fltr_lvl6').hide();

	   	$('#fltr_lvl7').hide();
	    $('#tog_fltr_lvl7').hide();

	    // click handler for showing/hiding fltr_lvl 1
	    $("#tog_fltr_lvl1").click(
	    	function ()
	    	{
	    		toggle_filter_level("1")

	    	});

	    $("#tog_fltr_lvl2").click(
	    	function ()
	    	{
	    		toggle_filter_level("2")
	    	});
	    	    
	    $("#tog_fltr_lvl3").click(
	    	function ()
	    	{
	    		toggle_filter_level("3")
	    	});

	  	$("#tog_fltr_lvl4").click(
	    	function ()
	    	{
	    		toggle_filter_level("4")
	    	});

	  	$("#tog_fltr_lvl5").click(
	    	function ()
	    	{
	    		toggle_filter_level("5")
	    	});

	  	$("#tog_fltr_lvl6").click(
	    	function ()
	    	{
	    		toggle_filter_level("6")
	    	});

	  	$("#tog_fltr_lvl7").click(
	    	function ()
	    	{
	    		toggle_filter_level("7")
	    	});
	}
);

function toggle_filter_level(levelNum)
{
	// first of all, tog the fltr_lvl div itself
	$("#fltr_lvl" + levelNum).slideToggle("fast");

	// if we just showed the fltr_lvl, change the button text to "Hide",
	// and switch the button color from green to red
    if ($.trim($("#tog_fltr_lvl" + levelNum).text()) === 'Show Filter Level ' + levelNum) 
	{
		$("#tog_fltr_lvl" + levelNum).text('Hide Filter Level ' + levelNum);
		$("#tog_fltr_lvl" + levelNum).removeClass("btn-success");
		$("#tog_fltr_lvl" + levelNum).addClass("btn-danger");

	} else // otherwise change button to "Show" and switch from red to green 
	{
		$("#tog_fltr_lvl" + levelNum).text('Show Filter Level ' + levelNum);
		$("#tog_fltr_lvl" + levelNum).removeClass("btn-danger");
		$("#tog_fltr_lvl" + levelNum).addClass("btn-success");        
	}

	// disable the previous fltr_lvl's button if we just Showed, and 
	// enable it if we just did a Hide
	var prev_fltr_lvl_btn = $("#tog_fltr_lvl"+(parseInt(levelNum)-1).toString());
	if (prev_fltr_lvl_btn.prop("disabled"))
	{
		prev_fltr_lvl_btn.prop("disabled", false);
	} else
	{
		prev_fltr_lvl_btn.prop("disabled", true);
	}

	// finally, tog the Show/Hide button itself
	$("#tog_fltr_lvl" + (parseInt(levelNum)+1).toString()).slideToggle("fast");
}
