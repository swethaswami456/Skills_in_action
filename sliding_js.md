Ah, I see what you’re exploring — you’ve already tried toggling visibility with `.active` and `display: none/block`. That’s one way, but there are several other approaches to achieve the same slideshow/fade effect without relying on `display`. Each has different trade‑offs:

- **Opacity toggling**  
  Instead of `display: none`, you can keep all images in place and fade them in/out with `opacity: 0` and `opacity: 1`. This is smoother for transitions because `display` doesn’t animate. You already used this in your `.trans_img_cls.active` example.

- **Visibility property**  
  Use `visibility: hidden` and `visibility: visible`. Unlike `display`, the element still occupies space, but it won’t be seen or interactable. Can be combined with `opacity` for fade effects.

- **Z-index layering**  
  Stack all images on top of each other with `position: absolute` and then bring the active one to the front using `z-index`. This avoids toggling display and makes transitions easier.

- **Transform scaling**  
  Hide inactive slides by scaling them down (`transform: scale(0)`), and show the active one with `transform: scale(1)`. This can create zoom‑in/out effects.

- **CSS clip-path or mask**  
  You can hide/show slides by clipping them out of view, then animating the clip path for creative transitions.

- **CSS animations/keyframes**  
  Instead of toggling classes manually, you can define a keyframe animation that cycles through opacity or transforms automatically.

👉 In short: `display: none/block` is the most basic, but for smooth transitions you’ll usually prefer `opacity`, `visibility`, or `z-index` layering.  

Would you like me to sketch out a **ready‑to‑use fade slideshow snippet** using just `opacity` and `z-index` (no `display` at all), so you can drop it into your current code?








# Okay now, can I have other images at the left and right? Now i just have a plain backgroung



Yes — you can definitely place “preview” images to the left and right of your active slide instead of just showing a plain background. This is a common carousel pattern. There are a few ways to achieve it:

- **Flexbox layout**  
  Put all your images inside a flex container and use `justify-content: center`. The active image can be larger, while the left and right ones are smaller previews.  
  ```css
  .carousel {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    width: 100%;
    height: 100%;
  }
  .carousel img {
    flex: 0 0 auto;
    width: 20%;   /* side images */
    opacity: 0.5;
    transition: all 0.5s ease;
  }
  .carousel img.active {
    width: 60%;   /* main image */
    opacity: 1;
  }
  ```

- **Absolute positioning**  
  Keep your current absolute setup, but assign each image a position:  
  ```css
  .slide.left {
    position: absolute;
    left: 10%;
    top: 50%;
    transform: translateY(-50%);
  }
  .slide.center {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
  .slide.right {
    position: absolute;
    right: 10%;
    top: 50%;
    transform: translateY(-50%);
  }
  ```

- **CSS grid**  
  Use a three‑column grid: left preview, main image, right preview.  
  ```css
  .carousel {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    align-items: center;
    width: 100%;
    height: 100%;
  }
  .carousel img {
    width: 100%;
    object-fit: contain;
  }
  ```

- **Transform translateX**  
  Keep all images in one row and slide them left/right with `transform: translateX(...)` depending on the active index. This is how many JavaScript carousels work.

👉 The simplest way for your current setup is to wrap your images in a flex container and scale/opacity the active one. That way you’ll see the left and right images as previews, instead of a plain background.  

Would you like me to sketch out a **ready‑to‑use HTML + CSS snippet** that shows three images (left, center, right) with the center one fading in/out as active?