const blob = document.querySelector('#blob__1');
const illImage = document.querySelector('.image__ill');
const contentSlides = document.querySelectorAll('.content');
const nav = document.querySelector('.nav__bar');
const main = document.querySelector('.main');
let maxSlideText = 6;
let curSlideText = 0;

// F U N C T I O N S
const funcSlideText = function (slide) {
  contentSlides.forEach(
    (c, i) => (c.style.transform = `translateY(${100 * (i - slide)}%)`)
  );
  contentSlides.forEach(c => (c.style.transition = 'ease-in-out all 1.5s'));
};
const contentTimer = function () {
  setInterval(function () {
    curSlideText++;
    funcSlideText(curSlideText);
    if (curSlideText === maxSlideText) {
      curSlideText = -1;
      curSlideText++;
      funcSlideText(curSlideText);
    }
  }, 1500);
};
const blobCallback = function (entries) {
  const [entry] = entries;
  if (entry.isIntersecting) illImage.classList.remove('image__ill--trans');
};
const blobOptions = {
  root: null,
  threshold: 0.5,
};
const mainCallback = function (entries) {
  const [entry] = entries;
  if (entry.isIntersecting) main.classList.remove('main--animation');
};
const mainOptions = {
  root: null,
  threshold: 0.5,
};
// M A I N
const mainObserver = new IntersectionObserver(mainCallback, mainOptions);
const blobObserver = new IntersectionObserver(blobCallback, blobOptions);
mainObserver.observe(nav);
blobObserver.observe(blob);
contentTimer();
