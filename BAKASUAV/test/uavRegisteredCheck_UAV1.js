const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        // UAV
        const UAVAddress = "0xffb0A93747a34f0bBA3A7c940E3F6d91FdE706D5";

        let isRegistered = await deployedBAKASUAV.registeredUAVs(UAVAddress);
        console.log("UAV Account:", UAVAddress);
        console.log("Is UAV Registered:", isRegistered);

    } catch (error) {
        console.error("Error in script:", error);
    }

    callback();
};