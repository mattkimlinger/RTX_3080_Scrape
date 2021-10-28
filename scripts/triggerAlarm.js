const sendText = require("./sendText");

const pingSound = async (i) => {
  return new Promise(function (resolve, reject) {
    let { PythonShell } = require("python-shell");
    const options = {
      args: ["./VEC3_FX_Alarm_19.wav"],
    };
    let pyshell = new PythonShell("./play_sound.py", options);
    pyshell.on("message", function (message) {
      console.log("message: ", message);
    });
    pyshell.end(function (err, code, signal) {
      if (err) {
        console.log("err, code, signal: ", err, code, signal);
        return resolve('Problem');
      }
      return resolve("Sound Played");
    });
    setTimeout(() => {
      return pingSound(i++);
    }, 15000);
  });
};

console.log('MY_NUMBER: ', process.env.MY_NUMBER);

const triggerAlarm = async (text) => {
  console.log("Alarm Triggered: ", text);
  sendText(
    process.env.MY_NUMBER,
    "RTX 8080 Alarm triggered. \ncheck best buy\nhttps://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
  );
  pingSound(1);
};

module.exports = triggerAlarm;
