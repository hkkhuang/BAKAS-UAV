const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        // Counterfeit GCS
        const GCSAddress = "0x69130Db7eeBF4B62Da666BA693ACE09175BFFd05";

        // UAV
        const UAVAddress = "0x80583f873d9B1335eA731Dfd0De9790bE5334F2A";
        console.log("The account address for this invoke is:",GCSAddress);
        
        let result = await deployedBAKASUAV.registerUAV(UAVAddress, {from: GCSAddress});

    } catch (error) {
        // console.log(error);
        console.log("The unauthorized GCS attempts to register UAVs!");        
    }

    callback();
};
