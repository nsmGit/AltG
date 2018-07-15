window.onload = function () {
  //sideNavè¨­å®š
  var elemSideNav = document.querySelector('.sidenav');
  var sideNavOptions = {
    draggable: false
  }
  var instance = M.Sidenav.init(elemSideNav, sideNavOptions);

  //selectè¨­å®š
  var elemSelect = document.querySelectorAll('select');
  var selectOptions = {};
  var instances = M.FormSelect.init(elemSelect, selectOptions);
}