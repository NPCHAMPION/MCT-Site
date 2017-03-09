
function showOrHide(element,action){
  if(action=='hide'){
    element.style.display = 'none';
  }
  else{
    element.style.display = 'block';
  }
}

// on login button click, show modal
var signinBtn = document.getElementById('signin-button')
var signinModal = document.getElementById('signin-modal')
signinBtn.onclick = function(){
  showOrHide(signinModal,'show');
}

// on signup button click, show modal
var signupModal = document.getElementById('signup-modal')
var signupBtn = document.getElementById('signup-button')
signupBtn.onclick = function(){
  showOrHide(signinModal, 'hide');
  showOrHide(signupModal, 'show');
}

// close modals buttons
var closeSignUp = document.getElementById('close-signup')
var closeSignIn = document.getElementById('close-signin')
closeSignIn.onclick = function(){
  showOrHide(signinModal, 'hide');
  showOrHide(signupModal, 'hide');
}

closeSignUp.onclick = function(){
  showOrHide(signupModal, 'hide');
  showOrHide(signinModal, 'hide');
}

// on click anywhere outside of modal, close modal
window.onclick = function(event){
  if (event.target == signinModal || event.target == signupModal){
      showOrHide(signinModal, 'hide');
      showOrHide(signupModal, 'hide');
  }
}
