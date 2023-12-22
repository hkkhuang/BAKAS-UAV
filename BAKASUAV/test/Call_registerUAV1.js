const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();
        // GCS
        const GCSAddress = "0x3Dc856c56aC62FA1Bd4c5b560B8740AffB4f566A";
        // UAV
        const UAVAddress = "0xffb0A93747a34f0bBA3A7c940E3F6d91FdE706D5";

        let result = await deployedBAKASUAV.registerUAV(UAVAddress, {from: GCSAddress});
        // console.log("UAV Registered: ", result);
        console.log("UAV1 registered successfully！");
        console.log("UAV1 account:", UAVAddress);

    } catch (error) {
        console.log(error);
    }

    callback();
};
