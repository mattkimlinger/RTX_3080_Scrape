require("dotenv").config();
const moment = require("moment-timezone");

const checkProductStatus = async (i, stopCycler) => {
  try {
    return new Promise(async(resolve, reject) => {
      const startTime = moment().format();
      console.log("Initiating best_buy_scrape.py");
      let { PythonShell } = require("python-shell");
      let pyshell = new PythonShell("./best_buy_scrape.py");
      pyshell.on("message", async(message) => {
        switch (message) {
          case "Sold Out":
            console.log("RTX 8080 10GB still sold out on Bestbuy.com");
            return resolve("Sold Out");
            // await stopCycler();//testing
            // return resolve("Check Now");//testing
            // console.log("Problem");//testing
            // return resolve("Problem");//testing
          case "Check Now":
            console.clear();
            await stopCycler();
            console.log("PART COULD BE IN STOCK CHECK NOW! : ", moment().format());
            return resolve("Check Now");
          case "Problem":
            console.log("Problem");
            await stopCycler();
            return resolve("Problem");
          default:
            console.log(message);
        }
      });
      pyshell.end(async(err, code, signal) => {
        if (err) {
          console.log("err: ", err);
          console.log("code: ", code);
          console.log("signal: ", signal);
          await stopCycler();
          return reject('Problem');
        }
        console.log(`scrape #${i} ended ${startTime} - ` + moment().format());
      });

    });
  } catch (error) {
    console.log("checkProductStatus query error", error);
  }
};

module.exports = checkProductStatus;