const sendText = require("./sendText");

const pingSound = async (i) => {
  return new Promise(function (resolve, reject) {
    let { PythonShell } = require("python-shell");
    let pyshell = new PythonShell("./play_sound.py", { args: ["./helgwerge.wav"] });
    pyshell.on("message", function (message) {
      console.log("message: ", message);
    });
    pyshell.end(function (err, code, signal) {
      if (err) {
        console.log("err: ", err);
        console.log("code: ", code);
        console.log("signal: ", signal);
        return resolve(err);
      }
      return resolve("Sound Played");
    });
    setTimeout(() => {
      pingSound(i++);
      return resolve("time_out");
    }, 15000);
  });
};

const triggerAlert = async (text) => {
  console.log("Alert Triggered: ", text);
  pingSound(1);
  sendText(
    process.env.MY_NUMBER,
    "RTX 8080 Inventory Scrape Problem Detected. \nstill check best buy thouugh\nhttps://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
  );
};

module.exports = triggerAlert;
