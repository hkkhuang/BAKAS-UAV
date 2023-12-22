const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        // UAV
        const UAVAddress = "0x69130Db7eeBF4B62Da666BA693ACE09175BFFd05";

        let isRegistered = await deployedBAKASUAV.registeredUAVs(UAVAddress);
        console.log("UAV Account:", UAVAddress);
        console.log("Is UAV Registered:", isRegistered);

    } catch (error) {
        console.error("Error in script:", error);
    }

    callback();
};