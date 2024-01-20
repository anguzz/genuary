let img;
let scale_factor = 0.50;

function preload() {
  // Load your image
  img = loadImage('../utils/skely.gif');
}


function setup() {
  createCanvas(1000, 1000);
  imageMode(CENTER);

  background(0, 0,0);
  
}

function droste(x, y, size, level) {
  if (level > 0) {
    image(img, x, y, size, size);
    droste(x, y, size * scale_factor, level - 1);

  
  }
}

function draw() {

  
  let drosteX = width / 2 + cos(frameCount * 0.02) * 200;
 // let drosteY = height / 2.2 + sin(frameCount * 0.02) * 200;

  droste(drosteX, 400, 400, 5);


}

