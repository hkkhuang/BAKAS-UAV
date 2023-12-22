const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        // GCS
        const GCSAddress = "0x3Dc856c56aC62FA1Bd4c5b560B8740AffB4f566A";

        // UAV
        const UAVAddress = "0x543C1B8EEf6A9ad69cfab220C097425C1b38ACf9";
        
        let result = await deployedBAKASUAV.registerUAV(UAVAddress, {from: GCSAddress});
        // console.log("UAV Registered: ", result);
        console.log("UAV2 registered successfully！");
        console.log("UAV2 account:", UAVAddress);


    } catch (error) {
        console.log(error);
    }

    callback();
};
