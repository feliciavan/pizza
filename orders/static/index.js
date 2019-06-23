document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#num_order').innerHTML =  {{ num_order|safe }};
    document.querySelector('#cart').onclick= () => {
      const request = new XMLHttpRequest();
      request.open('POST', '/order');
      // Callback function for when request completes
      request.onload = () => {
          const data = JSON.parse(request.responseText);
          document.querySelector('#num_order').innerHTML = data.num_order;
      }
      var num_order = document.querySelector('#num_order').innerHTML;
      num_order++;
      const data = new FormData();
      data.append('num_order', num_order);
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
      request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      request.send(data);
      return false;
    }
});
