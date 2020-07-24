var mailSend = document.getElementsByClassName('mailSend')[0];
var replaceSrc = function () {
	x = document.getElementsByClassName('lazy-load-me');
	for (i = 0; i < x.length; i++){
		if (x[i].getBoundingClientRect().top < window.innerHeight) {
			img = x[i]
			if(window.innerWidth < 850 && x[i].getAttribute('mobi-src') != null){
				lazySRC = x[i].getAttribute('mobi-src');
			}else{
				lazySRC = x[i].getAttribute('desk-src');		
			}
			if(x[i].tagName == 'VIDEO'){
				x[i].canPlayType("video/mp4");
				x[i].src = lazySRC;
				x[i].load();
				x[i].onload = x[i].play();
				x[i].classList.remove("lazy-load-me");
			}else{
				x[i].src = lazySRC;
				x[i].classList.remove("lazy-load-me");
			}
		}
	}
};
replaceSrc();
window.addEventListener('scroll', replaceSrc, false);


// The following code is based off a toggle menu by @Bradcomp
// source: https://gist.github.com/Bradcomp/a9ef2ef322a8e8017443b626208999c1
(function() {
    var burger = document.querySelector('.burger');
    var menu = document.querySelector('#'+burger.dataset.target);
    burger.addEventListener('click', function() {
        burger.classList.toggle('is-active');
        menu.classList.toggle('is-active');
    });
})();