let particles = [];
const numParticles = 1000; 

function setup() {
  createCanvas(700, 700);

  for (let i = 0; i < numParticles; i++) {
    // offesets
    let xOffset = random(-10, 10);
    let yOffset = random(-10, 10);
    particles.push(new Particle(width / 2 + xOffset, height / 2 + yOffset));
  }
}

function draw() {
  background(0, 0, 110);

 
  for (let i = particles.length - 1; i >= 0; i--) {  // update particle
    particles[i].update();
    particles[i].display();

    
    if (particles[i].lifespan <= 0) { // condition to remove particles when past lifespan
      particles.splice(i, 1);
    }
  }
}

class Particle {
  constructor(x, y) {
    this.position = createVector(x, y);
    this.velocity = p5.Vector.random2D().mult(random(1, 3)); 
    this.lifespan = 255; // set lifespan
    this.color = color(random(255), random(255), random(255)); 
  }

  update() {
    this.position.add(this.velocity);
    this.lifespan -= 2; // decrease lifespan
  }

  display() {
    fill(this.color.levels[0], this.color.levels[1], this.color.levels[2], this.lifespan);
    noStroke();
    ellipse(this.position.x, this.position.y, 8, 8);
  }
}