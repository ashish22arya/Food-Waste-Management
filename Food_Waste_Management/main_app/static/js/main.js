$(document).ready(function(){
	$('#myForm').submit(retrieveStudentData);
});

// To retrieve student data
function retrieveStudentData(event){
	event.preventDefault();
	var rollNum = $(this).find('#rollNo').val();
	$.ajax('/api/' + rollNum + '/?format=json',{
		success: function(response){
			$('#profile').html(`
				<ul class = "list-group">
					<li class = "list-group-item">Roll number: ${response.rollNum}</li>
				    <li class = "list-group-item">Name: ${response.name}</li>
					<li class = "list-group-item">Branch: ${response.branch}</li>
					<li class = "list-group-item">Hostel Address: Room number: ${response.roomNum} ${response.hostel}</li>
					<li class = "list-group-item">Contact: ${response.contactNum}</li>
				</ul>
				`)
		} ,
		error: function(request){
			alert("Error: "+ request.statusText + ' '+request.responseText);
		}
	});
}