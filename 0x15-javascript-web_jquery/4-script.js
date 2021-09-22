/*
script that updates the text color of the <header> element to red (#FF0000)
when the user clicks on the tag DIV#red_header
 */

const header = $('HEADER');
const toggle = $('DIV#toggle_header');

if (!header.hasClass('red') && !header.hasClass('green')) {
  header.addClass('red');
  header.removeClass('green');
}

toggle.click(() => {
  if (header.hasClass('red')) {
    header.addClass('green');
    header.removeClass('red');
  } else {
    header.addClass('red');
    header.removeClass('green');
  }
});
