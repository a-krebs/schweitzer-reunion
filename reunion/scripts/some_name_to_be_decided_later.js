$(function(){

	var Registrant = Backbone.Model.extend({

	});

	var RegistrationCollection = Backbone.Collection.extend({
		model = Registrant,
		url = "\restCall"
	});

	var AppView = Backbone.View.extend({
		el: $(".wrapper")
	});
	
	var App = AppView;
});