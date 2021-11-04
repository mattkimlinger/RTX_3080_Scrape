const yieldLocation = function* () {
  while (true) {
    yield { city: "maplewood", lat: 45.03996, lng: -93.02489 }
    yield { city: "oakdale", lat: 44.95355, lng: -92.92782 }
    yield { city: "eagan", lat: 44.83338, lng: -93.15394 },
    yield { city: "blaine", lat: 45.12312, lng: -93.26002 }
    yield { city: "roseville", lat: 45.01684, lng: -93.16048 }
    yield { city: "apple valley", lat: 44.72621, lng: -93.21359 }
  }
};

module.exports = yieldLocation;
