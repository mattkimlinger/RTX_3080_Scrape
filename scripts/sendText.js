
const sendText = async (number, message) => {
  try {
    const twilioClient = require("twilio")(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);
    return twilioClient.messages
      .create({
        to: number,
        from: process.env.TWILIO_NUMBER,
        body: `${message}`,
      })
      .then(async (res) => {
        console.log(`sent text to ${number} || sid: ${res.sid}`);
        return true;
      });
  } catch (error) {
    console.log("sendEmergencyText Error:", error);
    return false;
  }
};

module.exports = sendText;
