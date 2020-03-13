
function check_uname()
{
	var username = document.getElementById('username').value;
	if(username)
	{
		xhr = new XMLHttpRequest();
		username = username.replace(/[^a-zA-Z0-9]/g, '');
		xhr.open('POST','/ajaxreq/'+username);
		xhr.send();
		  xhr.onreadystatechange = function() 
		  {
  			  if (xhr.readyState == 4) 
  			  	{
      				var data = xhr.response;
      				if (data == 0)
      					{
							document.getElementById('username_err').innerHTML = "username doesn't exist so signup"      						
      					}
    			}
			}
	

	}
}

//Function to remove the errors if the username field is touched again
function remove_err(id = 0)
{
	if (id == 0)
		document.getElementById('username_err').innerHTML = " ";
	else if(id =="u"){
		document.getElementById('u_err').innerHTML = " ";
		document.getElementById('u').style.border = "1px solid skyblue";

	}
	else if (id == "e"){
		document.getElementById('e_err').innerHTML = " ";
		document.getElementById('e').style.border = "1px solid skyblue";

	}
}


//------------------Function for the form2 validation -------------------
//ajax req
function check_uname_exist()
{
	var uname = document.getElementById('u').value;
	
	if (uname)
	{
		//no special char other than -
		var flag = uname.search(/[^a-zA-Z0-9-]/g)		//Flag will be -1 if there are no special characters
														// if there is any special characters then flag will have the index
		if (flag!=-1)
		{

			console.log(" special characters are at",flag);
			document.getElementById('u_err').innerHTML = "username cann't have any special characters";
			var bdr = document.getElementById('u');
			bdr.style.border = "1px solid red";
		}
		else {

				var xhr = new XMLHttpRequest();
				xhr.open('POST','/ajax_check_u/'+uname);
				xhr.send()
				xhr.onreadystatechange = function() 
		 		 {
  			  		if (xhr.readyState == 4) 
  			  			{
      						var data = xhr.response;
      						if (data == 1)
      							{
      								document.getElementById('u_err').innerHTML = "Username already exist chose another";
      								var bdr = document.getElementById('u');
									bdr.style.border = "1px solid red";
      							}		
      						else if (data == 0)	// 0 means username like this is not found
      						{
      							console.log("ready to go");
      						}
    					}
				}
		
		}
	}
}

//ajax req for checking email
function check_email_exist()
{

		var email = document.getElementById('e').value;
		if (email)
		{
			var xhr = new XMLHttpRequest();
			xhr.open('POST','/ajax_check_e/');
			content = email
			xhr.send(content)
			xhr.onreadystatechange = function() 
				 {
			  		if (xhr.readyState == 4) 
			  			{
							var data = xhr.response;
							if (data == 1)
								{
									document.getElementById('e_err').innerHTML = "email already exist chose another";
									var bdr = document.getElementById('e');
									bdr.style.border = "1px solid red";
								}		
							else if (data == 0)			//0 means no email found like this
							{
								console.log("ready to go");
							}
						}
			
				  }
		}
}//outer email function














//Issues!!!!
/*
	The problem is I am calling diferent functions for all the  fields
	and also creating ajax req for every particular function
	so no of request can increase








*/
