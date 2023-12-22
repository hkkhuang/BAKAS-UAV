const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        // UAV
        const UAVAddress = "0x543C1B8EEf6A9ad69cfab220C097425C1b38ACf9";

        let isRegistered = await deployedBAKASUAV.registeredUAVs(UAVAddress);
        console.log("UAV Account:", UAVAddress);
        console.log("Is UAV Registered:", isRegistered);

    } catch (error) {
        console.error("Error in script:", error);
    }

    callback();
};