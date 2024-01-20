let maxFrames = 1000; //without a frame count this code would draw splotches 4ever

function setup() {
  createCanvas(800, 600);
  noStroke();
}

function draw() {
  if (frameCount <= maxFrames) {
  let splatterColor = color(random(255), random(255), random(255), random(200, 255));

  let splatterSize = random(20, 50);
  let splatterX = random(width);
  let splatterY = random(height);


  fill(splatterColor);
  beginShape();

  for (let i = 0; i < 360; i++) { 
    //this gives us the splotchy effect by modifying the shape of the splotches and giving us 360 points for the splotch
    //then randomizing the angle and radius for each splotch

    let angle = random(TWO_PI);
    let radius = random(splatterSize * 0.5, splatterSize);
    let offsetX = cos(angle) * radius;
    let offsetY = sin(angle) * radius;
    vertex(splatterX + offsetX, splatterY + offsetY);
  }
  endShape(CLOSE);
}
else
{
  noLoop();
}
} 

