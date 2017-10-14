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
	

	$(".lk-menu .lk-menu-item").click(function()
	{
		/**
		 * Init main menu buttons 
		 */
		
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
	}).mouseenter(function()
	{
		$(this).siblings().children(".lk-main-menu-item-more").children(".lk-main-menu-submenu").hide();
		$(this).children(".lk-main-menu-item-more").children(".lk-main-menu-submenu").show();		
	});	
	
	$(".lk-main-menu-item-more").click(function(event)
	{
		/**
		 * Init submenu-item buttons
		 * 
		 * @param event: event data
		 */
		
		event.stopPropagation();
		$(this).children(".lk-main-menu-submenu").toggle();
	});
	
	
	$(".lk-main-menu-submenu").mouseleave(function(){
		/**
		 * Handles mouse leave event of submenu
		 */
		
		$(this).hide();
	});
	
	$(".lk-main-menu-submenu .lk-menu-item").click(function()
	{
		$(this).parents(".lk-menu-item").addClass(lk.core.selectedMenuItemClasses);
	});
};

//Start core module
$(lk.core.init);
