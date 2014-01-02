$(function(){

	var Registrant = Backbone.Model.extend({

	});

	var RegistrationCollection = Backbone.Collection.extend({
		model: Registrant,
		url: "\restCall"
	});

	var AppView = Backbone.View.extend({
		el: $(".wrapper"),
		initialize: function(){
			this.membersView = MembersView();
		}
	});
	
	var MembersView = Backbone.View.extend({
		el: $(".members"),
		events: {
			"click #addmore" : "addAnotherMember"
		},
		addAnotherMember: function(){
			this.html("<div class='fname'> First Name <input id='fname' type='text'></div><div class='lname'>Last Name<input id='fname' type='text'></div>");
		}
		
	});

	var App = AppView;
});