require("dotenv").config();
const checkProductStatus = require("./checkProductStatus");
const triggerAlarm = require("./triggerAlarm");
const triggerAlert = require("./triggerAlert");
const yieldLocation = require("./yieldLocation");

const tMin = 5 * 60 * 1000; //min timeout (ms)
const tMax = 15 * 60 * 1000; //max timeout (ms)

let cycling = true;

const stopCycler = () => {
  cycling = false;
};
const num = (min, max) => Math.floor(Math.random() * (max - min)) + min;

const randomTimeout = () => {
  const ranMilli = num(tMin, tMax);
  console.log("Interval:", Math.round(ranMilli * 100 / 60000) / 100, "minutes");
  return ranMilli;
};

const gen = yieldLocation();

const cycler = async (i) => {
  try {
    location = gen.next().value;
    const status = await checkProductStatus(i, stopCycler, location);
    // const status = "Sold Out";
    switch (status) {
      case "Sold Out":
        if (cycling) {
          return setTimeout(() => {
            cycler(++i);
          }, randomTimeout()); //wait 5 minutes to start next fork
        }
      case "Check Now":
        console.log("status: ", status);
        return "Check Now";
        case "Problem":
          console.log("status: ", status);
          return "Problem";
        }
      } catch (error) {
        console.log("error: ", error);
        return false;
      }
    };

    const processManager = async (i) => {
  const cyclerStatus = await cycler(i, gen);
  if (cyclerStatus === "Check Now") {
    triggerAlarm("MAY NOT BE SOLD OUT");
  } else if (cyclerStatus === "Problem") {
    triggerAlert("a problem occurred in .py, MAY NOT BE SOLD OUT THOUGH! Still check.");
  }
};

try {
  processManager(1);
} catch (error) {
  console.log(error);
}

module.exports = processManager;
