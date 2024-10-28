function menuClicked() {
   if (menu_options.style.display == 'flex') {
      menu_options.style.display = 'none'
   }

   else {
      menu_options.style.display = 'flex'
   }
}

function backTop() {
   document.documentElement.scrollTop = 0;
}