// 220403 bngsh : /form loading bar 
const links = document.querySelectorAll(".loading_slider");
for (let i = 0; i < links.length; i++) {
  const link = links[i];
  const qFrac = link.nextElementSibling.innerText.substr(11).split('/');
  const qPercent = Math.floor((Number.parseInt(qFrac[0])-1)*100/Number.parseInt(qFrac[1]));
  console.log(qPercent);
  console.log(qPercent+'%');
  link.style.setProperty('--loadWidth', qPercent+'%');
}
// END of /form loading bar 

function scrollDown() {
  const vheight = $('.test').height();
  
  $('html, body').animate({
    // scrollTop: ((Math.floor($(window).scrollTop() / vheight)+1) * vheight)
    scrollTop: $(window).scrollTop() + vheight
  }, 500);
}

function scrollUp() {
  const vheight = $('.test').height();
  
  $('html, body').animate({
    // scrollTop: ((Math.ceil($(window).scrollTop() / vheight)-1) * vheight)
    scrollTop: $(window).scrollTop() - vheight
  }, 500);
}

$(function(){
  $('.next_btn').click(function(e){
    let divs = $(this).parent().parent().prev().children();
    let inputs = divs.find('input:checked');
    if(inputs.length < 1) {
      alert('체크 후 넘겨주세요!');
      return false;
    }
    e.preventDefault();
    scrollDown();
  });
  
  $('.prev_btn').click(function(e){
    e.preventDefault();
    scrollUp();
  });
  
  $("#form").submit(function() {
  let radios = $('input[type=radio]:checked');
  if(radios.length < 12) {  // TODO: replace this hardcoding with question#
    alert("모든 문항에 대답해주세요!");
    return false;
  }
  return true;
  });
  
  $('html, body').animate({
    scrollTop: 0
  }, 500);

});