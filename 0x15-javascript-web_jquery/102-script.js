$(document).ready(function() {
  
  $('INPUT#btn_translate').click(function(){
   sayHello();});

  $('INPUT#language_code').on('focus', function(){
    $(this).keypress(function(event){
      if(event.which === 13){
        sayHello();}
    });

  });
});

function sayHello(){
    let url = 'https://hellosalut.stefanbohacek.dev/?lang=' + $('INPUT#language_code').val();
    $.get(url, function(data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
}
