  $.ajax({
        
        url:"/getroomtypes",

        method:"GET",
        success: function(data) {
            page=document.getElementById("root")
            ulist=document.createElement("ul")
            data_length=data.length
            for(var i=0;i<data_length;i++){
           //para=document.createElement("p");
            ls=document.createElement("li")
            ls.innerHTML=data[i]['name'];
            ulist.appendChild(ls);

            }
           page.appendChild(ulist);
           

        },
        
    });

    /*$('#addRoom').click(function(event){

    event.preventDefault()
    $.ajax({
        type:"POST",
        url:"/createroomtype",
        data:{
            name:$('#name').val(),
            description:$('#description').val()
        },
        success:function(data){
            alert("Success")
        }

    });
});*/

//The functions below facilitate sending of csrftokenmiddleware don't delete them
function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});