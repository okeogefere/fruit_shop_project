 //add to cart button
//  $("#add-to-cart-btn").on("click", function(){
//     let quantity = $("#quantity").val()
//     let product_title = $(".product-title").val()
//     let product_id = $(".product-id").val()
//     let product_price = $("#price").text()
//     let this_val = $(this)

//     console.log('Quantity:', quantity);
//     console.log('Title:', product_title);
//     console.log('ID:', product_id);
//     console.log('Price:', product_price);
//     console.log('This is:', this_val);


//     $.ajax({
//         url: '/add-to-cart/',
//         data: {
//             'id': product_id,
//             'quantity': quantity,
//             'title': product_title,
//             'price': product_price
//         },
//         dataType: 'json',
//         beforeSend: function(){
//             console.log('Adding to cart...');

//         },
//         success: function(res){
//             this_val.html('item added to cart')
//             console.log('Added to cart...');
//             $('#cartcount').text(res.totalcartitems)
            
//         },
//         error: function(xhr, status, error) {
//             console.error('Error adding to cart:', error);
//         }
//     });
        
//  });

$(".add-to-cart-btn").on("click", function(){
    
    let this_val = $(this)
    let index = this_val.attr('data-index')


    let quantity = $(".product-quantity-" + index).val()
    let product_title = $(".product-title-" + index).val()

    let product_id = $(".product-id-" + index).val()
    let product_price = $("#price-" + index).text()

    let product_pid = $(".product-pid-" + index).val()
    let product_image=$(".product-image-" + index).val()
    
    console.log('Quantity:', quantity);
    console.log('Title:', product_title);
    console.log('Price:', product_price);
    console.log('ID:', product_id);
    console.log('PID:', product_pid);
    console.log('Image:', product_image);
    console.log('Index:', index);
    
    console.log('This is:', this_val);

    $.ajax({
        url: '/add-to-cart/',
        data: {
            'id': product_id,
            'pid': product_pid,
            'image': product_image,
            'quantity': quantity,
            'title': product_title,
            'price': product_price
        },
        dataType: 'json',
        beforeSend: function(){
            console.log('Adding to cart...');

        },
        success: function(res){
            this_val.html('✔️')
            console.log('Added to cart...');
            $('#cartcount').text(res.totalcartitems)
            
        },
        error: function(xhr, status, error) {
            console.error('Error adding to cart:', error);
        }
    });
    
});
$(".delete-product").on("click", function(){
    let product_id = $(this).attr('data-product')
    let this_val = $(this)

    console.log('Product ID:', product_id);

    
    $.ajax({
        url: '/delete-item-from-cart',
        data: {
            'id': product_id
        },
        dataType: 'json',
        beforeSend: function(){
            this_val.hide()
        },
        success: function(res){
            this_val.show()
            $('#cartcount').text(res.totalcartitems)
            $('#cart-list').html('res.data')
        },
        
    })
});
