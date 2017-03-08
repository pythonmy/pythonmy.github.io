function populateHeader(){
	$("#header").load("static/header.html", function(){
        $('.nav > li').removeClass('active');
        $('a[href="' + location.pathname + '"]').closest('li').addClass('active'); 
    });
}

function populateSection(){
	$("#section").load("static/section.html", function(){
	    var hdbartpls = ['javascripts/companyportlet.handlebars', 'javascripts/peopleportlet.handlebars', 'javascripts/newsportlet.handlebars'];
	    var sources = ['resources/company.json', 'resources/people.json', 'resources/news.json'];
	    var portletels = ['#companies', '#people', '#news'];

	    renderPortlet(sources[0], hdbartpls[0], portletels[0]);
	    renderPortlet(sources[1], hdbartpls[1], portletels[1]);
	    renderPortlet(sources[2], hdbartpls[2], portletels[2]);
    });
}

function populateFooter(){
	$("#footer").load("static/footer.html");
}

function populateView(){
	populateHeader();
	populateSection();
	populateFooter();
}