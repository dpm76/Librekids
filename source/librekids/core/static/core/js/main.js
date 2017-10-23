"use strict";

var lk = {};
lk.core = {};

/**
 * CSS classes used for selected menu items 
 */
lk.core.selectedMenuItemClasses = "w3-indigo";

/**
 * CSS classes used for not selected menu items 
 */
lk.core.unselectedMenuItemClasses = "w3-dark-marine";

lk.core.loadView = function(viewName)
{
	/**
	 * Loads a view into content area
	 */
	
	//Select related menu item
	$(".lk-menu .lk-menu-item[data-name !='" + viewName + "']")
		.removeClass(lk.core.selectedMenuItemClasses)
		.addClass(lk.core.unselectedMenuItemClasses);
	
	var menuItem = $(".lk-menu-item[data-name ='" + viewName + "']");

	$(menuItem).addClass(lk.core.selectedMenuItemClasses);
	$(menuItem).parents(".lk-menu-item").addClass(lk.core.selectedMenuItemClasses);
				
	//Load view target
	var target = $(menuItem).attr("data-target");
	
	if(target)
	{				
		$.get(target, function(response) {
			$("#lk-main-panel").html(response);					  
		});
	}else
	{
		$("#lk-main-panel").html("<h1>" + viewName + "</h1><p>Not yet implemented.</p>");
	}
}; 

lk.core.init = function()
{
	/**
	 * Inits the system
	 */
	

	$(".lk-menu .lk-menu-item").click(function()
	{
		/**
		 * Opens the view related to the clicked menu item 
		 */
		
		var viewName = $(this).attr("data-name");
		lk.core.loadView(viewName);
		
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
	
	//Load current view
	//TODO: 20171023 DPM - Temporally it get the first menu item, which should be the home view. 
	//Later, it must be provided from the view controller, according to the session data. 
	var viewName = $("#lk-main-menu > .lk-menu-item").first().attr("data-name");  
	lk.core.loadView(viewName);	
};

//Start core module
$(lk.core.init);
