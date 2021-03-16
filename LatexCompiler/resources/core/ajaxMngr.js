(function(AH, WD) {

	AH.getAssemblyUPIData = function(url, methodType) {

		$.ajax({
			type : methodType,
			url : url,
			dataType : 'json',
			contentType : 'application/json',
			 
			success : function(data) {
				
				if (data.done == false) {
				} else {
					if (data.length != 0) {
//						AD.renderAssemblyUPIData(data.data);
					} else {

					}
				}
			},
             
			error : function() {
			}
			

		});
		


	}
	
	

})
		(com.coep.test.ajaxHandler, com.coep.test.WaterData);