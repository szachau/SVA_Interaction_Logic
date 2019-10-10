var serial; // variable to hold an instance of the serialport library
var portName = 'COM3'; //fill in serial port name here
var inData;
var xPos = 0;
var nParticles = 80;
var particles = [];
var particleSize = 80;
var maxCounter = 120;
var lines = [];

function checkCollisions() {
  lines = [];
  for(var i=0;i<nParticles;i++){
    for(var j=0;j<nParticles;j++) {
      if(i!=j) {
        var distance = p5.Vector.dist(
          particles[i].position,
          particles[j].position
        );
        if(distance < particleSize) {
          if(particles[i].counter == 0) {
            particles[i].direction.rotate(Math.random());
            particles[i].counter = maxCounter;
          }  
          if(particles[j].counter == 0) {
            particles[j].direction.rotate(Math.random());
            particles[j].counter = maxCounter;
          }
          lines.push(
            [particles[i].position, 
             particles[j].position,
             distance
            ]
          );  
        } 
      }  
    }
  }
}

function createParticle() {
  var particle = {};
  particle.position = createVector(
    Math.random() * width,
    Math.random() * height
  );
  particle.direction = createVector(
    Math.random(),
    Math.random()
  );
  particle.update = function() {
    this.position.add(this.direction);
    if(this.position.x > width ||
      this.position.x < 0)
      this.position.x = width/2;
     if(this.position.y > height ||
      this.position.y < 0)
      this.position.y = height/2;
    if(this.counter > 0)
      this.counter -= 1;
  }
  particle.counter = 0;
  return particle;
  
}



function setup() {
 serial = new p5.SerialPort(); // make a new instance of the serialport library
 serial.on('list', printList); // set a callback function for the serialport list event
 serial.on('connected', serverConnected); // callback for connecting to the server
 serial.on('open', portOpen);        // callback for the port opening
 serial.on('data', serialEvent);     // callback for when new data arrives
 serial.on('error', serialError);    // callback for errors
 serial.on('close', portClose);      // callback for the port closing
 
 serial.list(); // list the serial ports
 serial.open(portName);              // open a serial port 
 createCanvas(800, 800);
  background(800);
  stroke(0, 80);
  fill(0, 90);
  
  for(var i=0;i<nParticles;i++) {
      particles.push(createParticle());
}
   background(0);
}  


// get the list of ports:
function printList(portList) {
 // portList is an array of serial port names
 for (var i = 0; i < portList.length; i++) {
 // Display the list the console:
 console.log(i + " " + portList[i]);
 }
}


function serverConnected() {
  console.log('connected to server.');
}
 
function portOpen() {
  console.log('the serial port opened.')
}
 
 
function serialError(err) {
  console.log('Something went wrong with the serial port. ' + err);
}
 
function portClose() {
  console.log('The serial port closed.');
}


function serialEvent() {
  inData = Number(serial.read());
}


function draw() {
   checkCollisions();
  for(var i=0;i<nParticles;i++) {
    particles[i].update();
    
  }
  for(var i=0;i<lines.length;i++) {
    var color = map(lines[i][2], 0, particleSize,
                   0, 255);
    stroke(color, inData, 200, 5);
    line(
      lines[i][0].x, lines[i][0].y,
      lines[i][1].x, lines[i][1].y
    );  
  }  
}