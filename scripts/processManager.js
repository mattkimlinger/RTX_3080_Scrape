require("dotenv").config();
const checkProductStatus = require("./checkProductStatus");
const triggerAlarm = require("./triggerAlarm");
const triggerAlert = require("./triggerAlert");
const timeout = 8 * 60 * 1000; //8min timeout
let cycling = true;
const stopCycler = () => {cycling = false};

const cycler = async (i) => {
  try {
    const status = await checkProductStatus(i, stopCycler);
    switch (status) {
      case "Sold Out":
        if (cycling) {
          return setTimeout(() => {
            cycler(++i);
          }, timeout); //wait 5 minutes to start next fork
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
  const cyclerStatus = await cycler(i);
  if (cyclerStatus === "Check Now") {
    triggerAlarm("MAY NOT BE SOLD OUT");
  } else if (cyclerStatus === "Problem") {
    triggerAlert("a problem occurred in .py, MAY NOT BE SOLD OUT THOUGH! Still check.");
  }
};

try {
  processManager(1)
} catch (error) {
  console.log(error);
}

module.exports = processManager;
