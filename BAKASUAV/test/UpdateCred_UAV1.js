const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        // UAV
        const UAVAddress = "0xffb0A93747a34f0bBA3A7c940E3F6d91FdE706D5";

        const isRegistered = await deployedBAKASUAV.registeredUAVs(UAVAddress);
        if (!isRegistered) {
            throw new Error("UAV is not registered.");
        }

        const Cred = [220001, 220001];
        const ET = 20230228;
        const npid = 20001;

        let result = await deployedBAKASUAV.UpdateCred(Cred, ET, npid, {from: UAVAddress});
        // console.log("UpdateCred called: ", result);
        console.log("UAV1 Update Cred:");
        console.log("pid",npid);
        console.log("Cred:",Cred);
        console.log("ET:",ET);
        


    } catch (error) {
        console.error("Error in script:", error);
        console.log("The unauthorized UAV attempts to Update Cred!");
    }

    callback();
};