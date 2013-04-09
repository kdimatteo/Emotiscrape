$(document).ready(function(){
	"use strict";

	// manually bind the click event
	$("#btn-submit").on("click", function(){
		window.location = "#term/" + $("#q").val();
	});

	$('#q').bind('keypress', function(e) {
		if((e.keyCode || e.which) === 13){
			window.location = "#term/" + $("#q").val();
		}
	});


	// backbone app below her
	var ResultsView = Backbone.View.extend({
		initialize:function(){
			this.model.bind("change", this.render, this);
		},

		render:function(){

			$("#classification")
				.removeClass("text-success")
				.removeClass("text-warning");

			$("#term").html(this.model.get("original_text"));

			if (this.model.get("classification") === "pos"){
				$("#classification").html("Positive").addClass("text-success");
			} else {
				$("#classification").html("Negative").addClass("text-warning");
			}


			var probability = (this.model.get("probability_pos") >= this.model.get("probability_neg")) ? this.model.get("probability_pos") : this.model.get("probability_neg");
			$("#probability").html(probability);

			$("#probability-delta").html(this.model.get("probability_delta"));


			$("#results").removeClass("hidden");
		}
	});

	var ResultsModel = Backbone.Model.extend({
		defaults: {
			"original_text"		: "",
			"probability_pos"	: 0,
			"probability_delta" : 0,
			"probability_neg"	: 0,
			"classification"	: ""
		},

		initialize: function(q){
			this.q = q;
		},

		url : function(){
			return "/search/?q=" + this.q;
		}
	});

	var AppRouter = Backbone.Router.extend({

		routes: {
			"term/:q"	: "showResults"
		},

		test: function(){
			console.log("OK");
		},

		showResults : function(q){
			var resultsModel = new ResultsModel(q);
			var resultsView = new ResultsView({model:resultsModel});
			resultsModel.fetch();
		}

	});

	var _myRouter = new AppRouter();
	Backbone.history.start();
});