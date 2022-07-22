function getCookie(cname) {
      let name = cname + "=";
      let decodedCookie = decodeURIComponent(document.cookie);
      let ca = decodedCookie.split(';');
      for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
          c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
          return c.substring(name.length, c.length);
        }
      }
      return "";
    }

function order( user_id , price_id , number_id){

      $(document).ready(function () {
            
           token = getCookie("csrftoken")
            
          number = document.getElementById(number_id).value
          price = document.getElementById(price_id).value

          $.ajax({
              type: 'POST',
              url: '/sell/home/registerorder/',
              data: { 'id':user_id,'price':price,'number':number ,"csrfmiddlewaretoken": token },
              cache: false,
              success: function (result) {
                  
                 if (result["status"] ==1){
                   alert("okay");
                   location.reload();
                 }
                 if (result["status"] ==0)alert(result["message"])

              },

          });
          

      })

  }


  function increase( user_id , price_id ){

      $(document).ready(function () {
            
           token = getCookie("csrftoken")
            
          price = document.getElementById(price_id).value

          $.ajax({
              type: 'POST',
              url: '/sell/increase/register/',
              data: { 'id':user_id,'price':price,"csrfmiddlewaretoken": token },
              cache: false,
              success: function (result) {
                  
                if (result["status"] ==1){
                  alert("okay");
                  location.reload();
                }
                 if (result["status"] ==0)alert(result["message"])
              },

          });
          
      })

  }