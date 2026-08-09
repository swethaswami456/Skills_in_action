function Online_Appointment() {
    alert("Available by appointment and offline direct visit to clinic during open hours");
}

function In_person_Appointment() {
    alert("Please call us at 📞 98765 43210");
}


// // For transformation Slideshow
// // document.addEventListener("DOMContentLoaded", function() {
// var slideIndex = 1;
// showDivs(slideIndex);

// function plusDivs(n) {
//   showDivs(slideIndex += n);
// }

// function showDivs(n) {
//   var i;
//   var x = document.getElementsByClassName("trans_img_cls");
//   if (n > x.length) {slideIndex = 1}
//   if (n < 1) {slideIndex = x.length} ;
//   for (i = 0; i < x.length; i++) {
//     x[i].style.display = "none";
//   }
//   x[slideIndex-1].style.display = "block";
// }



// // Auto Slide
// document.addEventListener("DOMContentLoaded", function() {
// var slideIndex = 0;
// carousel();

// function carousel() {
//   var i;
//   var x = document.getElementsByClassName("trans_img_cls");
//   for (i = 0; i < x.length; i++) {
//     x[i].style.display = "none"; 
//   }
//   slideIndex++;
//   if (slideIndex > x.length) {slideIndex = 1} 
//   x[slideIndex-1].style.display = "block"; 
//   setTimeout(carousel, 2000); 
// }
// })


// // auto+manual
// document.addEventListener("DOMContentLoaded", function() {
//   var slideIndex = 1;
//   showDivs(slideIndex);
//   autoSlide();

//   // Manual controls
//   function plusDivs(n) {
//     showDivs(slideIndex += n);
//   }

//   function showDivs(n) {
//     var i;
//     var x = document.getElementsByClassName("trans_img_cls");
//     if (n > x.length) {slideIndex = 1}
//     if (n < 1) {slideIndex = x.length}
//     for (i = 0; i < x.length; i++) {
//         x[i].classList.remove("active");}
//     x[slideIndex-1].classList.add("active");}


//       x[i].style.display = "none";
//     }
//     x[slideIndex-1].style.display = "block";
//   }

//   // Auto slide
//   function autoSlide() {
//     slideIndex++;
//     showDivs(slideIndex);
//     setTimeout(autoSlide, 3000); // every 3 seconds
//   }

//   // Expose manual controls to buttons
//   window.plusDivs = plusDivs;
// });


// let slideIndex = 0;
// const slides = document.getElementsByClassName("trans_img_cls");

// function showSlide(n) {
//   // reset classes
//   for (let i = 0; i < slides.length; i++) {
//     slides[i].classList.remove("active", "prev");
//   }

//   slideIndex = (n + slides.length) % slides.length; // wrap around
//   let prevIndex = (slideIndex - 1 + slides.length) % slides.length;

//   slides[slideIndex].classList.add("active");
//   slides[prevIndex].classList.add("prev");
// }

// function plusDivs(n) {
//   showSlide(slideIndex + n);
// }

// // Auto slide
// function autoSlide() {
//   plusDivs(1);
//   setTimeout(autoSlide, 2000);
// }

// // Initialize
// showSlide(slideIndex);
// autoSlide();


document.addEventListener("DOMContentLoaded", function() {
  var slideIndex = 0;
  showDivs(slideIndex);
  autoSlide();

  function plusDivs(n) {
    slideIndex += n;
    if (slideIndex >= document.getElementsByClassName("trans_img_cls").length) {
      slideIndex = 0;
    }
    if (slideIndex < 0) {
      slideIndex = document.getElementsByClassName("trans_img_cls").length - 1;
    }
    showDivs(slideIndex);
  }

  function showDivs(n) {
    var x = document.getElementsByClassName("trans_img_cls");
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("active");
    }
    x[n].classList.add("active");
  }

  function autoSlide() {
    slideIndex++;
    if (slideIndex >= document.getElementsByClassName("trans_img_cls").length) {
      slideIndex = 0;
    }
    showDivs(slideIndex);
    setTimeout(autoSlide, 4000);
  }

  window.plusDivs = plusDivs;
});
