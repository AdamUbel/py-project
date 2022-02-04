// NOTE modal functions

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("modalBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
if (btn) {
  btn.onclick = function () {
    modal.style.display = "block";
  };
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
  modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

// NOTE IMG script

var hoodieImg = document.getElementById("h-merch");
var teeImg = document.querySelector("#t-merch");
var otherImg = document.querySelector("#o-merch");
var allImg = document.querySelector("#a-merch");

const hoverEvent = function () {
  hoodieImg.style.backgroundImage = "url('static/img/merch/hoodie-1.jpg') ";
  hoodieImg.style.objectFit = "scale-down";
};

const hoverEvent2 = function () {
  hoodieImg.style.backgroundImage = "url('static/img/merch/hoodie-2.jpg') ";
  hoodieImg.style.objectFit = "scale-down";
  // setInterval(hoverEvent, 2000);
};
const hoverEvent3 = function () {
  teeImg.style.backgroundImage = "url('static/img/merch/tshirt-1.jpg') ";
  teeImg.style.objectFit = "scale-down";
};

const hoverEvent4 = function () {
  teeImg.style.backgroundImage = "url('static/img/merch/tshirt-2.jpg') ";
  teeImg.style.objectFit = "scale-down";
  // setInterval(hoverEvent3, 2000);
};
const hoverEvent5 = function () {
  otherImg.style.backgroundImage = "url('static/img/merch/other-1.jpg') ";
  otherImg.style.objectFit = "scale-down";
};

const hoverEvent6 = function () {
  otherImg.style.backgroundImage = "url('static/img/merch/other-2.jpg') ";
  otherImg.style.objectFit = "scale-down";
  // setInterval(hoverEvent5, 2000);
};
const hoverEvent7 = function () {
  allImg.style.backgroundImage = "url('static/img/merch/all-1.jpg') ";
  allImg.style.objectFit = "scale-down";
};

const hoverEvent8 = function () {
  allImg.style.backgroundImage = "url('static/img/merch/all-2.jpg') ";
  allImg.style.objectFit = "scale-down";
  // setInterval(hoverEvent7, 2000);
};

hoodieImg.addEventListener("mouseenter", hoverEvent2);
teeImg.addEventListener("mouseenter", hoverEvent4);
otherImg.addEventListener("mouseenter", hoverEvent6);
allImg.addEventListener("mouseenter", hoverEvent8);

hoodieImg.addEventListener("mouseout", hoverEvent);
teeImg.addEventListener("mouseout", hoverEvent3);
otherImg.addEventListener("mouseout", hoverEvent5);
allImg.addEventListener("mouseout", hoverEvent7);

// NOTE BUtton JS
