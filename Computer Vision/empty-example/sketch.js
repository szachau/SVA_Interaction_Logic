var video;
var vScale = 16;

var particles = [];

var slider;

function setup() {
  background(51);
  createCanvas(1920, 1080);
  pixelDensity(1);
  video = createCapture(VIDEO);
  video.size(width/vScale, height/vScale);
  for (var i = 0; i < 80; i++) {
    particles[i] = new Particle(random(width), random(height));
  }
  slider = createSlider(0, 255, 127);
  background(36, 39, 57);
}

function Particle(x, y) {
  this.x = x;
  this.y = y;
  this.r = random(1, 6);
  
  this.update = function() {
    this.x += random(-10, 10);
    this.y += random(-10, 10);

    this.x = constrain(this.x, 0, width);    
    this.y = constrain(this.y, 0, height);    
  }
  
  this.show = function() {
    noStroke();
    var px = floor(this.x / vScale);
    var py = floor(this.y / vScale);
    var col = video.get(px, py);
    //console.log(col);
    fill(200, col[1], col[2], slider.value());
    rect(this.x, this.y, this.r, this.r);    
  }
  
}





function draw() {
  
  video.loadPixels();
  for(var i = 0; i < particles.length; i++) {
    particles[i].update();
    particles[i].show();
  }
}



