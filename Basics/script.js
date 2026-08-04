console.log("JS loaded");

// for(let i = 0; i < 50; i++) {
//     const p = document.createElement("div");
//     p.className = "particle";
//     document.body.appendChild(p);
// }

// for(let i = 0; i < 50; i++) {

//     const p = document.createElement("div");

//     p.className = "particle";

//     p.style.left = Math.random() * 100 + "vw";
//     p.style.top = Math.random() * 100 + "vh";

//     p.style.width = Math.random() * 15 + 5 + "px";
//     p.style.height = p.style.width;

//     document.body.appendChild(p);
// }

for(let i = 0; i < 50; i++) {

    const p = document.createElement("div");

    p.className = "group_particle";

    const size = Math.random() * 15 + 5;

    p.style.width = size + "px";
    p.style.height = size + "px";

    p.style.left = Math.random() * 100 + "vw";
    p.style.top = Math.random() * 100 + "vh";

    p.style.animationDuration =
        (Math.random() * 6 + 4) + "s";

    document.body.appendChild(p);
}
