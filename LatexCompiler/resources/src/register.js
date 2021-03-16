(function(AH, WD) {

	WD.getsocietydata = function()
	{
		var RegisterDataDisplay = '';
		RegisterDataDisplay += '';
		
		+'<div class="container-fluid" id="registration">          '    
		+'<div class="row"> '
		+'<div class="col-sm-12 col-md-6 col-lg-6 col-xl-6">'
		+'<h1> Registration Form</h1>'
		+'<p>You have to register here with society details.</p>'
		+'<p></p>'
		+'<button class="btn btncolor" type="submit" style="margin:0 30%;">Home</button>'
		+'</div>'
		+'<div class="col-sm-12 col-md-6 col-lg-6 col-xl-6">'
		+' <form class="container" id="needs-validation" novalidate>'
		    
		  
		    
		+' <div class="form-group">'

		    
		+'<div class="row">'
		+'<div class="col-md-12 mb-3">'
		+'<label for="SocietyName">Society name</label>'
		+' <input type="text" class="form-control" id="SocietyName" placeholder="Society name"  required>'
		+'  <div class="invalid-feedback">  '
		+'   Please provide a Society name.'
		+'    </div>'
		+'   </div>'
		+'   <div class="col-md-12 mb-3">'
		+'     <label for="Address">Address</label>'
		+'    <input type="text" class="form-control" id="Address" placeholder="Society address" required>'
		+'        <div class="invalid-feedback">  '
		+'        Please provide a Society address.'
		+'     </div>'
		+'      </div>'
		+'  </div>'
		+'  <div class="row">    '
		+'   <div class="col-md-12 mb-3">'
		+'     <label for="City">City</label>'
		+'     <input type="text" class="form-control" id="City" placeholder="City" required>'
		+'      <div class="invalid-feedback">  '
		+'        Please provide a valid city.'
		+'      </div>'
		+'    </div>'
		+'    <div class="col-md-12 mb-3">'
		+'      <label for="State">State</label>'
		+'      <input type="text" class="form-control" id="State" placeholder="State" required>'
		+'      <div class="invalid-feedback">'
		+'        Please provide a valid state.'
		+'      </div>'
		+'    </div>'
		+'    <div class="col-md-12 mb-3">'
		+'      <label for="Zip">Zip</label>'
		+'      <input type="text" class="form-control" id="Zip" placeholder="Zip" required>'
		+'      <div class="invalid-feedback">'
		+'        Please provide a valid zip.'
		+'      </div>'
		+'   </div>'
		+'	<div class="avatar-upload">'
		+'	        <div class="avatar-edit">'
		+'	            <input type="file" id="imageUpload" accept=".png, .jpg, .jpeg" />'
		+'	            <label for="imageUpload"></label>'
		+'	        </div>'
			        
		+'	    </div>'
		+'  <button class="btn btncolor" type="submit" style="margin:0 auto;" id="submitData" onclick="getsocietyregisterdata()"><i class="glyphicon glyphicon-ok"></i>Submit form</button>'
		  
		  
		+'</form>'

		+'</div> '

		
		+'</div>'


		+'</div>'
		
		
		$('#main-div').html('');
		$('#main-div').html(RegisterDataDisplay);
		
		getsocietyregisterdata = function()
		{
   var SocietyName = $("#SocietyName").val();
    var Address = $("#Address").val();
    var City = $("#City").val();
    var State = $("#State").val();
    var Zip = $("#Zip").val();
    
    var societyData = {};
    
    societyData.SocietyName = SocietyName;
    societyData.Address = Address;
    societyData.City = City;
    societyData.State = State;
    societyData.Zip = Zip;
    
    console.log(JSON.stringify(societyData));
		}
	}
})(com.coep.test.ajaxHandler, com.coep.test.WaterData);
