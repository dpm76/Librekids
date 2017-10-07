"use strict";

var lk = {};
lk.core = {};

/**
 * CSS classes used for selected menu items 
 */
lk.core.selectedMenuItemClasses = "w3-red w3-text-amber";

/**
 * CSS classes used for not selected menu items 
 */
lk.core.unselectedMenuItemClasses = "w3-amber w3-text-red";

lk.core.init = function()
{
	/**
	 * Inits the system
	 */
	
	
	//Init main menu buttons
	$(".lk-menu .lk-menu-item").click(
		function()
		{
			var menuItemName = $(this).attr("data-name");
			
			$(".lk-menu .lk-menu-item[data-name !='" + menuItemName + "']")
				.removeClass(lk.core.selectedMenuItemClasses)
				.addClass(lk.core.unselectedMenuItemClasses);
			
			$(this).addClass(lk.core.selectedMenuItemClasses);
						
			var target = $(this).attr("data-target");
			
			if(target)
			{				
				$.get(target, function(response) {
					$("#lk-main-panel").html(response);					  
				});
			}else
			{
				$("#lk-main-panel").html("<h1>" + menuItemName + "</h1>");
			}
		});
};

//Start core module
$(lk.core.init);
