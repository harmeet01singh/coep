var nameSpace = function(scope) {

	var com;

	if (scope.com == null || typeof (scope.com) != "object") {
		com = scope.com = {};
	} else {
		com = scope.com;
	}

	com.coep = {
		// handler for html template processing
		template : function() {
		},

		test : {

			ajaxHandler : function() {},
			WaterData : function() {}


		}
	};

}(this);
