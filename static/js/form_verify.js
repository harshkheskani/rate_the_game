function validate_form(thisform){
	with (thisform) {
		if (query.value==null || query.value==""){
			query.focus();
			return false;
		}else{
			return true;
		}
	}
}