$(document).ready(function () {
    $('.closebtn').click(function () {
        document.getElementById('navbar').style.width = '0';
        document.getElementById('top').style.marginLeft = '0';
        document.body.style.backgroundColor = 'white';
    })
    $('.open-nav').click(function () {
        document.getElementById("navbar").style.width = "250px";
        document.getElementById("top").style.marginLeft = "250px";
        document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
        $('.open-nav').style.display = 'none'
    })
})