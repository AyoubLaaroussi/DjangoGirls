

function comment_like(pk){
	//var objeto = $('.like').attr('likes');
	$.ajax({
		url: "/comment/"+pk+"/like",
		type: "POST",
		/*data: {
			objeto:objeto
		},*/

		success: function(json){
			$('.like').val('');
			console.log(json);
			contador= '#likecontador_'+json.comment_pk
			$(contador).html(json.likes);
			console.log(json);
		}

		
	});
};
function comment_dislike(pk){
	//var objeto = $('.like').attr('likes');
	$.ajax({
		url: "/comment/"+pk+"/dislike",
		type: "POST",
		/*data: {
			objeto:objeto
		},*/

		success: function(json){
			$('.dislike').val('');
			console.log(json);
			contador= '#dislikecontador_'+json.comment_pk
			$(contador).html(json.dislikes);
			console.log(json);
		}

		
	});
};

$('.like').on('click', function(event){
	event.preventDefault();
	comment_like(this.getAttribute("id-likes"))
});


$('.dislike').on('click', function(event){
	event.preventDefault();
	comment_dislike(this.getAttribute("id-dislikes"))
})