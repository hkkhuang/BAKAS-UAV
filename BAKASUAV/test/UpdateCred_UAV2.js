const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        const UAVAddress = "0x543C1B8EEf6A9ad69cfab220C097425C1b38ACf9"; 

        const isRegistered = await deployedBAKASUAV.registeredUAVs(UAVAddress);
        if (!isRegistered) {
            throw new Error("UAV is not registered.");
        }

        const npid = 30001;
        const Cred = [320001, 320001]; 
        const ET = 20240228;
        
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