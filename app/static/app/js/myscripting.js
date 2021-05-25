$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    //console.log(id)
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data:{
            prod_id: id
        },
        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerHTML = data.amount
        }
    })
})


$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    //console.log(id)
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data:{
            prod_id: id
        },
        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerHTML = data.amount
        }
    })
})


$('.remove-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this
    console.log(id)
    $.ajax({
        type: "GET",
        url: "/removecart",
        data:{
            prod_id: id
        },
        success: function (data) {
            console.log("Delete")
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerHTML = data.amount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})



/*-1-----------------------------------*/
$(document).on('click','.member-1',function(){
    $('.detail-box-1').toggleClass('show-details-1')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-6').removeClass('show-details-6')
});
/*-2-----------------------------------*/
$(document).on('click','.member-2',function(){
    $('.detail-box-2').toggleClass('show-details-2')
    $('.detail-box-1').removeClass('show-details-1')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-6').removeClass('show-details-6')
});
/*-3-----------------------------------*/
$(document).on('click','.member-3',function(){
    $('.detail-box-3').toggleClass('show-details-3')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-1').removeClass('show-details-1')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-6').removeClass('show-details-6')
});
/*-4-----------------------------------*/
$(document).on('click','.member-4',function(){
    $('.detail-box-4').toggleClass('show-details-4')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-1').removeClass('show-details-1')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-6').removeClass('show-details-6')
});
/*-5-----------------------------------*/
$(document).on('click','.member-5',function(){
    $('.detail-box-5').toggleClass('show-details-5')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-1').removeClass('show-details-1')
    $('.detail-box-6').removeClass('show-details-6')
});
/*-6-----------------------------------*/
$(document).on('click','.member-6',function(){
    $('.detail-box-6').toggleClass('show-details-6')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-1').removeClass('show-details-1')
});

/*-cancel------------------*/
$(document).on('click','.cancel',function(){
    $('.detail-box-1').removeClass('show-details-1')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-6').removeClass('show-details-6')
});


const btns = document.querySelectorAll(".btn");

btns.forEach((btn) => {
    btn.addEventListener("mousemove", function(e){
        const position = btn.getBoundingClientRect();
        const x = e.pageX - position.left - position.width / 2;
        const y = e.pageY - position.top - position.height / 2;

        btn.children[0].style.transform = "translate(" + x * 0.3 + "px, " + y * 0.5 + "px)";
    });
});

btns.forEach((btn) => {
    btn.addEventListener("mouseout", function(e){
        btn.children[0].style.transform = "translate(0px, 0px)";
    });
});

let star = document.querySelectorAll('input');
let showValue = document.querySelector('#rating-value');
for (let i = 0; i < star.length; i++) {
	star[i].addEventListener('click', function() {
		i = this.value;

		showValue.innerHTML = i + " out of 5";
	});
}