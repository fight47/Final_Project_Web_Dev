  $(document).ready(function() {

      $('.updateButton').on('click', function() {

          var product_id = $(this).attr('product_id');
          req = $.ajax({
              url: "/add_to_cart",
              type: 'POST',
              data: { product_id: product_id }
          });
          req.done(function(data) {
              console.log(data['items_in_cart_count'])
              $('#cartCount').text("Items in the cart " + data['items_in_cart_count']);

          });


      });

  });