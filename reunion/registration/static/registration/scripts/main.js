$(function(){

	var Registrant = Backbone.Model.extend({

	});

	var RegistrationCollection = Backbone.Collection.extend({
		model: Registrant,
		url: "/restCall"
	});

	var MembersView = Backbone.View.extend({
		el: $(".members"),
		events: {
			"click #addmore" : "addAnotherMember"
		},
		initialize:function(){
			this.addAnotherMember();
		},
		addAnotherMember: function(){
			var view = new MemberView();
			this.$(".memberList").append(view.render().el)
		}
		
	});

	var MemberView = Backbone.View.extend({
		template: _.template($("#member-template").html()),

		render: function(){
			this.$el.html(this.template(this.model));
			return this;
		}
	});
	var AppView = Backbone.View.extend({
		el: $(".wrapper"),
		initialize: function(){
			this.membersView = new MembersView();
		}
	});


	var App = new AppView;
});